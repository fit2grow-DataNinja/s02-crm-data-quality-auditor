"""Local, read-only FastAPI adapter. No AI model or external egress."""
import csv
import io
import json
import tempfile
import zipfile
from pathlib import Path
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import StreamingResponse
from s02.audit import audit, write_results

app = FastAPI(title='S02 CRM CSV Auditor', version='0.2.0', docs_url='/docs')
MAX_BYTES = 5 * 1024 * 1024

async def store_csv(upload: UploadFile, target: Path):
    if not upload.filename or not upload.filename.lower().endswith('.csv'):
        raise HTTPException(400, 'Only .csv files are supported')
    raw = await upload.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise HTTPException(413, 'CSV file exceeds 5 MiB limit')
    try:
        decoded = raw.decode('utf-8-sig')
        rows = csv.reader(io.StringIO(decoded))
        header = next(rows, [])
        if not header or any(not c.strip() for c in header):
            raise ValueError('Missing or empty CSV column header')
    except (UnicodeError, csv.Error, ValueError) as exc:
        raise HTTPException(400, f'Invalid UTF-8 CSV: {exc}') from exc
    target.write_bytes(raw)

@app.get('/health')
def health():
    return {'status':'ok','service':'s02-csv-auditor','external_ai':False}

@app.post('/audit')
async def run_audit(contacts: UploadFile = File(...), deals: UploadFile = File(...), associations: UploadFile | None = File(None)):
    with tempfile.TemporaryDirectory(prefix='s02_') as tmp:
        folder = Path(tmp)
        await store_csv(contacts, folder/'contacts.csv')
        await store_csv(deals, folder/'deals.csv')
        assoc_path = None
        if associations is not None:
            assoc_path = folder/'associations.csv'
            await store_csv(associations, assoc_path)
        try:
            summary, issues = audit(folder/'contacts.csv', folder/'deals.csv', assoc_path)
        except ValueError as exc:
            raise HTTPException(422, str(exc)) from exc
        write_results(summary, issues, folder/'output')
        payload = io.BytesIO()
        with zipfile.ZipFile(payload,'w',zipfile.ZIP_DEFLATED) as archive:
            for filename in ('summary.json','issues.csv','report.md'):
                archive.write(folder/'output'/filename, arcname=filename)
        payload.seek(0)
        return StreamingResponse(payload, media_type='application/zip', headers={'Content-Disposition':'attachment; filename="s02_audit_results.zip"','Cache-Control':'no-store'})

# Open WebUI integration

Status: Verified with synthetic CSV exports; reproduce and retest after importing source.

## Prerequisites
- S02 FastAPI running locally on port 8000.
- Open WebUI running in Podman and configured with a hosted chat model.
- Synthetic `contacts.csv` and `deals.csv` only, until SEC-001 is implemented and validated.

## Configure Workspace Tool
1. In Open WebUI, open **Workspace → Tools** and create a tool.
2. Paste the source from [`integrations/openwebui/s02_csv_audit_adapter.py`](../integrations/openwebui/s02_csv_audit_adapter.py) and save.
3. In chat, enable the Workspace Tool under **+ → Integrations**.
4. Attach files named `contacts.csv` and `deals.csv` and request an audit.
5. Inspect **View Result from run_s02_csv_audit**: expect `status: success`, `http_status: 200`, deterministic summary and report.

The adapter relies on Open WebUI's `__files__` metadata containing readable local file paths. It sends the files to `http://host.containers.internal:8000/audit`. It currently does not handle optional associations, persist a user-downloadable ZIP, or implement sensitivity tagging/approval.

## Known failure
The direct External Tool Server OpenAPI `/audit` call returned HTTP 422 because required multipart files were not passed from chat attachments. Do not confuse a successful `/health` tool call with successful file-upload integration.

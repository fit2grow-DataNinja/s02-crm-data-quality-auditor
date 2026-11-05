"""Regression coverage for the verified two-file Open WebUI adapter workflow."""
import io
import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

from integrations.openwebui.s02_csv_audit_adapter import Tools


class AdapterTests(unittest.TestCase):
    def test_two_file_upload_and_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            contacts = folder / "contacts.csv"
            deals = folder / "deals.csv"
            contacts.write_text("Record ID,Email\n1,a@example.com\n", encoding="utf-8")
            deals.write_text(
                "Record ID,Deal Name,Deal Stage,Amount,Deal owner\n"
                "2,Example,Qualified,100,Owner\n",
                encoding="utf-8",
            )
            attachments = [
                {"name": "contacts.csv", "file": {"path": str(contacts)}},
                {"name": "deals.csv", "file": {"path": str(deals)}},
            ]
            archive_buffer = io.BytesIO()
            with zipfile.ZipFile(archive_buffer, "w") as archive:
                archive.writestr(
                    "summary.json",
                    json.dumps({"contacts_checked": 1, "deals_checked": 1, "issues_total": 0}),
                )
                archive.writestr("report.md", "# Synthetic audit report\n")

            class FakeResponse:
                status = 200

                def __enter__(self):
                    return self

                def __exit__(self, *args):
                    return False

                def read(self):
                    return archive_buffer.getvalue()

            with patch(
                "integrations.openwebui.s02_csv_audit_adapter.urllib.request.urlopen",
                return_value=FakeResponse(),
            ) as mock_open:
                result = json.loads(Tools().run_s02_csv_audit(__files__=attachments))

            self.assertEqual(result["status"], "success")
            self.assertEqual(result["http_status"], 200)
            self.assertEqual(result["summary"]["issues_total"], 0)
            self.assertEqual(result["report"], "# Synthetic audit report\n")
            self.assertIn("summary.json", result["archive_files"])
            self.assertIn("report.md", result["archive_files"])
            request = mock_open.call_args.args[0]
            self.assertEqual(request.get_method(), "POST")
            self.assertEqual(
                request.full_url, "http://host.containers.internal:8000/audit"
            )
            self.assertIn("multipart/form-data; boundary=", request.get_header("Content-type"))
            self.assertIn(b'name="contacts"; filename="contacts.csv"', request.data)
            self.assertIn(b'name="deals"; filename="deals.csv"', request.data)
            self.assertIn(contacts.read_bytes(), request.data)
            self.assertIn(deals.read_bytes(), request.data)


if __name__ == "__main__":
    unittest.main()

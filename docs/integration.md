# Open WebUI integration

**Status:** Verified in the existing local setup with synthetic CSV exports. Fresh-environment reproducibility has not been verified. **Do not use real customer CRM data:** SEC-001 sensitivity classification and approval are not implemented.

## Prerequisites

- S02 repository checkout with API dependencies installed; see [local deployment](deployment.md).
- FastAPI running locally on port 8000. For the documented development setup, start it in a terminal:

  ```bash
  source .venv/bin/activate
  python -m uvicorn s02.api:app --host 127.0.0.1 --port 8000
  ```

- Open WebUI running in Podman with a configured chat model and network access to the host API.
- Synthetic files named exactly `contacts.csv` and `deals.csv`; optionally `associations.csv`. The adapter selects attachments by these names.

## Configure the Workspace Tool

1. In Open WebUI, open **Workspace → Tools** and create a tool.
2. Paste the source from [`integrations/openwebui/s02_csv_audit_adapter.py`](../integrations/openwebui/s02_csv_audit_adapter.py) and save.
3. In chat, enable that Workspace Tool under **+ → Integrations**.
4. Attach the synthetic CSV files; both required filenames must be present. An optional `associations.csv` is forwarded as a third input.

## Run a reviewer demonstration

Enter this **chat instruction** (not a terminal command):

> Run the S02 CRM audit on the attached CSV files. Summarize the deterministic findings by severity, explain the main issues, and identify checks that could not be fully evaluated. Do not infer additional findings.

Open **View Result from run_s02_csv_audit** and check that the tool response contains `status: success`, `http_status: 200`, a `summary` object and `report` text. Compare the AI explanation with the tool's counts and coverage information; the AI's prose is not independently validated.

**Recorded example:** A larger synthetic sample produced **202 contacts, 121 deals and 92 medium-severity missing-owner findings**. A separate user-reported live three-file demonstration returned **1 contact, 1 deal, 1 known association and 0 findings**. Your result depends on the files attached; do not expect these counts from arbitrary inputs. See [validation evidence](validation.md).

## Integration boundaries and troubleshooting

- The adapter relies on Open WebUI `__files__` metadata containing readable local file paths. It calls `http://host.containers.internal:8000/audit`; verify container-to-host connectivity if the request fails.
- The API returns a ZIP with `summary.json`, `issues.csv` and `report.md`. The Workspace Tool extracts the summary and report and returns them as text; it does **not** expose a downloadable ZIP in chat.
- Missing `contacts.csv` or `deals.csv` produces a tool error before upload. `associations.csv` is optional; partial association input does **not** justify inferring missing relationships.
- The direct External Tool Server OpenAPI `/audit` upload previously returned HTTP 422 because chat attachments were not forwarded as required multipart fields. A successful `/health` call does not verify that upload route. **Use the Workspace Tool described above.**
- The adapter has no sensitivity-tagging or approval gate. The project is a **synthetic-data-only portfolio MVP**, not a production service.

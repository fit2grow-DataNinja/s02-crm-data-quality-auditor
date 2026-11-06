# S02 validation record

Status: Verified synthetic-data integration milestones; evidence from reported local development runs, not independently rerun by this documentation update.

| Scenario | Result | Scope |
| --- | --- | --- |
| Standalone FastAPI audit | Passed | Synthetic CRM CSVs, ZIP output |
| Open WebUI attachment metadata | Passed | Two attachments with readable paths |
| Workspace Tool multipart upload | Passed | FastAPI HTTP 200 and ZIP response |
| Conversational audit explanation | Passed | Model described deterministic findings |
| Optional associations adapter regression | Passed | 2026-11-06: two-file and three-file mock HTTP tests passed (2/2); prior three-file test failed before implementation as expected |
| Full Python unittest suite | Passed | 2026-11-06: `python -m unittest discover -s tests -v` — 6 tests, 0.065s, OK (user-reported local run) |
| Live Open WebUI three-file upload | Pending | Automated tests mock the HTTP boundary; live Workspace Tool verification still needed |
| Direct OpenAPI `/audit` upload | Failed | HTTP 422 missing multipart files |
| SEC-001 enforcement | Not implemented | No customer-data clearance |

Observed synthetic results: **202 contacts**, **121 deals**, **92 medium findings**, all `CRM-DEAL-OWNER-MISSING`. ZIP report includes `summary.json`, `issues.csv`, `report.md`. Contact associations, close-date source reconciliation and freshness checks were not fully evaluated due to incomplete source data. Rules remain provisional pending CRM owner-policy review.

Test dependency note: `requirements-test.txt` already lists `httpx2`. The local environment lacked it during an earlier full-suite run; the user reinstalled it and then all six tests passed. Fresh-environment dependency installation and CI remain to be verified.

Next: verify a live synthetic three-file Open WebUI Workspace Tool upload, then evaluate additional negative cases and reproducible CI/container validation.

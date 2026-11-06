# S02 validation record

Status: Verified synthetic-data integration milestones; evidence from reported local development runs, not independently rerun by this documentation update.

| Scenario | Result | Scope |
| --- | --- | --- |
| Standalone FastAPI audit | Passed | Synthetic CRM CSVs, ZIP output |
| Open WebUI attachment metadata | Passed | Two attachments with readable paths |
| Workspace Tool multipart upload | Passed | FastAPI HTTP 200 and ZIP response |
| Conversational audit explanation | Passed | Model described deterministic findings |
| Optional associations adapter regression | Passed | 2026-11-06: two-file and three-file mock HTTP tests passed (2/2); prior three-file test failed before implementation as expected |
| Full Python unittest suite | Passed | 2026-11-06: `python -m unittest discover -s tests -v` — 11 tests, OK (latest user-reported local run after evaluated-check reporting fix; earlier runs also passed) |
| Live Open WebUI three-file upload | Passed (user-reported) | 2026-11-06: synthetic upload reported 1 contact, 1 deal, 1 known association, 0 findings, partial-reference-only coverage; no independent network trace |
| Direct OpenAPI `/audit` upload | Failed | HTTP 422 missing multipart files |
| SEC-001 enforcement | Not implemented | No customer-data clearance |

Observed synthetic results: **202 contacts**, **121 deals**, **92 medium findings**, all `CRM-DEAL-OWNER-MISSING`. ZIP report includes `summary.json`, `issues.csv`, `report.md`. Contact associations, close-date source reconciliation and freshness checks were not fully evaluated due to incomplete source data. Rules remain provisional pending CRM owner-policy review.

Test dependency note: `requirements-test.txt` already lists `httpx2`. The local environment lacked it during an earlier full-suite run; the user reinstalled it and then all six tests passed. Fresh-environment dependency installation and CI remain to be verified.

Missing-required-file adapter regression: 2026-11-06 user-reported full suite passed 9/9 after commit `2f163e6`; test verifies missing `deals.csv` yields an explicit error without an HTTP request, even when optional associations are attached.

## Final report coverage review (documentation sign-off, 2026-11-06)

Reviewed `s02/audit.py` output construction against the documented workflow (source inspection only; no new local run). `report.md` includes contact/deal counts, total findings, findings grouped by rule, explicit `Checks not fully evaluated` entries from `summary.coverage`, provisional-rule interpretation and recommended review. `summary.json` includes severity and rule counts, coverage flags and run time; `issues.csv` contains record-level findings.

**Remaining reporting limitation:** `report.md` lists rules with findings but does **not** enumerate every rule that was evaluated successfully. A zero-finding report therefore means no violations detected among implemented checks, **not** that every possible CRM quality check was performed. The coverage flags correctly identify absent association exports, partial association references, unavailable freshness timestamps and unavailable original close-date values. The report's phrase `No external AI was used` describes deterministic report generation, not the later Open WebUI AI explanation.

The earlier report limitation was addressed by explicit evaluated-check reporting, verified by the user-reported 11-test suite. The reviewed baseline report did not list all checks, but the updated report now does. CI/container portability, explanation-faithfulness testing and SEC-001 remain deferred or unverified as documented. CI/container portability, explanation-faithfulness testing and SEC-001 remain deferred or unverified as documented.

## Evaluated-check reporting enhancement — pending verification

Source commits `dc017c5` and `ab9617e` add an explicit `evaluated_checks` array to `summary.json`, a `Checks evaluated` section to `report.md`, and two targeted regression tests for reports with and without optional associations. This is a reporting-only change; existing CRM validation rules are unchanged. **Verified by user-reported local run, 2026-11-06:** `python -m unittest discover -s tests -v` returned `Ran 11 tests ... OK` after commit `bf13405` fixed missing rule-catalogue constants (the first 11-test run failed with `NameError: BASE_CHECKS is not defined`). The two new reporting tests are included. Variant 1 portfolio MVP acceptance is now closed; independent clean-environment/CI and model-explanation verification remain unperformed.

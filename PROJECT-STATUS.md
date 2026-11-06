# Project status — S02 CRM Data Quality & Freshness Auditor

**Last updated:** 2026-11-06  
**Phase:** Variant 1 portfolio MVP completion (synthetic-data-only); Variant 2 ChatGPT Skill comparison planned.  
**Status:** Active; **not production-ready**.

## Current working step
**Optional association CSV forwarding milestone complete**: automated regression and a live synthetic three-file Open WebUI audit are verified. The portfolio MVP acceptance checklist is now separated from production-readiness requirements in `docs/definition-of-done.md`.

### Next tiny action
**Run the current full regression suite after pulling the newly committed API negative-association test** (`tests/test_api.py`, commit `31782c5`); record the actual result before marking it passed. Continue one small verifiable action at a time.

### Last completed
- S02 FastAPI application, deterministic audit rules, CLI, dependency manifests, tests and synthetic CSV samples are source-controlled on `main` (commit `2d64691`).
- On 2026-11-05, all four automated tests passed using the project Python 3.11.5 environment.
- Standalone FastAPI `GET /health` returned HTTP 200; multipart `POST /audit` returned HTTP 200 with an audit ZIP.
- Open WebUI **Auditor Adapter** successfully processed synthetic contacts and deals CSVs and returned the expected summary and report.
- Verified synthetic result: **202 contacts**, **121 deals**, **92 medium findings**, all `CRM-DEAL-OWNER-MISSING`.
- The two-file Open WebUI adapter regression test passed locally (1 test, 2026-11-05); committed as `ff570a2`.
- Added `tests/fixtures/README.md` for reusable synthetic fixture policy and `docs/definition-of-done.md` for permanent milestone acceptance criteria.
- Test-first cycle verified: new three-file adapter test failed for the missing multipart field while two-file regression passed; adapter fixed in commit `468b04e`.
- On 2026-11-06, the focused adapter suite passed (2/2), and the full `python -m unittest discover -s tests -v` suite passed (6 tests in 0.065s) in the project's `.venv`.
- `requirements-test.txt` already declares `httpx2`; it was missing from the active environment until installed. Dependency declaration is not a guarantee that existing environments are provisioned; reproducible fresh-environment/CI verification remains pending.
- Live Open WebUI Workspace Tool audit with three synthetic files reported 1 contact, 1 deal, 1 known association, 0 findings, and partial-reference-only association coverage (user-provided response, 2026-11-06). The tool response did not separately expose raw multipart/ZIP evidence, so this is a successful end-to-end reported result, not an independent wire-level capture.
- Added an API-level negative-association regression test in commit `31782c5`; its execution is still pending user confirmation.
- Scope decision: complete a compact, synthetic-data-only Variant 1 portfolio MVP, then compare with a ChatGPT Skill-based Variant 2 using shared synthetic inputs and acceptance criteria. Full production/commercial backlog is explicitly deferred; see `docs/definition-of-done.md`.
- Approved architecture and audit rules remain unchanged.

## Implementation checkpoints
| Checkpoint | State | Evidence or next requirement |
| --- | --- | --- |
| Repository documentation and integration adapter | Complete | Available on `main` |
| FastAPI source, dependencies, tests and synthetic fixtures | Complete | Commit `2d64691` |
| Local standalone API and audit verification | Complete | 2026-11-05 health, multipart upload and ZIP checks |
| Open WebUI Workspace Tool conversational audit | Complete for two required CSVs | 2026-11-05 synthetic adapter verification |
| Optional association input in conversational adapter | **Complete for synthetic MVP** | 2 adapter tests and 6 total tests passed; live three-file Open WebUI audit reported expected results |
| Portfolio MVP scope and two-variant plan | Defined | Portfolio MVP acceptance distinct from production gate in definition of done |
| Full association and freshness audit coverage | Deferred beyond portfolio MVP | Complete source exports, timestamps and agreed rule criteria |
| SEC-001 sensitivity/manual approval enforcement | **Not implemented** | Design, approval, negative tests and fail-closed verification |
| Portable deployment and operational checks | Pending | Documented reproducible Podman validation |
| Customer/commercial validation | Pending | Separate from technical acceptance |

## Known limitations and boundaries
- The FastAPI endpoint accepts optional `associations` input and validates references present in the file; the Open WebUI adapter now forwards optional associations, and the live synthetic three-file workflow was verified by its reported results. A partial association reference file cannot establish which deals have no associations.
- Original close-date values and extract timestamps are unavailable for full reconciliation and freshness evaluation.
- Direct OpenAPI External Tool Server `/audit` upload previously failed HTTP 422 due to missing multipart attachments. **Do not confuse this with the verified Open WebUI Auditor Adapter.**
- Deterministic Python/SQL rules own findings; hosted AI may explain results, not invent them.
- **Synthetic data only.** SEC-001 is not implemented; no real customer CRM data or production-readiness claims.
- Preserve the approved modular FastAPI/Open WebUI/Podman architecture. Defer `ai-services-core` extraction until actual cross-service reuse is demonstrated.

## Resume instructions
1. Read this file and the [portfolio status](https://github.com/bb-DataNinja/ai-services-portfolio/blob/main/PROJECT-STATUS.md).
2. Continue from **Next tiny action**, one incremental, verifiable change at a time.
3. Update this service status after meaningful milestones; update portfolio status only for portfolio-level changes.

## Reference documents
- [Service specification](docs/service-specification.md)
- [Architecture](docs/architecture.md)
- [Integration](docs/integration.md)
- [Validation](docs/validation.md)
- [Definition of done](docs/definition-of-done.md)
- [Security](docs/security.md)
- [Deployment](docs/deployment.md)
- [Decisions](docs/decisions.md)

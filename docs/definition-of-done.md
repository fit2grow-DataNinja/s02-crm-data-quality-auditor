# S02 definition of done

This checklist applies to **each meaningful S02 feature, fix, or integration milestone**. It is a completion gate, not a claim that the overall service is production-ready.

## Required for every change
- [ ] Scope and expected behavior are clear, including what is explicitly out of scope.
- [ ] The change follows the approved architecture: deterministic audit findings remain in Python/FastAPI; AI explains results only.
- [ ] Relevant automated tests cover the new behavior and protect existing behavior against regression.
- [ ] Tests use synthetic data only; shared fixtures belong in `tests/fixtures/` only when justified by reuse.
- [ ] Relevant tests pass in the supported project environment; record the command and actual result. Never mark unexecuted tests as passed.
- [ ] Errors and missing/invalid inputs are tested where applicable; no unsupported audit claims are introduced.
- [ ] Documentation and S02 `PROJECT-STATUS.md` are updated for meaningful changes, with evidence and remaining limitations.
- [ ] No customer data is used. SEC-001 must be designed, implemented, and verified before any real CRM data or production claim.
- [ ] Portfolio status changes only when a portfolio-level milestone changes.

## Acceptance criteria: optional association CSV in Open WebUI adapter
- [ ] Existing contacts + deals workflow still works without an association attachment.
- [ ] With `associations.csv` attached, the adapter forwards it as the optional `associations` multipart field alongside contacts and deals.
- [ ] Missing required contacts or deals still produces a clear error; absence of optional associations does not.
- [ ] Automated adapter regression tests cover both two-file and three-file cases.
- [ ] Existing deterministic association-reference checks remain unchanged; a partial association export does **not** imply missing associations.
- [ ] Relevant automated tests pass and results are recorded; S02 status reflects the verified outcome.

## Test organization
- `tests/test_audit.py`: deterministic rule tests.
- `tests/test_api.py`: FastAPI endpoint tests.
- `tests/test_openwebui_adapter.py`: conversational adapter regression tests.
- `tests/fixtures/`: reusable synthetic fixtures **when needed**, not a mandatory duplicate of inline test data.
- `samples/`: larger synthetic demonstration datasets.

## Future improvement
Add a GitHub Actions test workflow after dependencies and test execution are reproducible in CI. Until then, test execution is a documented manual verification step.

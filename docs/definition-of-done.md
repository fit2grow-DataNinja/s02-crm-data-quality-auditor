# S02 definition of done

This checklist applies to **each meaningful S02 feature, fix, or integration milestone**. It is a completion gate, not a claim that the overall service is production-ready.

## Delivery levels: portfolio MVP versus production readiness

**Current target: Variant 1 portfolio MVP, synthetic data only.** Its purpose is to demonstrate sound solution design, deterministic CRM audit logic, FastAPI integration, Open WebUI AI-assisted explanation, regression testing, honest limitations, and a reproducible demonstration. It is **not** a customer deployment or production-readiness claim.

### Variant 1 portfolio MVP acceptance — evidence review (2026-11-06)
- [x] Existing and newly added core business-rule tests pass, including invalid association references and representative duplicate/owner cases where implemented. **Evidence:** user-reported nine-test suite in [validation](validation.md).
- [x] Required-file, invalid-schema and relevant failure paths are verified; no unsupported inference from partial association exports. **Evidence:** regression suite and source review; not exhaustive input fuzzing.
- [x] Audit output clearly states evaluated checks and unavailable freshness/close-date checks. **Evidence:** `summary.json` includes `evaluated_checks`, `report.md` lists evaluated checks, and two targeted regression tests passed in the user-reported 11-test suite. See [validation](validation.md).
- [x] One complete synthetic Open WebUI demonstration is recorded with deterministic findings and AI explanation kept separate. **Evidence:** user-reported three-file run; no independent network trace or model-faithfulness evaluation.
- [x] Synthetic-only security boundary and unimplemented SEC-001 are prominent.
- [x] A portfolio [Variant 1 case study](https://github.com/fit2grow-DataNinja/ai-services-portfolio/blob/main/case-studies/S02-crm-data-quality-auditor.md) explains the problem, architecture, results, tests, trade-offs and limitations.
- [x] Evidence, test commands and outstanding issues are recorded before declaring the portfolio MVP complete.

**Variant 1 portfolio MVP acceptance: complete (7/7 criteria), 2026-11-06.** Documentation is finalized. Checked items reflect documented/user-reported local test and demonstration evidence, not an independently reproduced clean-environment run. Neither status confers customer-data or production clearance.

### Production readiness (separate, deferred gate)
Customer-data processing requires implemented and tested SEC-001 sensitivity classification, manual approval and fail-closed controls, plus appropriate operational security, deployment reliability, monitoring, performance, comprehensive business-rule/source-data validation and acceptance evidence. **Do not treat portfolio MVP acceptance as production clearance.** The detailed, intentionally deferred work inventory and its evidence expectations are maintained in the [commercial readiness backlog](commercial-readiness-backlog.md); this checklist remains the authority for MVP acceptance.

### Variant 2: ChatGPT Skill comparison (after Variant 1)
Develop a reusable skill-based workflow for the same synthetic CRM audit scenario and compare both variants using shared datasets and criteria: finding accuracy, repeatability, explainability, setup/maintenance effort and security boundaries. Prefer executable deterministic checks where the skill environment supports them; do not claim instructions alone guarantee deterministic results.

### Deferred from Variant 1 MVP
Comprehensive freshness and close-date reconciliation, extensive stage-specific business rules, GitHub CI, load testing, hardened production deployment, commercial pilot preparation and premature shared-core extraction are optional later backlog items, not portfolio MVP blockers.

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

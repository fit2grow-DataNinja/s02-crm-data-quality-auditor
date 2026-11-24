# Project status — S02 Variant 1

**Last updated:** 2026-11-24  
**Stage:** Synthetic-data portfolio MVP complete and accepted.  
**Status:** Closed for the defined MVP scope; **not production-ready**.

## Completed scope

Variant 1 delivers a deterministic, read-only Python/FastAPI CRM CSV auditor with an Open WebUI Workspace Tool integration. It was accepted against all seven documented portfolio MVP criteria.

The shared synthetic scenario recorded **202 contacts, 121 deals, and 92 medium-severity missing-owner findings**. These are review flags under a provisional policy rule, not confirmed business errors.

## Validation

The project includes an 11-test regression suite and documented standalone API and Open WebUI demonstration scenarios. The detailed [validation record](docs/validation.md) preserves the commands, outcomes, evidence boundaries, and limitations.

## Governance assessments

Two bounded retrospective analyses are complete for the documented synthetic MVP scope:

- **EU AI Act:** preliminary screening accepted by the portfolio owner. The project-specific [overview](docs/eu-ai-act-evaluation-overview-status.md), [screening record](docs/eu-ai-act-project-screening-record.md), and [retrospective assessment](docs/eu-ai-act-retrospective-assessment.md) preserve the results and limits.
- **NIST AI RMF:** all 72 Core subcategories have a disposition. The [business-facing overview](docs/nist-ai-rmf-evaluation-overview-status.md) and [structured project assessment record](docs/nist-ai-rmf-project-assessment-record.md) were accepted by the portfolio owner. The detailed [retrospective assessment](docs/nist-ai-rmf-retrospective-assessment.md) contains the row-level rationale and remains marked draft for review.

No company representatives participated. NIST Target Profile entries are proposed portfolio targets, not organizational goals. These assessments do not change the closed MVP scope or authorize real-data or production use.

## Scope and limitations

- Synthetic data only. **Do not upload real or sensitive customer CRM data.**
- SEC-001 sensitivity tagging and manual approval are not implemented.
- The missing-owner rule is provisional and requires business-policy confirmation.
- Partial association exports cannot establish that all relationships are present.
- Comprehensive freshness and original close-date reconciliation require source data not available in the current exports.
- AI explanation faithfulness is not independently verified.
- GitHub CI, production hardening, and commercial validation are outside the closed MVP scope.

## Documentation

- [Service specification](docs/service-specification.md)
- [Architecture](docs/architecture.md)
- [Open WebUI integration](docs/integration.md)
- [Validation record](docs/validation.md)
- [Security status](docs/security.md)
- [Definition of done](docs/definition-of-done.md)
- [Commercial-readiness backlog](docs/commercial-readiness-backlog.md)
- [Portfolio S02 comparison](https://github.com/fit2grow-DataNinja/ai-services-portfolio/blob/main/case-studies/S02-crm-data-quality-auditor.md)
- [Variant 2 — ChatGPT Skill/Python](https://github.com/fit2grow-DataNinja/s02-crm-data-quality-auditor-skill)

S02 implementation changes are closed at the synthetic portfolio MVP level. The portfolio repositories preserve the comparison and evidence; this status file records Variant 1's current state.

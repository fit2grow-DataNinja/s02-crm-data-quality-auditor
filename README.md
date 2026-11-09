# S02 — CRM Data Quality & Freshness Auditor

A completed **synthetic-data portfolio MVP** demonstrating deterministic CRM data checks with AI-assisted explanation through a Python/FastAPI service and Open WebUI.

This repository contains the Variant 1 implementation. The portfolio-level use case compares it with a separate ChatGPT Skill implementation.

## Business problem

CRM data issues can reduce confidence in pipeline reporting and create manual review work. S02 explores how to identify specific, reviewable findings in CRM CSV exports and explain them in business language, while keeping audit decisions in deterministic code.

## Solution

The service accepts synthetic contacts and deals CSV files, with an optional associations file. Python rules produce structured findings and report artifacts. The Open WebUI Workspace Tool sends the files to the API and provides the resulting report content to the conversational model for explanation.

**Python determines the audit findings; the AI explains the supplied results.** The workflow does not edit CRM records. The separation of audit computation and explanation does not guarantee that every model explanation will be faithful; automated explanation verification is not implemented.

## Demonstrated capabilities

- Deterministic validation of selected contact, deal, and association fields.
- Standalone FastAPI audit endpoint with structured output.
- Open WebUI Workspace Tool integration for conversational use.
- Coverage reporting that identifies checks not fully evaluated.
- Automated regression tests for audit rules, API behavior, and adapter behavior.

The shared synthetic scenario recorded **202 contacts, 121 deals, and 92 medium-severity missing-owner findings**. These are review flags under a provisional policy rule, not confirmed business errors.

## Validation

The project includes an 11-test regression suite and documented API and Open WebUI demonstration scenarios. See the [validation record](docs/validation.md) for details.

## Scope and limitations

- Synthetic data only. **Do not upload real or sensitive customer CRM data.**
- SEC-001 sensitivity tagging and manual approval are **not implemented**.
- The missing-owner rule is provisional and requires business-policy confirmation.
- Partial association exports cannot establish that all relationships are present.
- Comprehensive freshness and original close-date reconciliation require source data not available in the current exports.
- AI explanation faithfulness is not independently verified.
- This MVP is not production-ready, commercially validated, or evidence of GDPR compliance or tenant isolation.

See [security status](docs/security.md) for the current data-handling boundary.

## Repository navigation

- [Service specification](docs/service-specification.md)
- [Architecture and integration boundaries](docs/architecture.md)
- [Open WebUI walkthrough](docs/integration.md)
- [Local deployment](docs/deployment.md)
- [Validation evidence](docs/validation.md)
- [Security status](docs/security.md)
- [Decisions](docs/decisions.md)
- [Commercial-readiness backlog](docs/commercial-readiness-backlog.md)
- [Open WebUI Workspace Tool source](integrations/openwebui/s02_csv_audit_adapter.py)

## Related portfolio materials

- [S02 portfolio use case and two-variant comparison](https://github.com/fit2grow-DataNinja/ai-services-portfolio/blob/main/case-studies/S02-crm-data-quality-auditor.md)
- [S02 portfolio service overview](https://github.com/fit2grow-DataNinja/ai-services-portfolio/blob/main/services/S02.md)
- [Variant 2 — ChatGPT Skill and Python](https://github.com/fit2grow-DataNinja/s02-crm-data-quality-auditor-skill)
- [Portfolio repository](https://github.com/fit2grow-DataNinja/ai-services-portfolio)

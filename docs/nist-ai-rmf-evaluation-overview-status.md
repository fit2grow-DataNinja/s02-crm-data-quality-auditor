# Business-facing NIST AI RMF evaluation overview and status — S02 Variant 1

**Record ID:** S02-NIST-OVERVIEW-V1-2026-11-24  
**Document status:** Draft for portfolio-owner review  
**Assessment status:** Retrospective portfolio assessment; bounded scope  
**Assessment date:** 24 November 2026  
**Assessed system:** S02 CRM Data Quality & Freshness Auditor — Variant 1  
**Audience:** Managers, decision-makers, reviewers, and portfolio visitors  
**Detailed assessment and evidence source:** [NIST AI RMF retrospective assessment — S02 Variant 1](nist-ai-rmf-retrospective-assessment.md)  
**Framework baseline:** NIST AI RMF 1.0 (NIST AI 100-1, 2023); NIST AI 600-1 used as partial input for the generative explanation component

> This is a business-facing summary of a self-directed portfolio assessment using a voluntary NIST framework. It is not a NIST determination, legal assessment, maturity rating, certification, independent audit, compliance conclusion, or approval to deploy. The linked retrospective contains the full outcome analysis, evidence limitations, and source traceability. The structured project assessment record is linked from that retrospective.

## 1. Executive decision panel

| Question | Current answer |
|---|---|
| What is S02 Variant 1? | A portfolio MVP that applies deterministic Python rules to synthetic CRM exports and uses a hosted generative model to explain report content. |
| What stage is assessed? | A completed synthetic-data demonstration. The project is not production-ready and is not approved for customer use or real/sensitive CRM data. |
| What does the NIST assessment cover? | A retrospective application of NIST AI RMF 1.0 to the Variant 1 MVP as documented. It does not assess an organization or the hosted provider’s controls. |
| What is the main design boundary? | Python determines findings; the model explains report content. AI explanations are not independently verified and must not be treated as confirmed findings. |
| What is the assessment result? | All 72 Core subcategories have a recorded disposition: 6 Main focus points, 8 Sub-focus points, 41 not selected for this MVP stage with rationale, and 17 unable to assess because relevant evidence was unavailable. |
| What is the current portfolio decision? | Retain Variant 1 as a synthetic-data portfolio demonstration only. Any expansion requires a separate, context-specific assessment with suitable evidence and accountable organizational input. |
| Is an organizational target or risk acceptance recorded? | No. Target Profile entries are proposed portfolio targets, not company-agreed goals or accepted organizational risks. |

## 2. System and use at a glance

| Item | Documented assessment context |
|---|---|
| Purpose | Demonstrate selected CRM data-quality checks and AI-assisted explanations while keeping finding generation deterministic. |
| Inputs | Synthetic contact, deal, and optional association CSV exports. |
| Processing | Python rules produce structured findings and report artifacts. A FastAPI service and Open WebUI Workspace Tool connect the report to a configured hosted model for explanation. |
| Outputs | Review flags and explanatory text. In a documented synthetic run, 202 contacts and 121 deals produced 92 medium-severity missing-owner review flags under a provisional rule; these are not confirmed errors. |
| Human role | Service is read-only. Documentation expects users to review output, but a formal approval/override workflow is not implemented or evaluated. |
| Data boundary | Synthetic data only. Real or sensitive customer CRM data is not approved for this configuration. |
| Verification state | The repository reports 11 passing regression tests from a user-run local test; the assessment did not rerun them. Explanation fidelity has not been independently evaluated. |
| Key limitations | No production/customer deployment, real-data privacy/provider review, production security evidence, formal human review/override, operational monitoring, or incident-feedback evidence. |

## 3. How to read the NIST result

NIST AI RMF 1.0 is a voluntary risk-management framework. It provides outcomes and actions to guide context-specific risk management; it does not prescribe one universal checklist or assign this project a compliance score. The selection tiers and disposition labels below are repository-created tools for transparent portfolio analysis, not NIST ratings.

- **Main focus points** are outcomes most central to this MVP’s purpose, system boundary, explanation risks, and proceed decision.
- **Sub-focus points** support or qualify the main points.
- **Not selected for current MVP** means the outcome was reviewed and not selected for the current stage, with rationale and a revisit trigger. It does not mean the related risk is absent.
- **Unable to assess** means relevant evidence was unavailable; it is an evidence gap, not a negative finding.
- **Target Profile** means proposed desired portfolio state in this self-directed assessment. No company representatives developed or approved it.

## 4. Assessment focus and disposition

| Focus / disposition | Count | Interpretation |
|---|---:|---|
| Main focus points | 6 | Core outcomes emphasized in the current MVP assessment. |
| Sub-focus points | 8 | Supporting outcomes assessed alongside the main focus. |
| Not selected for this MVP stage, with rationale | 41 | Reviewed and individually dispositioned; revisit if scope expands. |
| Unable to assess because evidence was unavailable | 17 | Individual information gaps are documented; do not infer risk or control absence. |
| **Total Core subcategories dispositioned** | **72** | Full row-level coverage is in the retrospective assessment. |

**Main focus areas:** intended purpose and scope; separation of deterministic findings from AI explanations; known limits and human use of output; synthetic-only/read-only boundary; explanation validation; and the bounded proceed decision.

**Sub-focus areas:** explicit MVP requirements; evaluation and data integrity; hosted-model data boundary; metrics and unmeasured risks; test sets; validity and reliability; basic security/resilience boundary; and synthetic-only data flow.

NIST AI RMF Generative AI Profile (NIST AI 600-1) was used as **partial input** for the hosted model explanation component. It was not treated as a profile for the whole CRM workflow or as a source of automatic project targets. No relevant published NIST profile for the full bounded CRM scenario was identified in the dated search.

## 5. Key findings and evidence limits

| Finding | Current evidence / limitation |
|---|---|
| Deterministic audit logic is distinct from AI explanation | Project documents and architecture describe Python as determining findings and the hosted model as explaining supplied report content. This is repository-authored evidence, not independent assurance. |
| Synthetic MVP demonstration exists | A reported run covered 202 contacts and 121 deals and generated 92 provisional review flags. The flags are not confirmed errors and do not demonstrate real CRM performance. |
| Test evidence is bounded | The project records 11 passing regression tests from a user-reported local run. They were not independently rerun; no clean-environment/CI verification is claimed here. |
| Explanation quality remains unverified | No independent evaluation establishes that generated explanations are faithful, complete, or free of unsupported statements. |
| Data/security gate is incomplete | SEC-001 sensitivity tagging, fail-closed handling, and manual approval are planned but not implemented or tested. |
| Organizational operation is outside scope | No company representatives, organizational risk owner, production deployment, real-data privacy review, or operational monitoring evidence is part of this assessment. |

## 6. Priority actions and decision gates

These are portfolio follow-up actions and gates for any future use. They are not NIST-mandated tasks or company-approved remediation items.

| Priority | Action / question | Why it matters | Owner / timing |
|---|---|---|---|
| Maintain current boundary | Keep the synthetic-only, read-only restriction prominent; do not use real or sensitive CRM data in this configuration. | SEC-001 is not implemented or tested; current evidence supports only a bounded demonstration. | Portfolio owner; ongoing. |
| Evaluate explanations | Compare generated explanations against deterministic findings, including unsupported claims and omitted coverage caveats. | Explanation faithfulness is not independently evaluated. | Portfolio owner; before relying on explanations beyond the demonstration. |
| Implement data gate before real-data consideration | Define and test sensitivity tagging, fail-closed handling, and manual approval. | The planned gate is absent. | Portfolio owner; prerequisite before considering any real-data path. |
| Review provider and data handling | Identify exact model/provider and review processing, retention, access, security, and version changes. | Current configuration and hosted-service terms are not established. | Portfolio owner and relevant provider; before organizational use. |
| Define operational human review | If an organization adopts the system, define responsible roles, review/override, incident, and feedback processes. | No organization or operational process was assessed. | Prospective deploying organization; before any pilot or production use. |

## 7. Decision and reassessment triggers

**Bounded portfolio decision:** retain Variant 1 as a synthetic-data portfolio demonstration only. Do not use real or sensitive CRM data, deploy for customers or in production, write back to CRM, or rely on AI explanations as verified audit findings or as the sole basis for business action.

Reassess if purpose, data, model/provider, integration, user group, system capability, deployment setting, or lifecycle stage changes; if real data, customer use, or production is proposed; if new impact or test evidence appears; or if NIST revises the framework/profile sources used. Any organizational assessment should include the relevant company representatives and an accountable decision-maker. The Target Profile should then be developed with them using the Current Profile as context.

## 8. Evidence, review limits, and source traceability

The overview derives from the [NIST AI RMF retrospective assessment](nist-ai-rmf-retrospective-assessment.md), which contains the full 72-outcome disposition, row-level reasoning, evidence register, actions, and limitations. The retrospective links to the [structured NIST project assessment record](nist-ai-rmf-project-assessment-record.md). This overview does not link directly to the record; use the retrospective as the detailed assessment route.

Evidence includes S02 README/project status, architecture and security documentation, the validation record, portfolio case study, NIST AI RMF 1.0, and NIST AI 600-1. Project-authored and user-reported evidence is labeled as such; no independent audit, company review, or control-effectiveness verification is claimed.

## Use limitation

This overview is a business-facing summary of a bounded, retrospective portfolio assessment. It does not establish organizational risk acceptance, a company-agreed Target Profile, legal compliance, certification, model reliability, control effectiveness, privacy/security readiness, or production readiness.

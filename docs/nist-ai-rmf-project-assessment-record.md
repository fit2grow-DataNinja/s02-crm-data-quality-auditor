# NIST AI RMF project assessment record — S02 Variant 1

**Record ID:** S02-NIST-RECORD-V1-2026-11-24  
**Status:** Completed for the bounded portfolio assessment; draft for owner review  
**Assessment date:** 24 November 2026  
**Record owner:** Portfolio author  
**Contributors / company representatives:** None; self-directed portfolio project  
**Assessment type:** Retrospective application of a voluntary framework  
**Framework baseline:** NIST AI RMF 1.0, NIST AI 100-1 (2023)  
**Application matrix:** [NIST AI RMF application matrix draft](https://github.com/fit2grow-DataNinja/ai-governance-frameworks/blob/main/working-documents/nist-ai-rmf-application-matrix-draft.md), reviewed 24 November 2026  
**Source status checked:** 24 November 2026; NIST reports that AI RMF revision is in progress. Recheck the official source baseline before a future reassessment.  
**Related project:** [S02 CRM Data Quality Auditor — Variant 1](https://github.com/fit2grow-DataNinja/s02-crm-data-quality-auditor)  
**Detailed outcome assessment:** [NIST AI RMF retrospective assessment — S02 Variant 1](nist-ai-rmf-retrospective-assessment.md)  
**Business-facing summary:** [NIST AI RMF evaluation overview and status — S02 Variant 1](nist-ai-rmf-evaluation-overview-status.md)

> This repository-created record applies a voluntary risk-management framework to a bounded portfolio MVP. It is not NIST-issued, a legal assessment, a maturity rating, certification, compliance determination, organizational risk acceptance, or proof that controls operate effectively.

## 1. Record control

| Field | Entry |
|---|---|
| Assessment record ID | S02-NIST-RECORD-V1-2026-11-24 |
| Project / system name | S02 CRM Data Quality & Freshness Auditor — Variant 1 |
| Record owner | Portfolio author |
| Contributors / reviewers | No company representatives or independent reviewers recorded. Portfolio-owner review is pending. |
| Assessment date and status | 24 November 2026; completed for the stated scope, draft for owner review |
| Related solution repository or project record | This S02 repository; detailed retrospective linked above |
| Matrix version / commit / date | Draft application matrix reviewed 24 November 2026; the matrix is a living working document |
| Framework source version | NIST AI RMF 1.0, NIST AI 100-1 (2023); NIST AI 600-1 used as partial input for generative AI |
| Source baseline rechecked on | 24 November 2026 |
| Assessment type | Retrospective |
| Prior assessment / change reference | Initial S02 Variant 1 NIST retrospective assessment; no prior NIST assessment record |

## 2. System and use context

| Prompt | Record |
|---|---|
| What system is assessed? | Variant 1 of a self-directed CRM data-quality portfolio MVP: deterministic Python/FastAPI audit service, Open WebUI Workspace Tool adapter, and a configured hosted generative model that explains report content. |
| Business or public-interest need | Demonstrate selected CRM export data-quality checks and communicate review findings, while keeping finding generation deterministic and AI explanation separate. |
| Intended purpose, users, and expected actions | Portfolio demonstration using synthetic CRM exports. The tool flags selected records for user review; it does not rank people, select applicants, make an automated business decision, or update CRM. |
| Uses outside scope / prohibited in this configuration | Real or sensitive customer data; customer or production deployment; CRM write-back; treating model explanations as verified findings or as the sole basis for business action. |
| AI methods/components | Deterministic Python validation rules; FastAPI interface; Open WebUI adapter/orchestration; hosted generative model for natural-language explanation. The demo materials mention GPT-4.1-mini, but do not establish a fixed deployed model version or configuration. |
| System boundary and dependencies | The assessed path includes the local audit service, adapter/chat interface, report content, and hosted model. Provider configuration, supplier terms, and hosted-service data handling are not established. |
| Lifecycle stage | Completed portfolio MVP and synthetic demonstration only; no organizational deployment, production operation, or post-deployment lifecycle is assessed. |
| Geography, sector, organization, environment | No deploying organization or actual deployment geography is established. The framework application is a portfolio exercise; the scenario is CRM data quality, not a company-specific sector assessment. |
| Affected parties, benefits, and harms | No real people or customer organizations are represented in the synthetic scenario. In hypothetical use, users may benefit from reviewable findings; customers, employees, or sales teams could be indirectly affected if inaccurate findings or explanations influence reporting or action. No real-world impact study exists. |
| Human roles and oversight | The service is read-only and documentation expects user review. A formal approval/override workflow is not implemented or evaluated; explanation faithfulness has not been independently verified. |
| Assumptions and uncertainties | Synthetic status is based on project documentation and was not independently verified sample-by-sample. The missing-owner rule is provisional. Reported tests were not rerun for this assessment. |
| Non-AI alternatives | A deterministic-only explanation/report workflow could be considered in a future comparison; comparative user value is outside this retrospective’s scope. |

## 3. Profile search, selection, and tailoring

Official NIST AI RMF/AIRC sources and profile materials were checked on 24 November 2026. Profile search is a repository-proposed method; NIST does not prescribe this sequence or this record format.

| Candidate profile / source | Publisher and status | Scope and fit | Decision and rationale |
|---|---|---|---|
| [NIST AI RMF Generative AI Profile, NIST AI 600-1 (2024)](https://doi.org/10.6028/NIST.AI.600-1) | NIST; published | Relevant to risks in the hosted model’s generated explanations, but not the entire deterministic CRM audit workflow or its organizational context. | **Use as partial input.** Apply relevant risk ideas to the explanation component only; it does not automatically define S02’s outcome selection or targets. |
| NIST concept note for a Trustworthy AI in Critical Infrastructure profile | NIST concept note, not a finalized profile | S02 has no critical-infrastructure context in its documented scope. | **Not used.** Context mismatch and concept-note status. |
| Other official NIST profiles | Official sources checked on the search date | No other published NIST profile relevant to this bounded CRM export-audit scenario was identified. | **No additional profile reused.** This is a dated, bounded search; repeat if the context changes. |
| Non-NIST profile pointers listed by NIST | External sources, not NIST-issued profiles | No external profile was needed to define this portfolio scenario. | **Not used.** Do not label external profiles as NIST profiles. |

**Profile search conclusion:** A NIST profile is used as partial input; project-specific tailoring is based on the AI RMF 1.0 Core. The profile does not set the project’s Target Profile.

### 3.1 Assessment scope and tailoring rationale

| Tailoring factor | Assessment notes |
|---|---|
| User and organizational requirements | Portfolio project requirements and boundaries are documented. No organization or company requirements were assessed. |
| Context-specific laws, norms, and expectations | This record is not a legal assessment. EU AI Act screening is maintained separately in the linked EU AI Act project documents. |
| Organizational risk tolerance / decision basis | No organization risk tolerance or risk owner exists in scope. The portfolio owner’s bounded decision is to retain the MVP for synthetic demonstration only. |
| Capabilities, expertise, time, and resources | No organizational capacity assessment was performed. |
| System capability and knowledge limits | Deterministic findings are limited to selected checks; the missing-owner rule is provisional; model explanation fidelity and production performance are unverified. |
| Affected parties and perspectives | No affected-party consultation occurred; there is no real deployment or affected population in scope. |
| Framework outcomes selected | 14 outcomes selected and separated into 6 Main focus points and 8 Sub-focus points. The remaining 58 outcomes are individually dispositioned in the detailed retrospective. |
| Current Profile | Describes documented S02 project state and available evidence, not verified organizational operation. See detailed assessment §§4.1–4.2. |
| Target Profile | Proposed portfolio targets only. No company representatives or organizational risk owner participated; targets are not company-agreed or approved. |
| Representatives consulted | None; self-directed portfolio project. |
| Target decision owner and approval | Portfolio owner proposed targets for the MVP; no organizational approval or risk acceptance recorded. Owner review of this record is pending. |
| Outcomes not selected / unable to assess | 41 were not selected for the MVP stage with rationale; 17 could not be assessed because relevant evidence was unavailable. Full reference-by-reference rationale and revisit triggers are in detailed retrospective §5. |

NIST describes Profiles as context-specific selections and tailoring of Core outcomes, and Current/Target Profiles as existing and desired states. The Target Profile here remains a proposal for the portfolio MVP; the company-representative collaboration fields in the reusable template are not applicable to this self-directed project. If a company assessment is later performed, relevant representatives should develop the desired state using the Current Profile as context.

## 4. Summary and decisions

| Item | Record |
|---|---|
| Main findings about documented current state | Python determines audit findings; a hosted model explains supplied report content. The service is synthetic-only and read-only. A synthetic run reported 202 contacts, 121 deals, and 92 medium-severity missing-owner review flags under a provisional rule; these are not confirmed errors. |
| Material risks, benefits, and uncertainties | The split between deterministic findings and AI explanations is a useful boundary. Remaining concerns include unsupported or misleading explanations, incomplete audit coverage, real-data exposure if the boundary changes, and uncertain provider/model configuration. |
| Important evidence reviewed | Project README/status, architecture/security, validation record, portfolio case study, and NIST AI RMF Generative AI Profile. Evidence register E-01 to E-06 is in the detailed retrospective. |
| Significant evidence gaps | No independent test rerun; no independent explanation-fidelity evaluation; no implemented SEC-001 sensitivity/fail-closed/manual-approval gate; no real-data privacy/provider review, production security review, formal human override, or operational monitoring evidence. |
| Current decision / recommendation | Retain Variant 1 as a synthetic-data portfolio demonstration only. Do not use real or sensitive CRM data, deploy for customers or in production, write back to CRM, or treat AI explanations as verified findings or as the sole basis for action. |
| Decision-maker and date | Portfolio owner; documented 24 November 2026. This is not a company decision. |
| Conditions, dependencies, or review triggers | Any scope expansion requires a separate review with context-appropriate evidence and accountable organizational input. See §9. |
| What this assessment does not establish | Company Current/Target Profiles, organizational control effectiveness, legal compliance, security/privacy/fairness, model reliability, or production readiness. |

## 5. Core outcome review and focus hierarchy

The detailed retrospective is the controlling, row-level outcome analysis for this record. It includes the full 72-subcategory coverage table, the evidence and Current/Target Profile details for all selected outcomes, and individual dispositions with rationales and triggers for all remaining outcomes. This cross-reference is intentional to avoid maintaining two conflicting copies of the same 72-row analysis.

- **Main focus points (6):** MAP 1.1; MAP 2.1; MAP 2.2; MAP 3.3; MEASURE 2.9; MANAGE 1.1.
- **Sub-focus points (8):** MAP 1.6; MAP 2.3; MAP 4.2; MEASURE 1.1; MEASURE 2.1; MEASURE 2.5; MEASURE 2.7; MEASURE 2.10.
- **Not selected for this MVP stage with rationale (41):** individual references and reasons are listed in [§5 of the detailed retrospective](nist-ai-rmf-retrospective-assessment.md#5-remaining-core-outcomes-and-dispositions).
- **Unable to assess because relevant evidence was unavailable (17):** individual references and reasons are listed in the same detailed retrospective section.
- **Coverage check:** Main focus 6; Sub-focus 8; Not selected 41; Unable to assess 17; **Total reviewed: 72**. Each Core subcategory has exactly one disposition in the detailed retrospective.

The focus tiers are repository-created and indicate relative emphasis for this MVP, not NIST categories, risk ratings, maturity levels, or achievement scores. “Not selected” does not mean the associated risk is absent. “Unable to assess” records an evidence gap, not a negative finding.

### Selected outcome focus summary

| Focus tier | NIST reference | Context-specific focus |
|---|---|---|
| Main | MAP 1.1 | Scope, intended purpose, workflow, and boundaries |
| Main | MAP 2.1 | Deterministic audit and AI explanation roles |
| Main | MAP 2.2 | Known limits and human use of output |
| Main | MAP 3.3 | Synthetic-only, read-only scope |
| Main | MEASURE 2.9 | Explanation validation |
| Main | MANAGE 1.1 | Bounded proceed decision |
| Sub | MAP 1.6 | Explicit MVP requirements |
| Sub | MAP 2.3 | Evaluation and data integrity |
| Sub | MAP 4.2 | Third-party/model data boundary |
| Sub | MEASURE 1.1 | Metrics and unmeasured risks |
| Sub | MEASURE 2.1 | Test sets and evaluation tools |
| Sub | MEASURE 2.5 | Validity and reliability |
| Sub | MEASURE 2.7 | Basic security and resilience boundary |
| Sub | MEASURE 2.10 | Synthetic-only data boundary and hosted-model flow |

For the Current Profile, Target Profile, evidence IDs/limits, gaps, actions, owners, and project decisions for each selected outcome, see [§§4.1–4.2 of the detailed retrospective](nist-ai-rmf-retrospective-assessment.md#4-selected-outcomes). No selected outcome is asserted to be achieved merely because a target is proposed.

## 6. Voluntary Playbook suggestions

No NIST AI RMF Playbook suggestion is recorded as an adopted requirement or mandatory step for this MVP. The outcome assessment is grounded in the Core and uses NIST AI 600-1 as partial input for the generative explanation component. Playbook ideas may be considered later as voluntary suggestions, with their source and project-specific adoption decision recorded separately.

## 7. Evidence register

| Evidence ID | Artifact / observation | What it supports | Limitations / verification |
|---|---|---|---|
| E-01 | [README](../README.md) and [PROJECT-STATUS.md](../PROJECT-STATUS.md) | Purpose, synthetic-only restriction, provisional rule, limitations, and MVP status. | Project-authored statements; not independent assurance. |
| E-02 | [Architecture](architecture.md) and [security status](security.md) | Data flow, hosted-model boundary, read-only path, and SEC-001 status. | No independent security test, privacy review, or vendor assessment. |
| E-03 | [Validation record](validation.md) | Reported synthetic outcomes and test evidence. | User-reported local run; not rerun for this assessment; no CI or clean-environment verification. |
| E-04 | [S02 portfolio case study](https://github.com/fit2grow-DataNinja/ai-services-portfolio/blob/main/case-studies/S02-crm-data-quality-auditor.md) | Cross-project scenario and enforced versus behavioral boundaries. | Portfolio-authored synthesis; not independent model-fidelity evidence. |
| E-05 | [NIST AI RMF Generative AI Profile, NIST AI 600-1](https://doi.org/10.6028/NIST.AI.600-1) | Partial risk input for the generative explanation component. | Voluntary profile input; not a full system assessment or compliance standard. |
| E-06 | [NIST AI RMF source page](https://www.nist.gov/itl/ai-risk-management-framework) and [NIST Profiles](https://airc.nist.gov/airmf-resources/airmf/6-sec-profile/) | Framework/profile search and source status checked 24 November 2026. | Search is time-bounded; recheck before future application. |

## 8. Actions, decisions, and monitoring

These are portfolio actions and future-use gates, not company-approved actions or NIST-mandated tasks.

| ID | Risk / gap / improvement | Response and rationale | Owner / timing | Status and completion evidence |
|---|---|---|---|---|
| A-01 | Maintain synthetic-only boundary | Keep the restriction prominent; no real CRM data in this configuration. | Portfolio owner; ongoing | Documented; keep user-facing setup and repository instructions aligned. |
| A-02 | SEC-001 data gate absent | Implement sensitivity tagging, fail-closed handling, and manual approval before any real-data path is considered. | Portfolio owner; before real-data consideration | Planned, not implemented. Completion evidence: reviewed design, security tests, and enforcement evidence. |
| A-03 | Explanation fidelity unverified | Evaluate model explanations against deterministic findings, including unsupported claims and preservation of coverage caveats. | Portfolio owner; before relying on explanations beyond demonstration | Not implemented. Completion evidence: reproducible evaluation set, criteria, results, and failure handling. |
| A-04 | Hosted-model handling unassessed | Review provider configuration, data processing, retention, access, security, and version changes. | Portfolio owner and provider; before organizational use | Not assessed. Completion evidence: provider/configuration record and qualified privacy/security review. |
| A-05 | No formal review/override or operational feedback path | Define human review/override, incident, and feedback paths for a real deployment. | Prospective deploying organization; before organizational use | Not implemented. Completion evidence: named roles, workflow, and testing evidence. |

No residual risk is accepted on behalf of a company. No organizational monitoring process is in scope for the current portfolio MVP.

## 9. Reassessment triggers

Reassess if any of the following occurs:

- Intended purpose, data type, model/provider, integration, system capability, user group, deployment environment, or lifecycle stage changes.
- Real CRM data, external users, customer deployment, or production operation is proposed.
- New impact, performance, incident, or user-feedback evidence becomes available.
- A company or other deploying organization enters scope; obtain relevant representatives and an accountable risk owner, and develop the desired state using the Current Profile as context.
- NIST revises the AI RMF or a profile/source materially relied upon changes.
- Any other project-specific trigger materially changes the risks or evidence basis.

## 10. Review and sign-off

| Role | Name / status | Review or decision | Date |
|---|---|---|---|
| Assessment owner | Portfolio author | Prepared this record and the linked retrospective. | 24 November 2026 |
| Relevant business / domain owner | None; self-directed project | No company review. | Not applicable |
| Technical / data / security reviewer | No independent reviewer recorded | User-reported testing is identified as such; no independent verification is claimed. | Not recorded |
| Risk / governance reviewer | No independent reviewer recorded | No organizational risk acceptance. | Not recorded |
| Decision-maker | Portfolio owner | Bounded portfolio decision: synthetic demonstration only. | 24 November 2026 |

Owner review of this record remains pending. Sign-off, if later recorded, means review for the stated purpose; it is not certification or proof of control effectiveness.

## 11. Change history

| Record version/date | Change | Reason/source | Affected sections | Reviewed by |
|---|---|---|---|---|
| 0.1 / 24 November 2026 | Initial S02 Variant 1 project assessment record prepared from the retrospective assessment and available project evidence. | Apply the repository NIST project assessment record template to the completed bounded portfolio assessment. | All | Portfolio-owner review pending |

## Use limitation

This record is a structured summary and navigation record for the S02 Variant 1 retrospective application of NIST AI RMF 1.0. The linked retrospective contains the full 72-outcome disposition and row-level analysis. The two records together describe documented implementation and available evidence for a bounded synthetic portfolio MVP. They do not establish a company’s Current or Target Profile, legal compliance, certification, implementation effectiveness, or production readiness.

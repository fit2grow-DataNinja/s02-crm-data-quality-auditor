# Business-facing EU AI Act evaluation overview and status — S02 Variant 1

**Record ID:** S02-EUAI-OVERVIEW-V1-2026-11-24  
**Document status:** Draft for review  
**Assessment status:** Retrospective portfolio screening; preliminary  
**Assessment date:** 24 November 2026  
**Assessed system:** S02 CRM Data Quality & Freshness Auditor — Variant 1  
**Audience:** Managers, decision-makers, external auditors and reviewers  
**Detailed assessment and evidence source:** [EU AI Act retrospective assessment — S02 Variant 1](eu-ai-act-retrospective-assessment.md)  
**Legal snapshot:** Regulation (EU) 2024/1689, consolidated EUR-Lex text dated 27 July 2026, including Regulation (EU) 2026/1744. Verify the current authentic text before relying on this overview for a real deployment.

> This is a concise, business-facing view of a self-directed portfolio assessment. It is not legal advice, an independent audit, a compliance determination, or approval to deploy the system. The linked detailed assessment is the source for provision-level rationale, evidence, open issues, and legal-source traceability; this overview summarizes those findings for business-facing review.

## 1. Executive decision panel

| Question | Current answer |
|---|---|
| What is S02 Variant 1? | A synthetic-data portfolio MVP that runs deterministic CRM data-quality checks and uses a hosted generative model to explain the resulting report. |
| What stage is assessed? | Completed and accepted for the defined synthetic-data demonstration only. It is not production-ready or approved for customer use. |
| What is the current portfolio decision? | Keep the use within the documented synthetic-data, read-only demonstration boundary. Do not use real or sensitive CRM data or expand to customer or production use on the basis of this assessment. |
| What is the preliminary EU AI Act screen? | The current screen found no match for Article 5 or Article 6 / Annex I or III on the documented purpose. This is provision-specific; it does not mean the EU AI Act as a whole is inapplicable. Articles 50(1) and (2), provider/deployer roles, and the exact model/provider configuration need further review. |
| Is a company decision or approval recorded? | No. This is a self-directed portfolio project; no deploying company, company representatives, independent legal reviewer, or external auditor participated in the assessment. |
| What needs attention first? | Clarify the integrated system boundary and operator roles; then resolve Article 50 notice and output-marking questions before any broader EU-facing use. |

The word “decision” above refers only to the portfolio owner’s bounded project decision. It does not represent an organization’s risk acceptance or a legal permission.

## 2. System and use at a glance

| Item | Documented assessment context |
|---|---|
| Purpose | Demonstrate selected CRM data-quality checks with AI-assisted explanation while keeping finding generation deterministic. |
| Inputs | Synthetic contacts, deals and optional association CSV exports. |
| Processing | Python rules calculate the findings. A FastAPI service returns report artifacts. An Open WebUI Workspace Tool sends report content to a configured hosted model for explanation. |
| Outputs | Structured findings and report content; AI-generated explanations are not independently verified. |
| Human role | The tool does not write to CRM. The documentation expects the user to review the output, but a formal approval or override workflow has not been implemented or evaluated. |
| Data boundary | Synthetic data only. Real or sensitive customer CRM data is not approved for this configuration. |
| Demonstration evidence | A reported synthetic run included 202 contacts, 121 deals and 92 medium-severity missing-owner review flags under a provisional rule. These are not confirmed business errors. |
| Key limits | No production/customer deployment, no CRM write-back, no verified real-data privacy assessment, no independent explanation-fidelity evaluation, and no implemented SEC-001 sensitivity/approval gate. |

## 3. How to read the status

The overview uses two separate status dimensions so that a preliminary legal screen is not confused with evidence quality.

**Screening result**

- **Not identified on documented purpose** — we compared the documented purpose and use context with this specific provision and found no match. This is a preliminary, provision-specific result; it does not mean the EU AI Act as a whole is inapplicable.
- **Current functionality excludes this function** — the functionality documented for the assessed version does not include the function covered by this screen. Reassess if functionality or end use changes.
- **Potentially relevant — needs review** — the provision may apply, but a material fact, operator role, exception, or piece of evidence remains unresolved.
- **Not assessed — [reason]** — no conclusion was reached. State the reason with the status: **project scope excludes the use**, **outside this assessment’s scope**, or **evidence unavailable**.

**Evidence / review state**

- **Documented** — stated in project materials; not necessarily independently verified.
- **Not evidenced** — the assessment did not find evidence that resolves the question.
- **Unresolved** — the available information does not settle the fact or role.
- **No independent review recorded** — no independent legal or external audit review is documented.

These labels do not measure compliance. In particular, “Not identified on documented purpose” is specific to the provision screened and must not be read as a conclusion that the EU AI Act does not apply overall.

## 4. EU AI Act screening overview

| Area | Preliminary screening result | Evidence / review state | Business meaning |
|---|---|---|---|
| Article 5 — prohibited practices | **Not identified on documented purpose** | Based on the described CRM data-quality audit and synthetic demonstration; not a complete legal determination. | No prohibited-practice use is described. Re-screen if intended purpose, users, data or deployment changes. |
| Article 6 / Annex I — product or safety-component route | **Not identified on documented purpose** | No regulated product or safety-component role is described. | Re-screen if the tool becomes part of a regulated product or safety function. |
| Article 6 / Annex III — listed high-risk use cases | **Not identified on documented purpose** | The tool is not documented as ranking applicants, making employment decisions, assessing creditworthiness, or performing another listed Annex III purpose. | The current S02 assessment is distinct from a hiring-ranking use case. Any adaptation to applicant filtering, ranking, employee evaluation or another Annex III use requires a fresh assessment. |
| Article 50(1) — informing people of direct AI interaction | **Potentially relevant — needs review** | The demo uses a chat interface and hosted model; provider role, actual interface, and whether AI use is obvious in context are unresolved. | Confirm the responsible provider and review the user-facing interaction and any applicable exception. |
| Article 50(2) — marking synthetic outputs | **Potentially relevant — needs review** | The hosted model generates explanatory text; no evidence establishes the relevant provider, machine-readable marking/detectability, or exception. | Confirm the applicable duty and whether the actual output path satisfies it. Synthetic inputs or internal use do not settle the question. |
| Article 50(3)–(4) — biometric/emotion uses, deepfakes and certain public-interest text | **Current functionality excludes this function** | No emotion-recognition, biometric-categorisation, deepfake, or public-interest text-generation function is documented. | Reassess if the tool gains these functions or generated text is repurposed for public-interest publication. |
| Article 4 — AI literacy | **Not assessed — project scope excludes an organizational workforce assessment** | No deploying company, staff group, or persons acting on a company’s behalf were assessed. | If an organization uses the system with staff or others acting on its behalf, assess context-sensitive literacy measures for the relevant provider/deployer. |
| Chapter V — GPAI model duties | **Not assessed — evidence unavailable (exact hosted model/provider configuration not fixed); provider compliance is outside this assessment’s scope** | The exact hosted model, version, and provider configuration are not fixed in this record. | Identify the model/provider and relevant value-chain responsibilities; this overview makes no finding about provider compliance. |
| Registration duties | **Not identified on documented purpose and known role facts** | No high-risk use or Article 6(3) exception reliance is identified; no other registration trigger is established by the available facts. | Recheck if classification or operator roles change. |
| Article 27 — fundamental-rights impact assessment | **Not assessed — project scope excludes an organizational deployer assessment** | No deploying company or specified public-authority / public-service deployer context is in scope; future deployer facts are unknown. | Reassess if an organization proposes a high-risk use or another Article 27 trigger is identified. |
| GDPR and other laws | **Not assessed — project scope excludes real personal-data processing and organizational deployment** | The documented demo is synthetic-only; no real-data privacy assessment is included. | Obtain specialist review before real personal data, customer deployment, or use in a regulated sector. |

The high-risk screening does not rely on an Article 6(3) exception: no Annex III match was found for the documented purpose, so the exception was not assessed or relied upon. The detailed record explains this distinction and lists the applicable-date questions.

## 5. Roles and accountability

| Actor | Current assessment status |
|---|---|
| Portfolio author / project owner | Authorship and public source-code availability are documented. Provider or deployer status for the integrated system is **unresolved**; those facts alone do not settle the legal role. |
| Person operating the local demo | Potential deployer role depends on authority and whether use is professional or personal/non-professional; current facts are incomplete. |
| Hosted model provider | Provider and model-version details are **not fixed** for this record. No assessment of provider compliance is made. |
| Open WebUI / hosting and integration suppliers | Components are documented, but legal roles, terms, data location and contractual allocation are **not assessed**. |
| Importer, distributor, authorised representative, deploying company | No such separate actor or company is identified in the current portfolio scenario. |

Roles depend on activities and statutory definitions, not only on repository names or contractual labels. See the detailed assessment for the role questions and the evidence needed to resolve them.

## 6. Priority actions and decision gates

These are portfolio follow-up actions, not a statement that every item is a statutory requirement for the current synthetic demo.

| Priority | Action / question | Why it matters | Owner / timing |
|---|---|---|---|
| Maintain current boundary | Keep the synthetic-only, read-only restriction prominent; do not process real or sensitive CRM data in this configuration. | SEC-001 sensitivity tagging, fail-closed handling and manual approval are not implemented or tested. | Portfolio owner; ongoing and before any change. |
| Resolve system and operator roles | Define the integrated AI-system boundary, who offers or operates each component, the name/brand used, professional context, and relevant dates. | Provider and deployer duties attach to role and activity; these facts remain unresolved. | Portfolio owner and any prospective deploying organization; before broader EU-facing use. |
| Review Article 50(1) | Inspect the actual chat experience and determine whether direct-interaction information is needed and who is responsible. | Current materials do not establish the interface condition or provider role. | Responsible provider once identified; before broader use. |
| Review Article 50(2) | Identify the model/provider, determine applicability and any exception, and obtain evidence about output marking and detectability. | No marking or test evidence is recorded; the transition question is unresolved. | Relevant provider/system owner; before broader use and by the applicable date. |
| Confirm model and data path | Record exact model/version, provider configuration, and relevant data handling, retention and transfer terms. | The current assessment does not establish these details or approve real-data processing. | Portfolio owner and suppliers; before any real-data or organizational use. |
| Obtain specialist review for a real deployment | Reassess current law, roles, privacy and sector obligations with qualified reviewers. | This portfolio screen is not legal advice or an organizational assessment. | Prospective deploying organization; before pilot or production. |

## 7. Evidence, review limits and source traceability

The overview is derived from the [EU AI Act retrospective assessment](eu-ai-act-retrospective-assessment.md). That assessment links each screening conclusion to project evidence and the legal/guidance sources used.

| Evidence group | What it supports | Important limit |
|---|---|---|
| [Project README and status](../README.md) and [PROJECT-STATUS.md](../PROJECT-STATUS.md) | Purpose, MVP status, synthetic-only restriction and documented limitations. | Project-authored statements; not independent assurance. |
| [Architecture](architecture.md), [integration](integration.md) and [security status](security.md) | Component and data flow, read-only path, hosted-model interaction, and SEC-001 status. | Do not establish legal role, provider compliance, GDPR compliance, or output marking. |
| [Service specification](service-specification.md) and [validation record](validation.md) | Reported synthetic demonstration and local test evidence. | User-reported runs were not independently repeated for this assessment. |
| [Binding AI Act text snapshot](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng) | Legal provisions and application/transition dates referenced by the detailed assessment. | Check current authentic legal texts before applying to a real deployment. |

**Review statement:** the assessment was prepared by the portfolio author. No company representatives, independent legal reviewer, external auditor, or management approver are recorded. External auditors and reviewers are an intended audience for this overview; their review has not yet occurred.

The [NIST AI RMF retrospective assessment](nist-ai-rmf-retrospective-assessment.md) is a separate companion record. Its voluntary risk-management analysis is not combined with or treated as an EU AI Act legal conclusion here.

## 8. Reassessment triggers and change history

Reassess before real or sensitive data, customer or production use, a new provider/model, a new user group, a changed intended purpose, write-back or decision automation, deployment by an organization, or adaptation to HR/applicant ranking or another Annex III use. Recheck the legal text and guidance source status before relying on this overview for a real deployment.

| Date | Change |
|---|---|
| 24 November 2026 | Initial business-facing overview created from the S02 Variant 1 EU AI Act retrospective assessment and its linked evidence. |

## Use limitation

This overview is a readable summary and status index, not a substitute for the detailed assessment, the binding Regulation, an organizational decision, an independent audit, or qualified legal and data-protection advice.

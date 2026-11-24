# EU AI Act retrospective assessment — S02 Variant 1

**Record ID:** S02-EUAI-ACT-RETRO-V1-2026-11-24  
**Status:** Retrospective portfolio screening; draft for review  
**Assessment date:** 24 November 2026  
**Assessment owner:** Portfolio author  
**Contributors / company representatives:** None; self-directed portfolio project  
**Assessment type:** Retrospective preliminary issue-spotting  
**Legal source snapshot:** Regulation (EU) 2024/1689, consolidated EUR-Lex text dated 27 July 2026, including Regulation (EU) 2026/1744; verify the authentic Official Journal texts and EUR-Lex for later amendments before applying to a real deployment.  
**Working method:** [EU AI Act project-evaluation matrix](https://github.com/fit2grow-DataNinja/ai-governance-frameworks/blob/main/working-documents/eu-ai-act-project-evaluation-matrix.md) (reviewed 23 November 2026; working draft, pre-v1.0) and [project-screening record template](https://github.com/fit2grow-DataNinja/ai-governance-frameworks/blob/main/working-documents/project-screening-record-template.md).  
**Solution repository:** [S02 CRM Data Quality & Freshness Auditor — Variant 1](https://github.com/fit2grow-DataNinja/s02-crm-data-quality-auditor)  
**Business-facing summary:** [EU AI Act evaluation overview and status — S02 Variant 1](eu-ai-act-evaluation-overview-status.md)

> This is a bounded, repository-authored learning assessment of the documented synthetic-data MVP. It is not legal advice, a legal classification, a compliance determination, or proof that any operator has met an obligation. Results are preliminary and depend on the stated facts, role, system boundary, jurisdiction, and legal snapshot.

## How to use this record

For the concise, decision-oriented status and audience-specific summary, start with the [business-facing EU AI Act evaluation overview](eu-ai-act-evaluation-overview-status.md). It summarizes the current portfolio decision, screening outcomes, priority questions, and review limitations.

This document is the detailed assessment behind that overview. It records the system scope, role questions, provision-by-provision screening rationale, open issues, evidence, and source snapshot. Use it when a reviewer needs to trace a summary status back to the underlying facts and sources. The overview does not replace this record, and this record does not claim independent review or legal clearance.

## 1. System, purpose, and assessment boundary

S02 Variant 1 accepts synthetic contact, deal, and optional association CSV exports through a Python/FastAPI audit service. Deterministic rules produce structured findings and report artifacts. An Open WebUI Workspace Tool sends attached files to the local API and returns report content into the chat context for explanation by a configured hosted model.

**Intended portfolio purpose:** demonstrate how deterministic CRM data-quality checks can be paired with AI-assisted explanation while keeping the finding-generation and explanation roles separate.

**Documented boundaries:** synthetic data only; read-only with no CRM write-back; no production or customer deployment; no approval to process real or sensitive customer data; AI explanations are not independently verified. The missing-owner rule is provisional. A demonstration reported 202 contacts, 121 deals, and 92 medium-severity missing-owner review flags; these are not confirmed business errors.

The assessment covers the integrated Variant 1 demo path described in the repository, not the hosted model provider’s compliance, Open WebUI’s general service, Variant 2, an employing or deploying company, or real CRM processing. The exact deployed model version and all runtime settings are not fixed in this assessment. The repository’s public availability is recorded as a fact but is not, by itself, treated as proof that a regulated AI system has been placed on the market or put into service.

## 2. Preliminary organization and value-chain roles

Roles follow the activities and facts under the Regulation; repository labels or contracts alone do not determine them. This table records issues to resolve, not final role assignments.

| Entity / actor | Observed or reported activity | Preliminary role question | What is established / unresolved |
|---|---|---|---|
| Portfolio author / project owner | Authored the deterministic audit service and Workspace Tool; conducted or documented synthetic demonstrations; made source code available in a public repository. | Could be a provider if the integrated AI system is placed on the market or put into service under the author’s own name or trademark. Could also be a deployer when using the system under their authority in a professional activity. | The repository establishes authorship and a portfolio demonstration, but does not establish the precise system boundary, market offering, name/brand, professional-use facts, or date of any placing on the market / putting into service. Resolve before making a role conclusion. |
| Person operating the local demonstration | Attaches synthetic CSV files and invokes the tool in Open WebUI. | Potential deployer if using the AI system under their authority; the Act excludes use in a personal, non-professional activity from the deployer definition. | The evidence describes portfolio demonstrations but does not fully establish the legal capacity or authority in which each run occurred. |
| Hosted model provider | Supplies the configured generative model used to explain the report. Project materials refer to GPT-4.1-mini in a demonstration, but do not fix the deployed version or complete configuration. | Provider of a GPAI model may have Chapter V duties; it may also be provider of an AI system depending on the service and facts. | This assessment does not establish provider identity for the exact runtime, model classification, contractual terms, or compliance. Obtain the actual model/provider record if the service is used beyond the documented demo. |
| Open WebUI / hosting and integration suppliers | Open WebUI hosts the chat interface; the configured model is accessed through a hosted service. | Supplier, provider, or other value-chain role depends on the functions and legal arrangements; no role is assigned here. | Current evidence describes the component path but does not establish supplier contracts, controller/processor roles, data location, or the relevant AI Act responsibilities. |
| Importer, distributor, authorised representative, deploying company | No such separate actor or company is documented for this self-directed portfolio MVP. | No role identified on current evidence. | Reassess if a company adopts, imports, distributes, rebrands, substantially modifies, or changes the intended purpose of the system. |

The AI Act defines provider and deployer roles in Article 3 and addresses certain value-chain role changes in Article 25. A project author or tool operator should not assume a role conclusion without checking the statutory definitions against actual activities.

## 3. Screening results

Use the same status meanings as the [business-facing overview](eu-ai-act-evaluation-overview-status.md):

- **Not identified on documented purpose** — the documented purpose and context were compared with a specific provision and no match was found. This preliminary result is provision-specific and does not mean the EU AI Act as a whole is inapplicable.
- **Current functionality excludes this function** — the documented functionality of this version does not include the function being screened; reassess if functionality or end use changes.
- **Potentially relevant — needs review** — the provision may apply, but a material fact, operator role, exception, or evidence remains unresolved.
- **Not assessed — [reason]** — no conclusion was reached; state whether the reason is that the project scope excludes the use, the issue is outside this assessment’s scope, or evidence is unavailable.

### 3.1 Scope and Article 5 — prohibited practices

**Status: Not identified on documented purpose.**

The described function is to audit selected fields in synthetic CRM exports and explain the resulting report. We compared that documented purpose with the Article 5 screen and found no match in the available facts. This is a preliminary result for Article 5 only; it does not mean that the EU AI Act as a whole is inapplicable or establish that every possible use is permissible. The assessment is not a complete feature-by-feature legal analysis.

**Re-screen if:** the intended purpose, inputs, users, or deployment changes, especially if the system is connected to decisions about natural persons or used in a context covered by Article 5.

### 3.2 Article 6 and Annexes I / III — high-risk classification

| Route / question | Preliminary result | Basis in the documented S02 scope | Reassessment trigger |
|---|---|---|---|
| Article 6(1), Annex I product or safety-component route | Not identified on documented purpose | S02 is documented as a stand-alone CRM export-audit portfolio tool, not an AI safety component or regulated product. No Annex I product or third-party product conformity-assessment route is described. | Integration into a regulated product or safety function. |
| Article 6(2), Annex III use case | Not identified on documented purpose | The tool checks CRM record quality and explains report content. It is not documented as recruiting or selecting people, evaluating employees, assessing creditworthiness, deciding access to essential services, or serving another Annex III purpose. | Any change to a listed Annex III purpose, user group, or operational role. In particular, use for applicant filtering/ranking or employment decisions requires a fresh employment-area screen. |
| Article 6(3) exception for an Annex III system | Not assessed — outside this assessment’s scope because no Annex III match was found on documented purpose | No Annex III use was identified, so the Article 6(3) exception was not examined or relied upon. | If an Annex III use is identified, assess all statutory conditions, profiling consequences, provider documentation, and Article 49(2) registration. |
| High-risk provider/deployer duties | Not assessed — outside this assessment’s scope because no high-risk match was found on documented purpose | No Annex I or Annex III match was identified, so actor-specific high-risk duties were not assessed as current obligations. This is not a finding that the system is compliant with duties that could apply if purpose or classification changes. | Reassess classification and applicable dates before a changed use or deployment. |

The absence of applicant ranking is material to this assessment: the current S02 tool is not the hiring-ranking example previously discussed. Its “owner missing” flag concerns a provisional CRM data-quality rule and is not documented as scoring a job applicant or deciding whether someone gets an interview. The Article 5 and Article 6 results above are provision-specific; they do not establish that the EU AI Act as a whole is inapplicable.

The framework’s current source snapshot states that Annex III high-risk requirements apply from 2 December 2027 and Annex I high-risk requirements from 2 August 2028, subject to the consolidated Regulation and the precise system facts. These future dates do not remove the need to screen a planned system now. Verify the current law before any real deployment.

### 3.3 Article 50 — transparency obligations

| Provision | Preliminary result | S02 facts and unresolved issues |
|---|---|---|
| Article 50(1) — direct interaction | **Potentially relevant — needs review.** | A person uses an Open WebUI chat and a hosted model explains the audit report. Establish whether the integrated system is intended to interact directly with natural persons, who its provider is, and whether the AI nature is obvious to a reasonably well-informed, observant, and circumspect person in the actual interface and context. No interface evidence establishes that the notice condition or exception is met. |
| Article 50(2) — machine-readable marking of synthetic outputs | **Potentially relevant — needs review.** | The hosted model generates synthetic explanatory text. Establish which provider is responsible for the relevant AI system, whether the provision applies to this output and system, whether an exception applies, and whether outputs are marked in a machine-readable format and detectable as artificially generated. The project has no evidence of such marking or testing. Internal chat output and synthetic input data do not, by themselves, settle this screen. |
| Article 50(3) — emotion recognition / biometric categorisation | **Current functionality excludes this function.** | No emotion-recognition or biometric-categorisation function is documented in the assessed functionality. Reassess if functionality or use changes. |
| Article 50(4) — deepfakes / public-interest text | **Current functionality excludes this function.** | The assessed functionality produces explanatory chat text for the CRM demonstration; it does not generate deepfakes or publish text to inform the public on a matter of public interest. Reassess if functionality or use changes. |
| Article 50(5) — timing, presentation, accessibility | **Not assessed — outside this assessment’s scope pending paragraphs 1–4; no notice/marking design has been evaluated.** | If a preceding duty applies, the responsible actor must assess timing, presentation, and accessibility. No notice or marking design has been assessed here. |

Article 50(2) has a specific transition for certain systems placed on the market before 2 August 2026, with compliance required by 2 December 2026. The available evidence does not establish whether S02 meets the transition’s system and market-placement conditions. Do not assume the transition applies. Article 50 transparency obligations generally apply from 2 August 2026; verify the exact consolidated text and facts.

### 3.4 Other AI Act duties

| Separate screen | Preliminary result | S02-specific reasoning and limits |
|---|---|---|
| Article 4 — AI literacy | **Not assessed — project scope excludes an organizational workforce assessment.** | No company, staff group, or persons acting on a company’s behalf are part of this portfolio assessment. If a provider or deployer uses the system with staff or other persons acting on its behalf, Article 4 requires context-sensitive measures to support AI literacy; it does not require a guaranteed level for each individual. |
| Chapter V — GPAI model obligations | **Not assessed — evidence unavailable (exact model/provider configuration not fixed); provider compliance is outside this assessment’s scope.** | A hosted generative model is part of the workflow, but the exact model/version and provider configuration are not fixed here. GPAI provider duties belong to the relevant model provider; this record makes no finding about that provider’s compliance. If the portfolio author or another entity is a downstream AI-system provider, confirm what documentation/information is relevant to its role. |
| Registration and database duties | **Not identified on documented purpose; role-dependent questions remain open.** | No high-risk system or provider relying on Article 6(3) is identified in the documented use. Operator roles are not fully assigned, so recheck registration duties if the classification or role analysis changes. |
| Article 27 — fundamental-rights impact assessment | **Not assessed — project scope excludes an organizational deployer assessment.** | No high-risk use or specified public-authority / public-service deployer context is described. The assessment does not establish the status of any future deployer. |
| Other duties for high-risk systems | **Not assessed — outside this assessment’s scope because no high-risk match was found on documented purpose.** | Because no high-risk route is identified for the documented purpose, the assessment does not map Articles 9–21, 26, or related high-risk duties as current requirements. Reassess before any purpose or deployment change. |

### 3.5 Other law and separate legal checks

- **Data protection — Not assessed (project scope excludes real personal-data processing):** the project describes its sample datasets as synthetic and prohibits real customer data. This assessment did not independently validate every sample value or inspect a live data flow. The hosted-model path may process report content; no real personal-data processing is approved or assessed. If real CRM data is proposed, separately establish whether it contains personal data, controller/processor roles, lawful basis, transparency, purpose limitation, minimisation, retention, security, transfers, and whether a GDPR DPIA is required. No GDPR compliance conclusion is made.
- **Employment and workplace law — current functionality excludes the assessed HR decision functions; other employment-law questions are not assessed (project scope excludes organizational use):** no HR, applicant-ranking, employee evaluation, or employment decision use is documented. If the tool is adapted to support hiring, employee monitoring, or workforce decisions, conduct a fresh AI Act and employment-law assessment before use.
- **Consumer, product-safety, accessibility, cybersecurity, and sector-specific law — Not assessed (outside this assessment’s scope):** no current facts establish a specific trigger, and these areas were not comprehensively assessed. Screen them if the system is marketed, integrated into a regulated product, exposed to customers, or used in a regulated sector.
- These checks are non-exhaustive and should be performed by appropriately qualified specialists when a real organization or deployment is involved.

## 4. Open questions, follow-up, and bounded decision

The screening in Section 3 is preliminary and tied to the documented synthetic-data MVP. The issues below identify facts or evidence needed to resolve the open questions; they do not declare that every item is a legal duty for the current demonstration.

| Issue | What is established / unresolved | Follow-up and decision gate | Suggested owner |
|---|---|---|---|
| System boundary and operator roles | The integrated path includes the audit API, Open WebUI adapter, and hosted model. The portfolio author, local operator, model provider, and integration suppliers may have different roles; the repository and code authorship alone do not settle provider/deployer status or market-placement facts. | Record the exact system boundary, who develops/offers/operates each component, the name or trademark used, the professional context, and relevant dates. Reassess before organizational or broader EU-facing use. | Portfolio owner; any prospective deploying organization; relevant suppliers |
| **Potentially relevant — needs review: Article 50(1) — direct interaction** | A person interacts through a chat interface, but the actual interface, intended interaction, responsible provider, and whether the AI nature is obvious in context are not established. | Review the actual user experience, identify the responsible provider, and document the applicable trigger, exception, timing, and any notice evidence before broader use. | Responsible provider once identified |
| **Potentially relevant — needs review: Article 50(2) — generated text and marking** | The hosted model generates explanatory text. The responsible provider, applicability, exceptions, technical marking/detectability, and Article 111(4) transition facts are unresolved. | Identify the exact model and provider; confirm the applicable legal trigger and transition; obtain or test evidence for any required machine-readable marking and detectability before broader use. | Relevant provider / system owner |
| **Not assessed — evidence unavailable: GPAI model and supplier data path** | The model/version and complete runtime configuration are not fixed; provider compliance and the actual data-processing terms have not been assessed. | Record model/version/provider and relevant technical and contractual information. Review data handling, retention, access, and transfers before organizational use or any real-data proposal. | Portfolio owner and suppliers; prospective deployer |
| **Not assessed — project scope excludes organizational use: organization-specific duties and other law** | No company or workforce was assessed. Article 4 measures, Article 27 context, GDPR duties, and sector-specific laws depend on actor, people, data, use, and jurisdiction facts. | If a real organization or real data enters scope, conduct a separate role-specific legal and data-protection review; determine which specialist assessments are triggered. | Prospective deploying organization with qualified reviewers |
| Purpose, users, data, and lifecycle changes | Current screening is limited to synthetic CRM data-quality review and explanation, without CRM write-back or production operation. | Re-screen before real/sensitive data, customer or production use, new providers/models, new user groups, automated decisions or write-back, HR/applicant ranking, or another Annex III / Article 50 use. Recheck legal sources when law or guidance changes. | Portfolio owner; prospective deploying organization |

**Bounded portfolio disposition:** retain Variant 1 as a synthetic-data portfolio demonstration only. Do not use real or sensitive CRM data or deploy for customers or in production on the basis of this assessment. The project is closed only for its defined MVP criteria; this is not a company risk acceptance, deployment authorization, or legal-compliance conclusion.

## 5. Sources and evidence

### Project evidence

- **E-01 — README and project status:** [README](https://github.com/fit2grow-DataNinja/s02-crm-data-quality-auditor/blob/main/README.md) and [PROJECT-STATUS.md](https://github.com/fit2grow-DataNinja/s02-crm-data-quality-auditor/blob/main/PROJECT-STATUS.md), checked 24 November 2026. Supports stated purpose, synthetic-only scope, MVP status, and limitations. Project-authored; not independent assurance.
- **E-02 — Architecture, integration, and security:** [architecture](https://github.com/fit2grow-DataNinja/s02-crm-data-quality-auditor/blob/main/docs/architecture.md), [integration](https://github.com/fit2grow-DataNinja/s02-crm-data-quality-auditor/blob/main/docs/integration.md), and [security status](https://github.com/fit2grow-DataNinja/s02-crm-data-quality-auditor/blob/main/docs/security.md), checked 24 November 2026. Supports data flow, read-only boundary, hosted-model interaction, and absent SEC-001 gate. Does not establish provider legal role, privacy compliance, marking, or independent security assurance.
- **E-03 — Service specification and validation:** [service specification](https://github.com/fit2grow-DataNinja/s02-crm-data-quality-auditor/blob/main/docs/service-specification.md) and [validation record](https://github.com/fit2grow-DataNinja/s02-crm-data-quality-auditor/blob/main/docs/validation.md), checked 24 November 2026. Supports synthetic demonstration counts and reported test evidence. Tests were not independently rerun for this assessment.

### Legal and guidance sources

- **Binding text:** [EUR-Lex consolidated Regulation (EU) 2024/1689, version dated 27 July 2026](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng), including Regulation (EU) 2026/1744. Relevant provisions include Articles 2–6, 25–27, 49–50, 111, 113 and Annexes I and III. The consolidated text is a documentation aid; consult the authentic acts in the Official Journal for legal effect.
- **High-risk classification guidance:** [European Commission guidelines page](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-high-risk-systems). The framework source record reviewed 23 November 2026 describes the classification guidelines as draft at that time; recheck current adoption status before relying on it. Non-binding guidance does not replace the Regulation.
- **Article 50 guidance:** [European Commission transparency guidelines](https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems), published 20 July 2026; interpretive support, not binding legislation.
- **Official implementation support:** [AI Act Service Desk — Article 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50). Its summaries are explanatory and non-binding; the Regulation controls.
- **Framework records:** [SRC-001 — consolidated text](https://github.com/fit2grow-DataNinja/ai-governance-frameworks/blob/main/sources/records/SRC-001-eu-ai-act-consolidated-text.md), [SRC-002 — high-risk guidance status](https://github.com/fit2grow-DataNinja/ai-governance-frameworks/blob/main/sources/records/SRC-002-high-risk-classification-guidance.md), [SRC-003 — Article 50 guidance](https://github.com/fit2grow-DataNinja/ai-governance-frameworks/blob/main/sources/records/SRC-003-article-50-transparency-guidance.md), and [SRC-008 — Article 4 AI literacy](https://github.com/fit2grow-DataNinja/ai-governance-frameworks/blob/main/sources/records/SRC-008-ai-act-article-4-ai-literacy.md).

## 6. Use limitation

This assessment records preliminary issue-spotting against a dated legal snapshot and available project documentation. It does not establish provider/deployer status, compliance, absence of legal duties, privacy or security compliance, or readiness for real-data use. For a concrete EU deployment, confirm the current law, full facts, actors, and applicable dates with qualified legal and data-protection specialists.

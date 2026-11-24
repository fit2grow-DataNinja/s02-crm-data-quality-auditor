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

> This is a bounded, repository-authored learning assessment of the documented synthetic-data MVP. It is not legal advice, a legal classification, a compliance determination, or proof that any operator has met an obligation. Results are preliminary and depend on the stated facts, role, system boundary, jurisdiction, and legal snapshot.

## Executive summary

S02 Variant 1 is a self-directed portfolio MVP that audits synthetic CRM exports using deterministic Python rules and provides report content to a hosted generative model for natural-language explanation. It is read-only, is not approved for real or sensitive CRM data, and is not production-ready or approved for customer use. The assessment is limited to this described purpose and the evidence in the repository.

On the documented purpose, **no Article 5 prohibited practice or Annex I / Annex III high-risk use has been identified**. The tool checks completeness and other selected CRM data-quality rules; it does not rank people, select applicants, make employment decisions, or profile natural persons. This is a preliminary screening result, not a definitive legal classification. A change to the intended purpose or operating context could change it.

**Article 50 needs specific follow-up.** The conversational workflow involves a natural person interacting with a hosted model, and it generates explanatory text. Depending on the system boundary, provider role, interface, and applicable exceptions, Articles 50(1) and 50(2) may be relevant. The current record does not establish whether users are clearly informed, whether generated text is machine-readably marked and detectable, who carries the provider duty for the integrated system, or whether Article 111(4)'s transition applies. “Internal” or synthetic-data use alone does not resolve those questions.

The record also flags role and scope facts that are not established by the project materials: whether the portfolio author has placed an AI system on the market or put it into service under their name, whether the local demonstration constitutes professional deployment, and which exact model/provider configuration was used. The public source-code repository by itself does not resolve those legal questions.

**Bounded portfolio decision:** keep Variant 1 within its documented synthetic-data demonstration scope. Do not use real or sensitive CRM data, deploy it for customers or in production, or treat this assessment as permission to do so. Re-screen before any market offering, organizational use, new data type, new user group, or change in intended purpose. No company-level legal or risk decision is made here.

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

### 3.1 Scope and Article 5 — prohibited practices

**Preliminary result: No prohibited practice identified on the documented intended purpose.**

The described function is to audit selected fields in synthetic CRM exports and explain the resulting report. No use involving prohibited social scoring, manipulation, exploitation, biometric categorisation, emotion recognition, or another Article 5 practice is documented. The assessment is not a complete feature-by-feature Article 5 legal analysis and cannot establish that every possible use is permissible.

**Re-screen if:** the intended purpose, inputs, users, or deployment changes, especially if the system is connected to decisions about natural persons or used in a context covered by Article 5.

### 3.2 Article 6 and Annexes I / III — high-risk classification

| Route / question | Preliminary result | Basis in the documented S02 scope | Reassessment trigger |
|---|---|---|---|
| Article 6(1), Annex I product or safety-component route | Not identified | S02 is documented as a stand-alone CRM export-audit portfolio tool, not an AI safety component or regulated product. No Annex I product or third-party product conformity-assessment route is described. | Integration into a regulated product or safety function. |
| Article 6(2), Annex III use case | Not identified on stated intended purpose | The tool checks CRM record quality and explains report content. It is not documented as recruiting or selecting people, evaluating employees, assessing creditworthiness, deciding access to essential services, or serving another Annex III purpose. | Any change to a listed Annex III purpose, user group, or operational role. In particular, use for applicant filtering/ranking or employment decisions requires a fresh employment-area screen. |
| Article 6(3) exception for an Annex III system | Not relied upon | No Annex III route has been identified, so this assessment does not claim or document the Article 6(3) exception. | If an Annex III use is identified, assess all statutory conditions, profiling consequences, provider documentation, and Article 49(2) registration. |
| High-risk provider/deployer duties | Not triggered by the preliminary screen | No high-risk classification is identified on current facts. This is not a finding that the system is compliant with duties that would apply if its purpose or classification changes. | Reassess classification and applicable dates before a changed use or deployment. |

The absence of applicant ranking is material to this assessment: the current S02 tool is not the hiring-ranking example previously discussed. Its “owner missing” flag concerns a provisional CRM data-quality rule and is not documented as scoring a job applicant or deciding whether someone gets an interview.

The framework’s current source snapshot states that Annex III high-risk requirements apply from 2 December 2027 and Annex I high-risk requirements from 2 August 2028, subject to the consolidated Regulation and the precise system facts. These future dates do not remove the need to screen a planned system now. Verify the current law before any real deployment.

### 3.3 Article 50 — transparency obligations

| Provision | Preliminary result | S02 facts and unresolved issues |
|---|---|---|
| Article 50(1) — direct interaction | **Potentially relevant; needs review.** | A person uses an Open WebUI chat and a hosted model explains the audit report. Establish whether the integrated system is intended to interact directly with natural persons, who its provider is, and whether the AI nature is obvious to a reasonably well-informed, observant, and circumspect person in the actual interface and context. No interface evidence establishes that the notice condition or exception is met. |
| Article 50(2) — machine-readable marking of synthetic outputs | **Potentially relevant; needs provider and technical review.** | The hosted model generates synthetic explanatory text. Establish which provider is responsible for the relevant AI system, whether the provision applies to this output and system, whether an exception applies, and whether outputs are marked in a machine-readable format and detectable as artificially generated. The project has no evidence of such marking or testing. Internal chat output and synthetic input data do not, by themselves, settle this screen. |
| Article 50(3) — emotion recognition / biometric categorisation | **Not identified.** | No emotion-recognition or biometric-categorisation function is documented. |
| Article 50(4) — deepfakes / public-interest text | **Not identified for current use.** | The tool produces private explanatory chat text for a synthetic CRM demonstration; it is not documented as generating a deepfake or text published to inform the public on a matter of public interest. Reassess if generated explanations are published or repurposed. |
| Article 50(5) — timing, presentation, accessibility | **Depends on paragraphs 1–4.** | If a preceding duty applies, the responsible actor must assess when and how information is presented, including accessibility. No notice or marking design has been assessed here. |

Article 50(2) has a specific transition for certain systems placed on the market before 2 August 2026, with compliance required by 2 December 2026. The available evidence does not establish whether S02 meets the transition’s system and market-placement conditions. Do not assume the transition applies. Article 50 transparency obligations generally apply from 2 August 2026; verify the exact consolidated text and facts.

**Action before any broader use:** identify the provider(s) and actual model configuration; inspect the user interface and output path; obtain provider information on machine-readable marking/detectability; document the applicable Article 50 paragraph, any exception, applicable date, responsible actor, and evidence.

### 3.4 Other AI Act duties

| Separate screen | Preliminary result | S02-specific reasoning and limits |
|---|---|---|
| Article 4 — AI literacy | **Applicability to a provider/deployer workforce is unresolved; no company program assessed.** | No company, staff group, or persons acting on a company’s behalf are part of this portfolio assessment. If a provider or deployer uses the system with staff or other persons acting on its behalf, Article 4 requires context-sensitive measures to support AI literacy; it does not require a guaranteed level for each individual. |
| Chapter V — GPAI model obligations | **Model-provider screen needed; not assessed.** | A hosted generative model is part of the workflow, but the exact model/version and provider configuration are not fixed here. GPAI provider duties belong to the relevant model provider; this record makes no finding about that provider’s compliance. If the portfolio author or another entity is a downstream AI-system provider, confirm what documentation/information is relevant to its role. |
| Registration and database duties | **No registration duty identified on the current preliminary classification.** | No high-risk system or provider relying on Article 6(3) is identified. No other registration trigger is established by the evidence. Recheck if role or classification changes. |
| Article 27 — fundamental-rights impact assessment | **Not identified on current facts.** | No high-risk use or specified public-authority / public-service deployer context is described. The assessment does not establish the status of any future deployer. |
| Other duties for high-risk systems | **No current trigger identified.** | Because no high-risk route is identified for the documented purpose, the assessment does not map Articles 9–21, 26, or related high-risk duties as current requirements. Reassess before any purpose or deployment change. |

### 3.5 Other law and separate legal checks

- **Data protection:** the project describes its sample datasets as synthetic and prohibits real customer data. This assessment did not independently validate every sample value or inspect a live data flow. The hosted-model path may process report content; no real personal-data processing is approved or assessed. If real CRM data is proposed, separately establish whether it contains personal data, controller/processor roles, lawful basis, transparency, purpose limitation, minimisation, retention, security, transfers, and whether a GDPR DPIA is required. No GDPR compliance conclusion is made.
- **Employment and workplace law:** no HR, applicant-ranking, employee evaluation, or employment decision use is documented. If the tool is adapted to support hiring, employee monitoring, or workforce decisions, conduct a fresh AI Act and employment-law assessment before use.
- **Consumer, product-safety, accessibility, cybersecurity, and sector-specific law:** no current facts establish a specific trigger, but these areas were not comprehensively assessed. Screen them if the system is marketed, integrated into a regulated product, exposed to customers, or used in a regulated sector.
- These checks are non-exhaustive and should be performed by appropriately qualified specialists when a real organization or deployment is involved.

## 4. Preliminary obligations and evidence summary

| Topic | Classification | Current status | Evidence needed / next step |
|---|---|---|---|
| Article 5 prohibited practices | Binding-law screen | No prohibited practice identified on documented purpose; preliminary only. | Preserve intended-purpose statement; repeat screen if system use or context changes. |
| Article 6 / Annex I and III classification | Binding-law screen | No route identified for current CRM audit purpose; not a legal determination. | Confirm system boundary and intended purpose; screen again before changed use or deployment. |
| Provider/deployer and value-chain roles | Binding-law role definitions | Unresolved for integrated system, portfolio author, model supplier, and local demo operator. | Document who developed, offers, names, places on market, configures, and operates each component; establish dates and professional context. |
| Article 50(1) notice | Binding-law screen | Potentially relevant; notice/obviousness and provider role not evidenced. | Review actual interface and determine responsible provider and notice treatment. |
| Article 50(2) synthetic-output marking | Binding-law screen | Potentially relevant; machine-readable marking/detectability and applicable transition not evidenced. | Obtain exact model/provider information and test/document marking; determine whether Article 111(4) transition applies. |
| Article 50(3)–(4) | Binding-law screen | Not identified for current documented functions and use. | Re-screen if biometric/emotion functions or public-interest publication/deepfake outputs are introduced. |
| Article 4 AI literacy | Binding-law duty, role/context dependent | No company workforce or measures assessed. | If staff or persons acting on behalf of a provider/deployer are involved, identify them and document context-sensitive measures. |
| GPAI Chapter V | Binding-law duties of relevant model provider | Exact model/provider is not fixed; provider compliance not assessed. | Record model name/version/provider and obtain relevant provider documentation. |
| Registration / Article 27 FRIA | Binding-law screens | No trigger identified on current facts. | Recheck if classification, actor, or use context changes. |
| GDPR and other law | Separate legal checks | Not assessed for real personal data or organizational deployment. | Specialist review before any real-data, customer, or production use. |

The categories above distinguish binding legal duties from unresolved facts and separate-law questions. The suggested evidence is not a universal statutory documentation package.

## 5. Preliminary decision and reassessment triggers

**Decision:** retain Variant 1 as a synthetic-data portfolio demonstration only. Do not use real or sensitive CRM data or deploy it for customer or production use. The project remains closed only for its documented MVP criteria; this assessment does not authorize expanded use or establish legal compliance.

**Open questions for any future EU-facing use:**

1. What is the precise AI-system boundary: hosted model alone, integrated S02 workflow, or both?
2. Who developed, provides, operates, hosts, and controls each component; under whose name or trademark is the integrated system offered or put into service?
3. When and where was it used, and in what professional or personal capacity?
4. Which exact hosted model, version, provider, and settings were used in each demonstration?
5. Do Article 50(1) and (2) apply to the exact system and interface, who is responsible, and what notice/marking evidence exists?
6. Does the Article 111(4) transition apply to the relevant system and market-placement facts?
7. Are any actual or planned inputs personal data, and what are the provider’s data handling, retention, access, and transfer conditions?
8. Will the tool ever be adapted for HR, applicant ranking, employee evaluation, public-facing content, or another Annex III / Article 50 use?

Reassess if the intended purpose, model/provider, data, affected people, user group, integration, operating authority, deployment country, market offering, or lifecycle stage changes; if real CRM data or customer use is proposed; or if the AI Act or relevant official guidance changes.

## 6. Sources and evidence

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

## 7. Use limitation

This assessment records preliminary issue-spotting against a dated legal snapshot and available project documentation. It does not establish provider/deployer status, compliance, absence of legal duties, privacy or security compliance, or readiness for real-data use. For a concrete EU deployment, confirm the current law, full facts, actors, and applicable dates with qualified legal and data-protection specialists.

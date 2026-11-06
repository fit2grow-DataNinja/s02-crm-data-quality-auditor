# S02 — CRM Data Quality & Freshness Auditor

Status: **Working synthetic-data MVP; commercial and production validation pending** | Reviewed: 2026-10-26

## Business purpose
Audit exported CRM contact and deal records using deterministic data-quality rules; use AI to explain results, not calculate findings.

## Inputs and outputs
Required: `contacts.csv`, `deals.csv`. The FastAPI `/audit` endpoint also supports optional `associations` input; the Open WebUI Workspace Tool adapter forwards optional associations when supplied. Output: ZIP containing `summary.json`, `issues.csv`, `report.md`. The chat adapter reads summary and Markdown report and returns text, not a downloadable ZIP.

## Verified milestone
Synthetic sample: 202 contacts, 121 deals, 92 medium-severity missing-deal-owner findings (`CRM-DEAL-OWNER-MISSING`). Other checks remain limited by missing exports and incomplete freshness/reconciliation data. Business owner-assignment policy is provisional.

## Not yet verified
Customer demand, pricing, operational readiness, customer-data safety, SEC-001, deployment portability, and full freshness checks.

## Shared-core checkpoint
Initial review due at this verified S02 milestone. Keep adapter and audit rules local for now: no second service has demonstrated reusable code. Revisit `ai-services-core` at every future verified solution milestone, following portfolio governance.

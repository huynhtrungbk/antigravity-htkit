---
name: feature-analysis
description: Analyze features from 15 perspectives (Frontend, Backend, DB, UI/UX, Security, Integration, Testing, Performance, DevOps). Use for feature audits, pre-launch reviews, gap analysis, tech debt assessment.
version: 1.0.0
---

# Feature Analysis

Comprehensive feature analysis from Developer, Tester, PM, and Designer perspectives.
Each analysis produces findings in `docs/features/<feature-slug>/` — updated continuously.

## When to Use

- Analyzing new or existing features for completeness
- Pre-launch / pre-deployment reviews
- Gap analysis, tech debt assessment, migration planning
- Post-incident root cause analysis

## Analysis Workflow

```
1. SCOPE    → Define feature boundary + entry points
2. DISCOVER → Map all components (files, routes, tables, APIs)
3. ANALYZE  → Run each dimension checklist (see table below)
4. CLASSIFY → 🔴 Critical / 🟡 Major / 🟢 Minor
5. REPORT   → Write to docs/features/<feature-slug>/
```

### Step 1: Scope

Identify: feature name, entry points (pages, CLI, APIs), data entities (DB tables), external deps, user roles.

### Step 2: Discover

Map ALL files using grep/search, organized by layer:
- Frontend: pages, components, API routes, hooks
- Backend: controllers, services, workers, middleware
- Database: tables, migrations, seeds
- Config: env vars, Docker, CI/CD

### Step 3: Analyze — 15 Dimensions × 4 Perspectives

| # | Dimension | Reference | Perspective |
|---|-----------|-----------|-------------|
| 1 | Pages, Routes, Components | `references/frontend-checklist.md` | Developer |
| 2 | State, Polling, Forms | `references/frontend-checklist.md` | Developer |
| 3 | API Endpoints, Validation | `references/backend-checklist.md` | Developer |
| 4 | Business Logic, Error Handling | `references/backend-checklist.md` | Developer |
| 5 | Schema, Indexes, Integrity | `references/database-checklist.md` | DBA |
| 6 | Migrations, Missing Fields | `references/database-checklist.md` | DBA |
| 7 | User Flow, Navigation | `references/ui-ux-checklist.md` | Designer |
| 8 | Feedback, Error Recovery, A11y | `references/ui-ux-checklist.md` | Designer |
| 9 | Data Flow, Service Contracts | `references/integration-checklist.md` | Architect |
| 10 | Auth, Input Attack Surface | `references/security-checklist.md` | Security |
| 11 | Test Coverage, Edge Cases | `references/testing-monitoring.md` | QA |
| 12 | Observability, Health Checks | `references/testing-monitoring.md` | SRE |
| 13 | Load, Caching, Scaling | `references/performance-devops.md` | DevOps |
| 14 | Code Quality, Tech Debt | `references/maintainability.md` | Tech Lead |
| 15 | Anti-patterns (cross-cutting) | `references/antipatterns.md` | All |

### Step 4: Classify Findings

| Level | Criteria | Action |
|-------|----------|--------|
| 🔴 Critical | Blocks usage, data loss, security breach | Fix immediately |
| 🟡 Major | Degrades experience, missing functionality | Fix before release |
| 🟢 Minor | Cosmetic, nice-to-have, optimization | Next sprint |

### Step 5: Write Report

Output to `docs/features/<feature-slug>/` — see `references/report-template.md`

```
docs/features/
├── <feature-slug>/
│   ├── analysis-report.md    ← Full analysis (all 15 dimensions)
│   ├── findings.md           ← Issue table: ID, severity, description, effort
│   ├── roadmap.md            ← Fix phases: Unblock → UX → Security → Polish
│   └── changelog.md          ← Updates log (date, what changed, status)
```

## Updating Existing Analyses

When a feature evolves:
1. Re-run relevant dimension checklists on changed files
2. Update `analysis-report.md` with new findings
3. Update `findings.md` — mark fixed items ✅, add new items
4. Update `roadmap.md` phases if priorities shifted
5. Append entry to `changelog.md` with date + summary

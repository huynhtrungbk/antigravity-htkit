# Report Template

Output structure for feature analysis. Place in `docs/features/<feature-slug>/`.

## Directory Structure

```
docs/features/<feature-slug>/
├── analysis-report.md    ← Full 15-dimension analysis
├── findings.md           ← All issues in priority table
├── roadmap.md            ← Fix phases with effort estimates
└── changelog.md          ← Updates log over time
```

## analysis-report.md Template

```markdown
# <Feature Name> — Analysis Report
**Date:** YYYY-MM-DD | **Version:** X.X | **Analyst:** Agent

## Scope
- **Feature:** [description]
- **Entry Points:** [pages, APIs, CLI]
- **Data Entities:** [tables, models]
- **External Deps:** [services, APIs]

## Architecture Overview
[Diagram or text describing component interactions]

## Analysis by Dimension
### 1. Frontend  → [findings with file:line references]
### 2. Backend   → [findings with file:line references]
### 3. Database  → [findings with file:line references]
### ...
### 15. Anti-Patterns → [cross-cutting findings]

## Summary
| Severity | Count |
|----------|-------|
| 🔴 Critical | X |
| 🟡 Major | X |
| 🟢 Minor | X |
```

## findings.md Template

```markdown
# <Feature Name> — Findings

| ID | Severity | Dimension | Description | File | Effort | Status |
|----|----------|-----------|-------------|------|--------|--------|
| F1 | 🔴 | Frontend | Missing status polling | page.js:45 | 2h | [ ] |
| B1 | 🟡 | Backend | No auth on API | app.py:120 | 1h | [ ] |
| D1 | 🟡 | Database | Missing recipe_id column | videos | 30m | [x] |
```

Status values: `[ ]` open, `[/]` in progress, `[x]` fixed, `[-]` won't fix

## roadmap.md Template

```markdown
# <Feature Name> — Fix Roadmap

## Phase 1: Unblock (Critical)
| ID | Fix | Effort | Dependencies |
|----|-----|--------|--------------|
| F1 | Add status polling | 2h | None |
| I1 | Fix hostname mismatch | 5m | None |

## Phase 2: Core UX (Major)
...

## Phase 3: Security (Major)
...

## Phase 4: Polish (Minor)
...

**Total Estimated Effort:** Xh
```

## changelog.md Template

```markdown
# <Feature Name> — Changelog

## YYYY-MM-DD — Initial Analysis
- Analyzed from 15 dimensions
- Found X critical, Y major, Z minor issues
- Created roadmap with 4 phases

## YYYY-MM-DD — Phase 1 Complete
- Fixed I1: hostname mismatch (12 files)
- Fixed D1-D4: added pipeline tracking columns
- Updated findings.md: 4 items marked ✅
```

## Naming Convention

Feature slug: lowercase, kebab-case derived from feature name.
- "Video Pipeline" → `video-pipeline`
- "User Authentication" → `user-authentication`
- "Payment Integration" → `payment-integration`

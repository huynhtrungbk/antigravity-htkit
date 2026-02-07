# Development Rules

## General Principles

- **YAGNI** (You Aren't Gonna Need It)
- **KISS** (Keep It Simple, Stupid)
- **DRY** (Don't Repeat Yourself)
- File naming: **kebab-case** with descriptive names
- Keep code files **under 200 lines** — split into modules when exceeded
- Always implement real code — never mock or simulate

## Documentation Rules

All analysis, plans, and reports are saved in `./docs/` with numbered naming:

**Format:** `XX-Type-Name-YYYY-MM-DD.md`

| Type | When |
|------|------|
| `Analysis` | Before creating any plan |
| `Plan` | Before any implementation |
| `Report` | After completing work |

**Examples:**
- `11-Analysis-Kit-Evaluation-2026-02-07.md`
- `12-Plan-Kit-Slim-Down-2026-02-07.md`
- `13-Report-Kit-Slim-Down-2026-02-07.md`

**Rules:**
- Number sequentially from the last doc in `./docs/`
- Every doc must have a date
- Before planning → save analysis doc first
- Before implementing → save plan doc first
- After completing → save report doc

## Approval & Execution Flow

```
Analysis → Plan → USER APPROVAL → Execute all phases → Report
```

- **All plans require user approval** before implementation
- After approval, **execute all phases continuously** without stopping
- Only pause mid-execution if encountering errors or needing user decisions
- Exception: if user says "tự triển khai" → skip approval, execute immediately

## Code Quality

- Read and follow codebase structure in `./docs`
- No syntax errors — code must compile
- Prioritize functionality and readability
- Use try-catch error handling
- Handle edge cases

## Code Implementation

- Update existing files directly — do NOT create "enhanced" copies
- After modifying code, run compile/build to verify
- Do NOT open code files for user review — only open analysis/plan/report docs
- Use `docs-seeker` skill for latest library documentation when needed

## Pre-commit Rules

- Run linting before commit
- Run tests before push
- Never commit credentials, .env files, or API keys
- Use conventional commit format

## Project Identity

| Key | Value |
|-----|-------|
| **Kit** | Antigravity-HTKit v1.1.0 |
| **Admin** | [@huynhtrungbk](https://github.com/huynhtrungbk) |
| **Timezone** | Asia/Ho_Chi_Minh (GMT+7) |
| **Language** | Vietnamese (vi) preferred |
| **Config** | `.agent/.ht.json` |

## Commit Conventions

Use `ht:` prefix for kit-related changes:

```
ht-feat: add new skill
ht-fix: fix search script
ht-docs: update documentation
feat: application feature (non-kit)
fix: application bugfix (non-kit)
```
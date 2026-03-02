# Maintainability Checklist

## Code Organization
- [ ] Feature code grouped logically (by feature, not by type)
- [ ] Clear separation of concerns (UI / business logic / data access)
- [ ] Shared utilities in `/lib`, `/utils`, or `/helpers` (not duplicated)
- [ ] Constants extracted to named vars (no magic numbers/strings)
- [ ] File naming follows project convention (kebab-case, PascalCase, etc.)

## File Size & Modularity
- [ ] No file exceeds 200 lines (split into modules if larger)
- [ ] Each function has single responsibility
- [ ] Long functions (>50 lines) broken into named sub-functions
- [ ] Complex conditionals extracted to named boolean variables
- [ ] Deeply nested code (>3 levels) refactored

## Naming & Readability
- [ ] Variable/function names describe purpose (not abbreviated)
- [ ] Boolean variables start with is/has/can/should
- [ ] Functions named as verb+noun (createUser, fetchVideos)
- [ ] No commented-out code in production (use version control)
- [ ] TODO/FIXME/HACK comments tracked and scheduled for cleanup

## Dependency Management
- [ ] Dependencies version-pinned (exact or lock file)
- [ ] No unused dependencies (audit and remove)
- [ ] No duplicate dependencies (check for overlapping functionality)
- [ ] Security vulnerabilities scanned (npm audit, pip audit)
- [ ] License compatibility verified for all dependencies

## Configuration Management
- [ ] All environment-specific values in env vars (12-factor app)
- [ ] Default values are safe for production (fail-closed)
- [ ] Config schema documented (.env.example)
- [ ] Secret rotation possible without code deploy
- [ ] Feature flags externalized (not hardcoded booleans)

## Error Handling Consistency
- [ ] Error handling pattern consistent across codebase
- [ ] Custom error classes for domain-specific errors
- [ ] Error boundaries at UI component level (React error boundaries)
- [ ] Global error handler for unhandled exceptions
- [ ] Errors logged before being swallowed or transformed

## Documentation
- [ ] README updated with feature description
- [ ] API endpoints documented (OpenAPI/Swagger or markdown)
- [ ] Architecture decisions documented (ADRs or architecture docs)
- [ ] Complex business logic explained in code comments or docs
- [ ] Setup instructions updated if new env vars or services added
- [ ] Changelog maintained for significant changes

## Technical Debt Tracking
- [ ] Known shortcuts documented as TODO with issue/ticket reference
- [ ] Technical debt items prioritized (not just accumulated)
- [ ] Refactoring candidates identified (duplicated code, outdated patterns)
- [ ] Dead code removed (unused functions, unreachable branches)
- [ ] Deprecated APIs identified with migration plan

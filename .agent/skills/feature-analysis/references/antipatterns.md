# Common Anti-Patterns

Cross-cutting bug patterns that repeat across projects. Check during every analysis.

## Architecture Anti-Patterns

### 1. Dual Orchestrator
**Pattern:** Two systems process the same entity (e.g., worker polling DB + HTTP trigger running in-memory).
**Symptom:** Race conditions, duplicate processing, inconsistent state.
**Fix:** Single source of truth for job assignment. Use DB status + row locking or Redis queue.

### 2. In-Memory State for Persistent Data
**Pattern:** Storing job status, sessions, or queues in Python dicts / Node.js variables.
**Symptom:** Data lost on restart, invisible to other processes, no audit trail.
**Fix:** Persist to DB or Redis. In-memory only for ephemeral cache with TTL.

### 3. Hostname Mismatch
**Pattern:** Code references service by wrong name (differs from Docker Compose service name).
**Symptom:** Connection refused, DNS resolution failure inside container network.
**Fix:** Centralize service URLs in env vars. Grep ALL files for hardcoded hostnames.

## Frontend Anti-Patterns

### 4. Ghost Navigation
**Pattern:** Sidebar/navbar links to routes that have no corresponding page.
**Symptom:** User clicks link → blank page or 404.
**Fix:** Audit every nav link against actual page files. Remove or stub missing pages.

### 5. Fire-and-Forget Triggers
**Pattern:** UI triggers long-running operation but never polls for result.
**Symptom:** User clicks "Generate" → spinner → nothing happens. No status feedback.
**Fix:** Return job ID, poll `/status/{jobId}` every N seconds, show progress.

### 6. Hardcoded Display Data
**Pattern:** UI shows static mock values instead of dynamic data from API.
**Symptom:** Dashboard shows $127.50 forever regardless of actual data.
**Fix:** Bind all display values to API responses. Use skeleton loaders while loading.

## Backend Anti-Patterns

### 7. Unprotected Internal APIs
**Pattern:** "Internal" service API has no auth because "only frontend calls it."
**Symptom:** Anyone who discovers the URL can access, modify, or delete data.
**Fix:** API key middleware, JWT validation, or network-level restriction (Docker internal).

### 8. Path Traversal Acceptance
**Pattern:** API accepts file paths from user input without sanitization.
**Symptom:** Attacker reads arbitrary files: `/api/file?path=../../etc/passwd`.
**Fix:** Validate against whitelist, use `os.path.basename()`, restrict to known directories.

### 9. Swallowed Errors
**Pattern:** Try-catch blocks that catch and ignore errors silently.
**Symptom:** Operations fail but user sees success. Debugging is impossible.
**Fix:** Always log errors with context. Transform internal errors to user-facing messages.

## Data Anti-Patterns

### 10. Missing Tracking Columns
**Pattern:** Table tracks entity but misses key metadata (who, when, why, error).
**Symptom:** Can't debug failures, can't measure performance, can't audit changes.
**Fix:** Add: `created_at`, `updated_at`, `created_by`, `error_message`, `processing_started_at`.

### 11. File Path vs URL Confusion
**Pattern:** Backend saves file as local path (`/data/output/video.mp4`), frontend needs URL.
**Symptom:** Frontend can't display files — wrong protocol, path inaccessible over HTTP.
**Fix:** Serve files via static file server or object storage. Store URLs in DB, not local paths.

### 12. No Idempotent Migrations
**Pattern:** Migration fails halfway, re-running creates duplicates or errors.
**Symptom:** `column already exists` errors, partial schema state.
**Fix:** Use `IF NOT EXISTS`, `IF EXISTS` in all DDL statements.

## Process Anti-Patterns

### 13. No Retry Point
**Pattern:** Pipeline with N steps fails at step K. No way to restart from step K.
**Symptom:** 80% of work wasted on failure. User must start over entirely.
**Fix:** Persist step progress. Allow retry from last successful step.

### 14. Inconsistent Health Checks
**Pattern:** Docker HEALTHCHECK uses wrong type (CMD for HTTP service or vice versa).
**Symptom:** Container marked unhealthy despite service working fine.
**Fix:** Match health check type to service type. Test manually before deploying.

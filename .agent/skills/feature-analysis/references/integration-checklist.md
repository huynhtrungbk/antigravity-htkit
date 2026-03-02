# Integration & Data Flow Checklist

## Request Lifecycle (Trace Each Flow)
- [ ] Trace: UI action → frontend API route → backend endpoint → DB → response → UI update
- [ ] Each layer transforms data correctly (snake_case ↔ camelCase, JSON parse)
- [ ] Response contains all fields frontend needs (no missing data)
- [ ] Error propagation: Backend error → frontend API → UI error message (no swallowing)
- [ ] HTTP status codes match semantics (not always 200 with error in body)

## Service Communication
- [ ] Container hostnames in code match Docker Compose service names
- [ ] Network: All communicating services on same Docker network
- [ ] Port mapping: Internal port in code matches container exposed port
- [ ] Environment variables for all service URLs (not hardcoded)
- [ ] Fallback behavior when upstream service is unavailable
- [ ] Timeout configured for inter-service HTTP calls

## API Contract Alignment
- [ ] Frontend API route method matches backend expectation (POST vs PUT)
- [ ] Request body schema matches backend validation
- [ ] URL path params match between proxy route and backend endpoint
- [ ] Query params forwarded correctly through proxy
- [ ] Headers forwarded (auth, content-type, accept)
- [ ] Multipart/form-data handled for file uploads through proxy

## Dual/Multiple System Conflicts
- [ ] No two components processing same entity concurrently (race condition)
- [ ] If multiple consumers: coordination via locks, queues, or ownership assignment
- [ ] Job deduplication: Same job not picked up by two workers
- [ ] Status transitions have defined ownership (who sets each status)
- [ ] Source of truth defined (DB vs in-memory vs cache)

## File & Asset Flow
- [ ] Files saved by backend accessible from frontend (URL mapping)
- [ ] File paths in DB are either: relative paths with known base, or full URLs
- [ ] Static asset serving configured (nginx, CDN, object storage)
- [ ] File cleanup: Temp files deleted after processing
- [ ] File size limits consistent across all layers (frontend, proxy, backend)

## Event & Queue Integration
- [ ] Queue consumer matches producer message format
- [ ] Dead letter queue for failed messages
- [ ] Idempotent message processing (re-delivery safe)
- [ ] Message ordering preserved where required
- [ ] Queue health monitored (depth, processing rate)

## Cache Consistency
- [ ] Cache invalidation on write operations
- [ ] TTL appropriate for data volatility
- [ ] Cache key includes all relevant parameters
- [ ] Stale cache doesn't serve incorrect data after mutations
- [ ] No caching of user-specific data in shared cache

## Third-Party API Integration
- [ ] API keys stored securely (env vars, not code)
- [ ] Rate limits respected (backoff/retry logic)
- [ ] API response validated before processing
- [ ] Webhook signatures verified (if receiving webhooks)
- [ ] API version pinned (not "latest")
- [ ] Usage/cost tracked and logged

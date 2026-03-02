# Backend Analysis Checklist

## API Endpoints
- [ ] All endpoints documented (method, path, request/response schema)
- [ ] Consistent naming convention (RESTful: `/resources`, `/resources/{id}`)
- [ ] Proper HTTP methods (GET=read, POST=create, PUT=update, DELETE=remove)
- [ ] Correct status codes (200, 201, 400, 401, 403, 404, 500)
- [ ] Pagination implemented for list endpoints (`?page=1&limit=50`)
- [ ] Filtering/sorting supported where applicable
- [ ] Consistent error response format (`{ error: string, details?: any }`)

## Authentication & Authorization
- [ ] All mutable endpoints require authentication
- [ ] Auth middleware applied at router level (not per-endpoint)
- [ ] Role-based access control (RBAC) enforced where needed
- [ ] API keys or tokens validated on every request
- [ ] Session expiry handled (token refresh or re-login)
- [ ] Admin-only endpoints protected separately
- [ ] Multi-tenant isolation (user can only access their org's data)

## Input Validation
- [ ] All request body fields validated (type, length, format)
- [ ] Path params validated (integer IDs, valid UUIDs)
- [ ] Query params validated (max page size, valid sort fields)
- [ ] File uploads validated (type, size, content)
- [ ] SQL injection protection (parameterized queries, no string concat)
- [ ] XSS prevention (output encoding, Content-Security-Policy header)
- [ ] No raw file paths accepted from user input (path traversal)

## Business Logic
- [ ] Idempotent operations where applicable (retryable without side effects)
- [ ] Race conditions handled (optimistic locking, unique constraints)
- [ ] Concurrent access managed (DB transactions, row-level locks)
- [ ] Domain constraints enforced at service layer (not just DB)
- [ ] Edge cases: empty input, max values, null/undefined, zero
- [ ] Circular dependencies checked between services

## Error Handling
- [ ] Try-catch at controller level (no unhandled promise rejections)
- [ ] Errors logged with context (request ID, user ID, stack trace)
- [ ] Internal errors masked from user (no stack traces in response)
- [ ] Specific error messages for known failure modes
- [ ] Retry logic for transient failures (network, rate limits)
- [ ] Circuit breaker for external service calls

## External Service Integration
- [ ] Timeout configured for all external HTTP calls
- [ ] Fallback behavior when external service unavailable
- [ ] Rate limiting on outgoing requests (respect API quotas)
- [ ] Response validation from external services
- [ ] Credentials stored securely (env vars, not hardcoded)
- [ ] Health check includes external dependency status

## Configuration
- [ ] All config via environment variables (12-factor app)
- [ ] No hardcoded URLs, ports, credentials, or magic numbers
- [ ] Different configs for dev/staging/production
- [ ] Defaults are safe and documented
- [ ] Secrets not logged or exposed in error messages

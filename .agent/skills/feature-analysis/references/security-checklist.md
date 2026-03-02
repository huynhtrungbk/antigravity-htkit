# Security Analysis Checklist

## Authentication
- [ ] All mutable endpoints require authentication
- [ ] Auth middleware applied at router/group level (not per-endpoint copy-paste)
- [ ] Session expiry and token refresh handled
- [ ] Logout invalidates session/token server-side
- [ ] Password stored with Argon2id/bcrypt (never plaintext/MD5/SHA)
- [ ] Password reset flow uses time-limited tokens
- [ ] Multi-factor authentication (MFA) available for admin accounts

## Authorization
- [ ] Role-based access control (RBAC) enforced
- [ ] Users can only access their own data (tenant isolation)
- [ ] Admin-only endpoints have separate permission checks
- [ ] API key scopes restrict access to specific resources
- [ ] No privilege escalation paths (regular user → admin via API manipulation)
- [ ] Object-level authorization checked (user A can't access user B's resource by ID)

## Input Validation & Injection Prevention
- [ ] SQL injection: Parameterized queries everywhere (no string concatenation)
- [ ] XSS: Output encoding for user-generated content in HTML
- [ ] Path traversal: No raw file paths accepted from user input
- [ ] Command injection: No `exec()` or `system()` with user input
- [ ] SSRF: Internal URLs not reachable via user-controlled URL params
- [ ] JSON injection: Request body parsed safely, no prototype pollution
- [ ] File upload: Type validation (not just extension), size limits, virus scan

## API Security
- [ ] Rate limiting on authentication endpoints (login, register, password reset)
- [ ] Rate limiting on expensive operations (AI generation, file processing)
- [ ] CORS configured to allow only known origins (not `*` in production)
- [ ] CSRF protection on state-changing requests (POST, PUT, DELETE)
- [ ] Security headers set: CSP, X-Frame-Options, X-Content-Type-Options
- [ ] API versioning prevents breaking changes from affecting clients

## Data Protection
- [ ] Sensitive data encrypted at rest (PII, financial data)
- [ ] HTTPS enforced for all external communication
- [ ] Internal service communication uses TLS or trusted network
- [ ] Minimal data exposure in API responses (no password hashes, internal IDs)
- [ ] Logs do not contain secrets, tokens, passwords, or full credit card numbers
- [ ] PII data has retention policy and deletion capability (GDPR compliance)

## Secrets Management
- [ ] API keys, passwords, tokens in environment variables (not in code)
- [ ] No secrets in git history (use git-secrets or pre-commit hooks)
- [ ] Secrets not logged in error messages or debug output
- [ ] Secrets rotated periodically (key rotation strategy)
- [ ] Different secrets for dev/staging/production environments
- [ ] `.env` file in `.gitignore`

## Infrastructure Security
- [ ] Default credentials changed (DB, admin panels, dashboards)
- [ ] Unused ports not exposed (Docker: only expose necessary ports)
- [ ] Container runs as non-root user
- [ ] Dependencies scanned for known vulnerabilities (npm audit, pip audit)
- [ ] SSH access uses key-based auth (not password)
- [ ] Firewall rules restrict access to management ports

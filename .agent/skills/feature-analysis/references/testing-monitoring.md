# Testing & Monitoring Checklist

## Unit Testing
- [ ] Business logic functions have unit tests
- [ ] Edge cases tested: null, empty, max values, negative, unicode
- [ ] Error paths tested (exceptions, invalid input)
- [ ] Mocks used for external dependencies (DB, APIs, file system)
- [ ] Test names describe behavior, not implementation
- [ ] Coverage target: ≥70% for critical paths

## Integration Testing
- [ ] API endpoints tested end-to-end (request → response)
- [ ] Database operations tested with real DB (test container or in-memory)
- [ ] Auth flows tested (login, logout, token refresh, expired token)
- [ ] Inter-service communication tested (service A → service B)
- [ ] File upload/download flows tested
- [ ] Error responses verified (correct status codes, error messages)

## E2E Testing
- [ ] Critical user flows covered (Playwright, Cypress, or Selenium)
- [ ] Happy path: Create → List → View → Edit → Delete
- [ ] Form validation errors shown correctly
- [ ] Navigation works (all sidebar links, breadcrumbs)
- [ ] Responsive tested (mobile viewport)
- [ ] Cross-browser tested (Chrome, Firefox, Safari) for production apps

## Test Infrastructure
- [ ] Tests run in CI/CD pipeline (PR checks)
- [ ] Test database isolated from production
- [ ] Test data seeded consistently (fixtures or factories)
- [ ] Flaky tests identified and fixed (not just retried)
- [ ] Test execution time reasonable (<5 min for unit, <15 min for E2E)

## Health Checks
- [ ] Each service exposes `/health` endpoint
- [ ] Health check verifies actual dependencies (DB connection, upstream services)
- [ ] Docker health check type matches endpoint type (HTTP for web, CMD for workers)
- [ ] Health check interval/timeout/retries configured appropriately
- [ ] Unhealthy containers auto-restart via Docker or orchestrator

## Logging
- [ ] Structured logging (JSON format for machine parsing)
- [ ] Log levels used correctly (ERROR, WARN, INFO, DEBUG)
- [ ] Request context included (request ID, user ID, timestamp)
- [ ] Error logs include stack trace and relevant context
- [ ] No sensitive data in logs (passwords, tokens, PII)
- [ ] Logs persisted centrally (not just container stdout)
- [ ] Log rotation configured (prevent disk full)

## Metrics & Alerting
- [ ] Request rate, error rate, response time tracked
- [ ] Queue depth and processing rate monitored
- [ ] Resource usage tracked (CPU, memory, disk)
- [ ] Business metrics tracked (videos generated, success rate)
- [ ] Alerts configured for: error rate spike, service down, disk full
- [ ] Alert notification channel (email, Slack, PagerDuty)
- [ ] Dashboards available for real-time monitoring

## Cost Tracking
- [ ] External API usage logged (OpenAI, cloud services)
- [ ] Cost per operation calculable from logs/metrics
- [ ] Budget alerts configured for cloud spending
- [ ] Usage patterns analyzed for optimization opportunities

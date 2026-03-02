# Performance & DevOps Checklist

## Query & Backend Performance
- [ ] Slow queries identified (>100ms) and optimized (EXPLAIN ANALYZE)
- [ ] N+1 queries eliminated (use JOINs, batch loading, eager loading)
- [ ] Connection pooling configured (not per-request connections)
- [ ] Heavy computations offloaded to background workers
- [ ] Result pagination for list endpoints (not returning all records)
- [ ] Response payload minimized (select only needed columns)

## Caching
- [ ] Frequently read, rarely changed data cached (Redis, in-memory)
- [ ] Cache TTL appropriate for data type
- [ ] Cache invalidation on write operations
- [ ] Cache key includes all variants (user, locale, params)
- [ ] No caching of user-specific data in shared cache
- [ ] Cache hit rate monitored

## Frontend Performance
- [ ] Bundle size analyzed (no unnecessary large dependencies)
- [ ] Images optimized (WebP, lazy loading, proper dimensions)
- [ ] Code splitting / lazy loading for routes
- [ ] Static assets served via CDN or reverse proxy
- [ ] API calls debounced/throttled where appropriate
- [ ] Rendering performance checked (no unnecessary re-renders)

## Scalability
- [ ] Stateless services (horizontal scaling ready)
- [ ] Session state externalized (Redis, DB — not in-memory)
- [ ] File storage on shared volume or object storage (not local disk)
- [ ] Database can handle expected load (connection limits, read replicas)
- [ ] Queue-based processing for spiky workloads
- [ ] Auto-scaling configured (if cloud-hosted)

## Docker & Containerization
- [ ] Multi-stage builds (small final image)
- [ ] `.dockerignore` configured (no node_modules, .git in image)
- [ ] Non-root user in container
- [ ] Resource limits set (CPU, memory)
- [ ] Volumes for persistent data (not lost on container restart)
- [ ] Restart policy configured (`unless-stopped` or `always`)
- [ ] Container logs accessible and rotated

## Deployment
- [ ] Zero-downtime deployment strategy (rolling, blue-green, canary)
- [ ] Rollback plan documented and tested
- [ ] Database migrations run before new code deploys
- [ ] Feature flags for gradual rollout of new features
- [ ] Deployment checklist documented
- [ ] Environment parity (dev ≈ staging ≈ production)

## CI/CD Pipeline
- [ ] Automated build on push/PR
- [ ] Linting and type checking in pipeline
- [ ] Tests run in pipeline (unit + integration)
- [ ] Security scanning (dependency audit, SAST)
- [ ] Docker image built and pushed automatically
- [ ] Deployment triggered automatically or via approval gate

## Backup & Disaster Recovery
- [ ] Database backups automated (daily minimum)
- [ ] Backup restoration tested periodically
- [ ] Point-in-time recovery possible (WAL archiving for PostgreSQL)
- [ ] File/asset backups automated
- [ ] Recovery time objective (RTO) and recovery point objective (RPO) defined
- [ ] Incident response runbook documented

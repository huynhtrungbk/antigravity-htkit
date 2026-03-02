# Database Analysis Checklist

## Schema Design
- [ ] All entities have corresponding tables
- [ ] Column names follow consistent convention (snake_case)
- [ ] Data types appropriate (TEXT vs VARCHAR, TIMESTAMPTZ vs TIMESTAMP)
- [ ] ENUM columns use CHECK constraints or separate lookup tables
- [ ] JSON/JSONB columns documented with expected structure
- [ ] Soft-delete supported where needed (`deleted_at` column)

## Relationships & Foreign Keys
- [ ] FK constraints defined for all relationships
- [ ] ON DELETE behavior specified (CASCADE, SET NULL, RESTRICT)
- [ ] Many-to-many relationships use junction tables
- [ ] No orphaned records possible (FK integrity)
- [ ] Self-referencing relationships handled correctly (parent_id)

## Missing Columns (Common Gaps)
- [ ] `created_at` / `updated_at` on all tables
- [ ] `created_by` / `updated_by` for audit trail
- [ ] Status tracking: `status` column with defined enum values
- [ ] Error tracking: `error_message` for failed operations
- [ ] Processing tracking: `started_at` / `completed_at` timestamps
- [ ] Linking columns: FK to related features (e.g., `recipe_id`, `job_id`)
- [ ] Soft-delete: `deleted_at` if records shouldn't be hard-deleted

## Indexes
- [ ] Primary keys on all tables (auto-generated UUID or SERIAL)
- [ ] Indexes on FK columns (foreign keys)
- [ ] Indexes on frequently filtered columns (status, created_at)
- [ ] Composite indexes for multi-column queries
- [ ] Partial indexes for status-specific queries (`WHERE status = 'active'`)
- [ ] No duplicate or redundant indexes
- [ ] Index usage verified with EXPLAIN ANALYZE

## Data Integrity
- [ ] NOT NULL constraints on required fields
- [ ] UNIQUE constraints on natural keys (email, slug)
- [ ] CHECK constraints for value ranges (price > 0, status IN (...))
- [ ] DEFAULT values for optional fields
- [ ] Trigger-based validation for complex rules (if needed)

## Migrations
- [ ] Migrations use `IF NOT EXISTS` / `IF EXISTS` for idempotency
- [ ] Backward compatible (old code works with new schema during deploy)
- [ ] Rollback migration provided or reversible
- [ ] Large table migrations tested for lock time
- [ ] Data backfill script included for new required columns
- [ ] Migration numbered/ordered correctly

## Query Patterns
- [ ] N+1 query problem avoided (use JOINs or batch loading)
- [ ] Large result sets paginated (LIMIT/OFFSET or cursor)
- [ ] COUNT queries use indexes (not full table scan)
- [ ] Bulk operations use batch inserts/updates (not loops)
- [ ] Connection pooling configured (not per-request connections)

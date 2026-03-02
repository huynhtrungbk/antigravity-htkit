# Frontend Analysis Checklist

## Components & Pages
- [ ] All routes in navigation have corresponding page files
- [ ] No dead links in sidebar/navbar (route exists but page missing)
- [ ] Route params handled correctly (`[id]`, `[slug]` etc.)
- [ ] 404 / error pages implemented for invalid routes
- [ ] Breadcrumb navigation reflects actual page hierarchy

## State Management
- [ ] Server state vs client state clearly separated
- [ ] Loading states shown during async operations
- [ ] Error states handled gracefully (not blank screens)
- [ ] Empty states designed (no data → show message/CTA)
- [ ] Stale data handled (auto-refresh or manual refresh)
- [ ] Form state preserved on navigation (unsaved changes warning)
- [ ] URL state sync (filters, pagination, search → query params)

## API Integration
- [ ] All frontend API routes proxy to correct backend hostname
- [ ] Environment variables used for backend URLs (not hardcoded)
- [ ] Fallback behavior when backend unavailable
- [ ] Request timeout configured (not infinite waiting)
- [ ] Error responses parsed and shown to user meaningfully
- [ ] Auth tokens passed to backend where required
- [ ] Response data mapped correctly (snake_case → camelCase)

## Real-Time & Polling
- [ ] Long-running operations poll status endpoint
- [ ] Polling interval reasonable (not too frequent, not too slow)
- [ ] Polling stops on completion, error, or page navigation
- [ ] Progress indicators show actual step (not just spinning)
- [ ] Websocket/SSE used where real-time is critical

## File & Media Handling
- [ ] File upload progress shown
- [ ] File size limits enforced client-side before upload
- [ ] Media files (images, video, audio) have proper serving URLs
- [ ] Thumbnails generated for media previews
- [ ] Download links functional and use correct MIME types

## Form & Input
- [ ] Required fields validated before submit
- [ ] Validation messages clear and positioned near invalid field
- [ ] Submit button disabled during submission (prevent double-submit)
- [ ] Success/error feedback after submission
- [ ] Form reset works correctly

## Code Quality
- [ ] No inline styles (use CSS modules, styled-components, or Tailwind)
- [ ] Component files < 200 lines (modularize if larger)
- [ ] Shared UI components in `/components` (not duplicated)
- [ ] Constants extracted (no magic numbers in JSX)
- [ ] API base URLs centralized in config/env

## Responsive & Accessibility
- [ ] Mobile viewport tested (< 768px)
- [ ] Touch targets ≥ 44px on mobile
- [ ] Keyboard navigation works for all interactive elements
- [ ] Focus indicators visible
- [ ] aria-labels on icon-only buttons
- [ ] Color contrast ratio ≥ 4.5:1 for text

# UI/UX Analysis Checklist

## User Flow
- [ ] Primary task completable in ≤ 5 steps
- [ ] Entry point discoverable (sidebar link, button, URL)
- [ ] No dead-end pages (always possible to navigate away)
- [ ] Navigation labels match page content
- [ ] No duplicate entry points for same feature (confusing)
- [ ] Breadcrumb or back button available on nested pages
- [ ] Success flow ends with clear next action

## Feedback & Communication
- [ ] Loading state shown during async operations (spinner, skeleton, progress)
- [ ] Long-running tasks (>3s) show progress indicator with steps (not just spinner)
- [ ] Success confirmation after create/edit/delete actions
- [ ] Error messages are actionable (state problem + how to fix)
- [ ] Error messages positioned near the source (not just toast)
- [ ] Undo available for destructive actions (or confirmation dialog)
- [ ] Real-time status polling for background pipeline/queue tasks

## Error Recovery
- [ ] Form data preserved after validation error
- [ ] Partial failure allows retry from failure point (not restart)
- [ ] Session expiry redirects to login then returns to original page
- [ ] Network error shows retry button (not blank page)
- [ ] File upload failure doesn't lose selected files

## Empty & Edge States
- [ ] First-time/no-data state shows helpful message + CTA
- [ ] Zero results search shows "no results" message
- [ ] Max items reached shows limit message
- [ ] Slow connection shows degraded UI (not broken UI)
- [ ] Concurrent edit conflict handled (last-write-wins or merge)

## Visual Design Consistency
- [ ] Colors from design system (no ad-hoc hex values)
- [ ] Typography follows scale (h1 > h2 > h3, consistent body text)
- [ ] Spacing consistent (8px grid or design token system)
- [ ] Icon style consistent (outline vs filled, same library)
- [ ] Button hierarchy clear (primary, secondary, ghost)
- [ ] Cards/containers have consistent border-radius and shadows
- [ ] Dark/light mode supported and tested

## Responsive Design
- [ ] Desktop (>1024px) layout uses available space
- [ ] Tablet (768-1024px) adapts gracefully
- [ ] Mobile (<768px) content stacks vertically
- [ ] Tables convert to cards or scroll horizontally on mobile
- [ ] Navigation collapses to hamburger/bottom nav on mobile
- [ ] Touch targets ≥ 44px on mobile

## Accessibility (A11y)
- [ ] All interactive elements keyboard accessible (Tab, Enter, Escape)
- [ ] Focus indicators visible
- [ ] `aria-label` on icon-only buttons/links
- [ ] Color contrast ≥ 4.5:1 for normal text, ≥ 3:1 for large text
- [ ] Form inputs have associated `<label>` tags
- [ ] Dynamic content updates announced to screen readers
- [ ] No content dependent solely on color (use icons/text too)

## Content & Copy
- [ ] No placeholder text in production ("Lorem ipsum", "TODO")
- [ ] No hardcoded mock data in UI ($127.50 instead of dynamic value)
- [ ] Date/time formatted consistently and in user timezone
- [ ] Numbers formatted with locale (1,000 vs 1.000)
- [ ] Truncated text has tooltip or "show more"

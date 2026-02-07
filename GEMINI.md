# GEMINI.md

This file provides guidance to Antigravity when working with code in this repository.

---

## Overview

**Antigravity-HTKit** v1.1.1 — Full AI development & marketing toolkit with 59 skills. By [@huynhtrungbk](https://github.com/huynhtrungbk).

---

## Rules

- Follow development rules in `./.agent/rules/development-rules.md`
- Before planning or implementing, read `./README.md` first for context
- If a code file exceeds 200 lines, consider modularizing it
- Use kebab-case naming with descriptive names

---

## Skills (59)

| Category | Skills |
|----------|--------|
| **Design** | `ui-ux` (BM25 search, 50 styles, 21 palettes, 9 stacks), `ui-styling` (shadcn/Tailwind), `design-system` (token embed + slides), `frontend-design` (design-to-code), `web-design-guidelines` (UI audit), `threejs` (examples DB), `ai-artist` (image gen), `creativity` (creative briefs), `logo-design` (AI logo gen), `slides-design` (Chart.js presentations) |
| **Engineering** | `backend-development` (Node/Python/Go APIs), `frontend-development` (React/TypeScript), `databases` (backup/migrate/perf), `web-frameworks` (Next.js init), `web-testing` (Playwright), `debugging` (test polluter), `code-review` (scout-based), `git` (conventional commits), `better-auth` (OAuth/2FA/passkeys), `mcp-builder` (FastMCP servers), `google-adk-python` (AI agents), `remotion` (React video), `repomix` (repo packing), `research` (tech evaluation), `skill-creator` (create skills), `mermaidjs-v11` (diagrams) |
| **Payment** | `payment-integration` (SePay/Polar/Stripe/Paddle/Creem.io, multi-provider) |
| **AI/Media** | `ai-multimodal` (Gemini vision/image/video), `media-processing` (FFmpeg/ImageMagick/RMBG), `youtube-handling` (VidCap API), `copywriting` (conversion copy), `video-production` (video marketing) |
| **DevOps** | `devops` (Cloudflare/Docker/K8s/GCP), `chrome-devtools` (Puppeteer), `assets-organizing` (asset management) |
| **SEO/Content** | `seo-optimization` (ReviewWeb API + CWV), `docs-seeker` (context7), `brand-guidelines` (brand injection), `analytics` (GA4), `content-hub` (asset gallery), `content-marketing` (editorial strategy) |
| **Marketing** | `marketing-ideas` (140 strategies), `marketing-psychology` (70+ models), `marketing-planning` (RACE/SOSTAC), `marketing-research` (market analysis), `campaign-management` (multi-channel), `email-marketing` (drip/automation), `social-media` (X/FB/TikTok/LinkedIn/YT APIs), `paid-ads` (PPC campaigns), `ads-management` (Google/Meta/LinkedIn ads), `pricing-strategy` (SaaS tiers), `launch-strategy` (Product Hunt/GTM), `ab-test-setup` (experiment design), `affiliate-marketing` (KOL/KOC programs), `referral-program-building` (viral loops) |
| **Meta** | `context-engineering` (token analyzer), `sequential-thinking` (thought processor), `mcp-management` (MCP CLI), `plans-kanban` (kanban server) |

---

## Python Scripts

When running Python scripts from `.agent/skills/`, use:
- **macOS/Linux:** `python3 .agent/skills/<skill>/scripts/xxx.py`

---

**IMPORTANT:** *MUST READ* and *MUST COMPLY* all *INSTRUCTIONS* in this file.

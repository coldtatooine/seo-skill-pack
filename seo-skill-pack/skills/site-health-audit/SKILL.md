---
name: site-health-audit
description: This skill should be used when the user asks to "audit site health", "technical SEO audit", "Core Web Vitals audit", "crawl errors audit", "website health check", or wants a rapid technical assessment of a website's SEO health covering crawlability, indexing, speed, and on-page factors.
version: 1.0.0
---

# Site Health Quick Audit

Perform a rapid but thorough technical SEO health assessment. Cover crawlability, indexing, Core Web Vitals, on-page SEO, mobile experience, security, and common technical issues. Generate a prioritized fix list with clear instructions.

---

## Core Workflow

### Phase 1 — Quick Scan

Collect from the user:
1. **Website URL** (homepage)
2. **Known issues** (optional — any problems they're already aware of)
3. **CMS/platform** (optional — WordPress, Shopify, custom, etc.)

Perform initial checks using web tools and browsing:

1. Load the homepage — note load time, redirects, errors
2. Check `robots.txt` at `/robots.txt`
3. Check `sitemap.xml` at `/sitemap.xml` and `/sitemap_index.xml`
4. View page source for meta tags, schema, and critical elements
5. Check HTTPS implementation
6. Test mobile responsiveness

### Phase 2 — Crawlability & Indexing

| Check | How | Pass Criteria |
|-------|-----|---------------|
| robots.txt | Fetch /robots.txt | Exists, not blocking important pages |
| Sitemap | Fetch /sitemap.xml | Exists, valid XML, includes key pages |
| Canonical tags | View source | Present on all pages, self-referencing |
| Noindex tags | View source | Not on pages that should be indexed |
| Redirect chains | Follow redirects | Max 1 redirect hop, no loops |
| 404 pages | Check common paths | Custom 404, not soft 404 |
| URL structure | Browse site | Clean, descriptive, no parameters |
| Pagination | Check paginated sections | rel=prev/next or load-more pattern |
| Hreflang | View source (multilingual sites) | Correct language/region codes |
| JavaScript rendering | View source vs rendered | Critical content in initial HTML |

### Phase 3 — Core Web Vitals & Performance

Evaluate these metrics (use web search for PageSpeed data if available). Apply standard CWV thresholds: LCP ≤2.5s, INP ≤200ms, CLS ≤0.1, TTFB ≤800ms, FCP ≤1.8s — anything above 2× these values is Poor, between is Needs Improvement.

Common performance issues to check:
- Unoptimized images (no WebP/AVIF, missing dimensions, oversized)
- Render-blocking CSS/JS
- No lazy loading on below-fold images
- Missing font-display: swap
- No compression (gzip/brotli)
- No browser caching headers
- Excessive third-party scripts
- Large DOM size (>1500 nodes)

### Phase 4 — On-Page SEO Factors

Check on the homepage and 3-5 key pages:

| Element | Check | Best Practice |
|---------|-------|---------------|
| Title tag | Present, unique, <=60 chars | Keyword + brand |
| Meta description | Present, unique, <=155 chars | Compelling + CTA |
| H1 tag | Exactly one per page | Contains primary keyword |
| Heading hierarchy | Logical H1>H2>H3 | No skipped levels |
| Image alt text | Present on all images | Descriptive, not stuffed |
| Internal links | Key pages linked | Logical structure |
| External links | Relevant outbound links | Open in new tab, rel attributes |
| Content length | Sufficient for topic | Matches search intent |
| Keyword usage | Natural placement | Title, H1, first 100 words, body |
| Schema markup | Relevant types present | Valid JSON-LD |

### Phase 5 — Mobile & UX

| Check | Criteria |
|-------|----------|
| Responsive design | Renders correctly on mobile viewports |
| Touch targets | Buttons/links min 48x48px with 8px spacing |
| Font size | Min 16px body text |
| Viewport meta | `<meta name="viewport" content="width=device-width, initial-scale=1">` |
| No horizontal scroll | Content fits viewport width |
| Interstitials | No intrusive popups on mobile |
| Navigation | Accessible hamburger/slide menu |
| Form usability | Appropriate input types, autocomplete |

### Phase 6 — Security & Trust

| Check | Criteria |
|-------|----------|
| HTTPS | Valid SSL, no mixed content |
| HSTS | Strict-Transport-Security header |
| Security headers | X-Frame-Options, CSP, X-Content-Type-Options |
| Privacy page | /privacy or /privacy-policy exists |
| Terms page | /terms or /terms-of-service exists |
| Contact info | Visible, matches business records |
| Trust signals | Reviews, certifications, associations |

### Phase 7 — Health Report

Generate the report using `references/health-report-template.md`:

#### Health Score (0-100)

| Category | Weight | Score |
|----------|--------|-------|
| Crawlability & Indexing | 25% | /100 |
| Core Web Vitals | 25% | /100 |
| On-Page SEO | 20% | /100 |
| Mobile Experience | 15% | /100 |
| Security & Trust | 15% | /100 |
| **Overall Health Score** | 100% | **/100** |

#### Report Sections

1. **Health Score Dashboard** — visual score breakdown
2. **Critical Issues** — blocking indexing or causing errors
3. **Warnings** — hurting performance or rankings
4. **Passed Checks** — what's working well
5. **Prioritized Fix List** — ordered by impact and effort
6. **Implementation Guide** — how to fix each issue
7. **Monitoring Recommendations** — what to track ongoing

#### Priority Matrix

Categorize all findings:

| | Low Effort | High Effort |
|--|-----------|-------------|
| **High Impact** | **Quick Wins** — do first | **Strategic** — plan & schedule |
| **Low Impact** | **Fill-ins** — when time allows | **Deprioritize** — skip for now |

---

## CMS-Specific Checks

Add platform-specific checks when CMS is known:

- **WordPress** — check for SEO plugin (Yoast/RankMath), plugin bloat, theme speed, auto-generated pages
- **Shopify** — check collection pagination, variant URLs, liquid template issues
- **Wix** — check JavaScript rendering, URL structure, limited robots.txt control
- **Squarespace** — check URL structure, limited schema options, image optimization
- **Custom** — check server configuration, caching implementation, framework-specific issues

---

## Additional Resources

### Reference Files

> Only read `health-report-template.md` when generating the final report (Phase 7). Only read `common-issues-fixes.md` when producing CMS-specific fix instructions — not during the audit phases.

- **`references/health-report-template.md`** — Full health audit report template with scoring rubric
- **`references/common-issues-fixes.md`** — Encyclopedia of common technical SEO issues with step-by-step fix instructions per CMS

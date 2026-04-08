---
name: local-seo-audit
description: This skill should be used when the user asks to "audit local SEO", "Google Business Profile audit", "NAP consistency check", "local citations audit", "local pack optimization", or wants to evaluate a business's local search visibility and Google Business Profile health.
version: 1.0.0
---

# Local SEO Audit

Perform comprehensive local SEO audits covering Google Business Profile (GBP) optimization, NAP (Name, Address, Phone) consistency, local citations, review signals, and local pack ranking factors. Generate actionable reports with prioritized fixes.

---

## Core Workflow

### Phase 1 — Information Gathering

Collect the following from the user before starting:

1. **Business name** and **primary location** (city/state/country)
2. **Google Business Profile URL** or business name as it appears on Google
3. **Website URL**
4. **Primary service area** (radius or specific cities)
5. **Target keywords** (3-5 main local search terms)
6. **Top 3 local competitors** (optional — can be researched)

If the user provides a website URL, use web search and browsing tools to gather publicly available data.

### Phase 2 — GBP Profile Analysis

Evaluate the Google Business Profile against these criteria:

| Factor | Check | Priority |
|--------|-------|----------|
| Business name | Matches real name, no keyword stuffing | Critical |
| Primary category | Most specific relevant category selected | Critical |
| Secondary categories | All relevant categories added (max 9) | High |
| Description | 750 chars, keywords natural, CTA included | High |
| Address | Complete, matches website exactly | Critical |
| Phone | Local number, matches website | Critical |
| Hours | Complete, including special hours | Medium |
| Photos | Min 10 photos, cover + logo + interior/exterior | High |
| Posts | Active within last 7 days | Medium |
| Q&A | Seeded with common questions + answers | Medium |
| Reviews | Response rate, avg rating, keyword presence | High |
| Services/Products | All listed with descriptions | Medium |
| Attributes | All relevant attributes enabled | Low |

### Phase 3 — NAP Consistency Audit

Check NAP consistency across these sources (use web search):

- Website (header, footer, contact page)
- Google Business Profile
- Major directories: Yelp, Facebook, Apple Maps, Bing Places
- Industry-specific directories
- Local chamber of commerce or associations

Flag any variations in:
- Business name spelling/formatting
- Address format (St vs Street, Suite formatting)
- Phone number format
- Website URL (www vs non-www, http vs https)

### Phase 4 — On-Site Local SEO Factors

Analyze the website for local optimization:

1. **Title tags** — city + service in homepage and key pages
2. **Meta descriptions** — local intent signals
3. **H1 tags** — local keyword presence
4. **Schema markup** — LocalBusiness or relevant subtype present
5. **NAP on site** — consistent, crawlable (not in images)
6. **Local landing pages** — dedicated pages per service area
7. **Embedded map** — Google Maps embed on contact page
8. **Internal linking** — location pages linked from nav/footer
9. **Mobile responsiveness** — critical for local search
10. **Page speed** — Core Web Vitals passing

### Phase 5 — Review & Reputation Signals

Analyze review profile:

- Total review count vs top 3 competitors
- Average star rating
- Review velocity (reviews per month)
- Review recency (last review date)
- Owner response rate and quality
- Keyword mentions in reviews (organic)
- Negative review patterns (recurring issues)

### Phase 6 — Report Generation

Produce the final audit report using the template in `references/audit-report-template.md`. Structure:

1. **Executive Summary** — overall local SEO health score (0-100)
2. **Critical Issues** — must fix immediately (red)
3. **High Priority** — fix within 2 weeks (orange)
4. **Medium Priority** — fix within 30 days (yellow)
5. **Low Priority** — optimize when possible (green)
6. **Competitive Snapshot** — how the business compares locally
7. **Action Plan** — prioritized task list with estimated impact

### Scoring System

Calculate the health score by weighting:

| Category | Weight |
|----------|--------|
| GBP Completeness | 25% |
| NAP Consistency | 20% |
| On-Site Local SEO | 20% |
| Reviews & Reputation | 20% |
| Local Content & Links | 15% |

Each category scored 0-100, then weighted for final score.

---

## Additional Resources

### Reference Files

> Only read these files when generating the final report output (Phase 6). Do not read them during earlier phases.

- **`references/audit-report-template.md`** — Full audit report template with scoring rubric
- **`references/gbp-optimization-checklist.md`** — Detailed GBP optimization guide with all fields and best practices

### Scripts

> User-run only — not invoked during the audit workflow. Suggest to the user if they want to automate NAP checking across many URLs.

- **`scripts/nap-checker.py`** — Python script to check NAP consistency across provided URLs

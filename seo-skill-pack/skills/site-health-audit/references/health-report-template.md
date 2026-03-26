# Site Health Audit Report Template

## Report Header

```
SITE HEALTH AUDIT REPORT
=========================
Website:   [URL]
CMS:       [WordPress/Shopify/Custom/etc.]
Date:      [Audit Date]
Auditor:   Claude Site Health Audit
```

---

## 1. Health Score Dashboard

**Overall Health Score: [XX]/100**

| Category | Score | Weight | Weighted | Status |
|----------|-------|--------|----------|--------|
| Crawlability & Indexing | /100 | 25% | /25 | [Pass/Warn/Fail] |
| Core Web Vitals | /100 | 25% | /25 | [Pass/Warn/Fail] |
| On-Page SEO | /100 | 20% | /20 | [Pass/Warn/Fail] |
| Mobile Experience | /100 | 15% | /15 | [Pass/Warn/Fail] |
| Security & Trust | /100 | 15% | /15 | [Pass/Warn/Fail] |
| **Overall** | — | **100%** | **/100** | — |

### Summary
- **Critical Issues:** [count] (must fix now)
- **Warnings:** [count] (should fix soon)
- **Passed Checks:** [count] (working well)

---

## 2. Crawlability & Indexing

### robots.txt

| Check | Status | Details |
|-------|--------|---------|
| File exists | Pass/Fail | [URL to robots.txt] |
| No critical blocks | Pass/Fail | [blocked paths if any] |
| Sitemap referenced | Pass/Fail | [sitemap URL in robots.txt] |
| AI crawler policy | Info | [which AI bots allowed/blocked] |

**robots.txt content:**
```
[paste robots.txt content]
```

### Sitemap

| Check | Status | Details |
|-------|--------|---------|
| Sitemap exists | Pass/Fail | [URL] |
| Valid XML | Pass/Fail | [errors if any] |
| Key pages included | Pass/Fail | [missing pages] |
| Last modified dates | Pass/Fail | [freshness] |
| Submitted to Search Console | Pass/Fail/Unknown | — |

### Indexing Factors

| Check | Status | Details |
|-------|--------|---------|
| Canonical tags | Pass/Warn/Fail | [issues] |
| Noindex tags | Pass/Warn/Fail | [incorrectly noindexed pages] |
| Redirect chains | Pass/Warn/Fail | [chains found] |
| 404 errors | Pass/Warn/Fail | [broken pages] |
| URL structure | Pass/Warn/Fail | [issues] |
| JavaScript rendering | Pass/Warn/Fail | [content hidden behind JS] |
| Pagination | Pass/Warn/N/A | [issues] |
| Hreflang | Pass/Warn/N/A | [issues] |

### Category Score: [XX]/100

---

## 3. Core Web Vitals & Performance

### Metrics

| Metric | Value | Threshold | Status |
|--------|-------|-----------|--------|
| LCP (Largest Contentful Paint) | [X.Xs] | <=2.5s good | [Good/Needs Work/Poor] |
| INP (Interaction to Next Paint) | [Xms] | <=200ms good | [Good/Needs Work/Poor] |
| CLS (Cumulative Layout Shift) | [X.XX] | <=0.1 good | [Good/Needs Work/Poor] |
| TTFB (Time to First Byte) | [Xms] | <=800ms good | [Good/Needs Work/Poor] |
| FCP (First Contentful Paint) | [X.Xs] | <=1.8s good | [Good/Needs Work/Poor] |

### Performance Issues Found

| Issue | Impact | Pages Affected | Fix |
|-------|--------|---------------|-----|
| [issue] | [High/Med/Low] | [pages/sitewide] | [fix description] |

### Category Score: [XX]/100

---

## 4. On-Page SEO

### Page-by-Page Analysis

#### Homepage: [URL]

| Element | Status | Current Value | Issue | Fix |
|---------|--------|--------------|-------|-----|
| Title tag | Pass/Fail | "[current]" ([X] chars) | [issue] | [fix] |
| Meta description | Pass/Fail | "[current]" ([X] chars) | [issue] | [fix] |
| H1 | Pass/Fail | "[current]" | [issue] | [fix] |
| Heading hierarchy | Pass/Fail | [structure] | [issue] | [fix] |
| Image alt text | Pass/Fail | [X]/[Y] images have alt | [issue] | [fix] |
| Schema markup | Pass/Fail | [types found] | [issue] | [fix] |

#### [Key Page 2]: [URL]
[Same table structure]

#### [Key Page 3]: [URL]
[Same table structure]

### Sitewide On-Page Issues

| Issue | Count | Severity | Pages |
|-------|-------|----------|-------|
| Missing title tags | [n] | Critical | [list] |
| Duplicate titles | [n] | High | [list] |
| Missing meta descriptions | [n] | High | [list] |
| Missing H1 tags | [n] | High | [list] |
| Multiple H1 tags | [n] | Medium | [list] |
| Images without alt text | [n] | Medium | [list] |
| Missing schema markup | [n] | Medium | [list] |
| Thin content (< 300 words) | [n] | Medium | [list] |

### Category Score: [XX]/100

---

## 5. Mobile Experience

| Check | Status | Details |
|-------|--------|---------|
| Responsive design | Pass/Fail | [issues] |
| Viewport meta tag | Pass/Fail | [present/missing] |
| Touch target size | Pass/Warn/Fail | [issues with small targets] |
| Font size | Pass/Warn/Fail | [min size found] |
| Horizontal scroll | Pass/Fail | [pages affected] |
| Intrusive interstitials | Pass/Fail | [popups found] |
| Mobile navigation | Pass/Warn/Fail | [issues] |
| Form usability | Pass/Warn/N/A | [issues] |

### Category Score: [XX]/100

---

## 6. Security & Trust

| Check | Status | Details |
|-------|--------|---------|
| HTTPS | Pass/Fail | [cert details] |
| Mixed content | Pass/Fail | [http resources on https pages] |
| HSTS header | Pass/Fail | [header value] |
| X-Frame-Options | Pass/Fail | [header value] |
| Content-Security-Policy | Pass/Warn/Fail | [header value] |
| X-Content-Type-Options | Pass/Fail | [header value] |
| Privacy policy | Pass/Fail | [URL] |
| Terms of service | Pass/Fail | [URL] |
| Contact information | Pass/Fail | [visible/hidden] |
| SSL certificate validity | Pass/Fail | [expiry date] |

### Category Score: [XX]/100

---

## 7. All Issues — Prioritized Fix List

### Priority Matrix

| | Low Effort (< 1 hour) | Medium Effort (1-4 hours) | High Effort (4+ hours) |
|--|----------------------|--------------------------|----------------------|
| **High Impact** | QUICK WINS | STRATEGIC | STRATEGIC |
| **Medium Impact** | QUICK WINS | PLAN | BACKLOG |
| **Low Impact** | FILL-IN | BACKLOG | SKIP |

### Quick Wins (Do First)

| # | Issue | Category | Impact | How to Fix | Est. Time |
|---|-------|----------|--------|-----------|-----------|
| 1 | [issue] | [cat] | High | [steps] | [time] |

### Strategic Fixes (Plan & Schedule)

| # | Issue | Category | Impact | How to Fix | Est. Time |
|---|-------|----------|--------|-----------|-----------|
| 1 | [issue] | [cat] | High | [steps] | [time] |

### Backlog (When Time Allows)

| # | Issue | Category | Impact | How to Fix | Est. Time |
|---|-------|----------|--------|-----------|-----------|
| 1 | [issue] | [cat] | Low-Med | [steps] | [time] |

---

## 8. Monitoring Recommendations

| What to Monitor | Tool | Frequency | Alert Threshold |
|----------------|------|-----------|-----------------|
| Core Web Vitals | Search Console / PageSpeed | Monthly | Any metric goes "Poor" |
| Indexing errors | Search Console | Weekly | New errors appear |
| 404 errors | Search Console / Analytics | Weekly | Spike in 404s |
| SSL certificate | Uptime monitor | Daily (auto) | 30 days before expiry |
| Uptime | Uptime monitor | Continuous | Any downtime |
| Rankings | Search Console | Bi-weekly | Significant drops |
| Mobile usability | Search Console | Monthly | New issues |

---

## 9. Next Steps

1. **Immediate** (this week): [top 3 critical fixes]
2. **Short-term** (next 2 weeks): [quick wins list]
3. **Medium-term** (next month): [strategic fixes]
4. **Ongoing**: [monitoring setup]

### Re-Audit Recommendation
Schedule a follow-up audit in [30/60/90] days to measure progress.

---

*Report generated by SEO Pack — Site Health Quick Audit*

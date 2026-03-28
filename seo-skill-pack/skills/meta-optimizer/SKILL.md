---
name: meta-optimizer
description: This skill should be used when the user asks to "optimize meta tags", "fix title tags", "write meta descriptions", "improve meta titles", "meta tag audit", "title tag optimization", "SERP snippet optimization", "CTR optimization", "fix page titles", "rewrite meta descriptions", "bulk meta tag optimization", or provides a list of pages/URLs needing title and description improvements for better search visibility and click-through rates.
version: 1.0.0
---

# Meta Title & Description Optimizer

Analyze and optimize meta titles and descriptions for maximum search visibility and click-through rate (CTR). Handle individual pages or bulk optimization across entire sites. Apply current best practices for both traditional SERP display and AI search result presentation.

---

## Core Workflow

### Phase 1 — Input Collection

Accept input in multiple formats:

1. **Single page** — URL + target keyword
2. **Bulk list** — CSV/spreadsheet with URL, current title, current description, target keyword
3. **Crawl data** — exported from Screaming Frog, Ahrefs, or similar
4. **Website URL** — crawl and extract current meta tags (use web tools)

For each page, gather:
- Current title tag and character count
- Current meta description and character count
- Target primary keyword
- Page type (homepage, product, blog, category, location)
- Current ranking position (if known)

### Phase 2 — Analysis & Issues

Audit each meta element against these rules:

#### Title Tag Issues

| Issue | Rule | Severity |
|-------|------|----------|
| Missing | No title tag present | Critical |
| Too long | >60 characters (truncated in SERP) | High |
| Too short | <30 characters (wasted space) | Medium |
| Keyword missing | Primary keyword not in title | High |
| Keyword not front-loaded | Primary keyword not in first 3 words | Medium |
| Duplicate | Same title on multiple pages | High |
| Brand missing | Brand name not included | Low |
| Keyword stuffing | Same keyword repeated | High |
| Generic | "Home", "Untitled", default CMS title | Critical |
| Pipe overload | More than 2 separators (| or -) | Medium |

#### Meta Description Issues

| Issue | Rule | Severity |
|-------|------|----------|
| Missing | No meta description | High |
| Too long | >155 characters (truncated) | Medium |
| Too short | <70 characters (thin) | Medium |
| No CTA | Missing call-to-action | Medium |
| No keyword | Primary keyword absent | Medium |
| Duplicate | Same description across pages | High |
| Not compelling | Generic, doesn't differentiate | Medium |
| No value prop | Doesn't state what user gets | Medium |

### Phase 3 — Optimization

Generate optimized versions following these formulas:

#### Title Tag Formulas

By page type:

- **Homepage**: `[Primary Keyword] - [Value Prop] | [Brand]`
- **Product**: `[Product Name] - [Key Benefit] | [Brand]`
- **Blog Post**: `[Number/How/What] [Keyword] [Promise/Year] | [Brand]`
- **Category**: `[Category Keyword] - [Differentiator] | [Brand]`
- **Location**: `[Service] in [City] - [Differentiator] | [Brand]`
- **Comparison**: `[A] vs [B]: [Verdict/Year] | [Brand]`

#### Meta Description Formula

Structure: **Hook + Value + CTA** (within 155 characters)

```
[Hook: stat, question, or bold claim]. [Value: what the page delivers].
[CTA: action verb + what happens next].
```

#### Optimization Rules

1. Place primary keyword within first 60 characters of title
2. Front-load the most important keyword in the title
3. Include a power word or number in the title for CTR
4. Write descriptions as a complete, compelling sentence
5. Include primary keyword naturally in description
6. Add a CTA (Learn more, Get started, See pricing, Compare now)
7. Use unique titles and descriptions per page — zero duplicates
8. Match the search intent (informational vs transactional tone)
9. For local pages, include city/region in title
10. Include the current year for time-sensitive content

### Phase 4 — Output Format

Generate results in a structured table:

```markdown
| URL | Current Title (chars) | Optimized Title (chars) | Current Desc (chars) | Optimized Desc (chars) | Issues Fixed |
```

For bulk optimization (10+ pages), also provide:
- **Summary statistics** — total issues found by severity
- **Pattern issues** — sitewide problems (e.g., all titles missing brand)
- **Priority list** — pages to fix first based on traffic + severity

### Phase 5 — Validation

Before delivering, validate each optimized tag:

- [ ] Title <=60 characters (pixel width ~580px)
- [ ] Description <=155 characters (pixel width ~920px)
- [ ] Primary keyword present in both
- [ ] No duplicates in the batch
- [ ] Matches page content and intent
- [ ] Brand name included in title
- [ ] CTA present in description
- [ ] Reads naturally (no keyword stuffing)

---

## SERP Preview

For high-priority pages, generate a text-based SERP preview:

```
[Optimized Title Tag — 60 chars max]
https://example.com/page-slug
[Optimized Meta Description — 155 chars max, with keyword bolded concept]
```

---

## Additional Resources

### Reference Files

- **`references/title-formulas.md`** — Extended title tag formulas by industry and page type with CTR data
- **`references/power-words-list.md`** — Curated list of CTR-boosting power words, numbers, and emotional triggers for titles and descriptions

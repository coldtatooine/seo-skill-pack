---
name: competitor-gap-analyzer
description: This skill should be used when the user asks to "competitor gap analysis", "find keyword gaps", "competitive SEO analysis", "content gap analysis", "competitor backlink analysis", or wants to identify SEO opportunities by analyzing what competitors rank for and where gaps exist.
version: 1.0.0
---

# Competitor Gap Analyzer

Perform systematic competitor analysis to identify keyword gaps, content opportunities, technical advantages, and strategic insights. Compare the user's site against 3-5 competitors across organic search, content quality, technical SEO, and backlink profiles.

---

## Core Workflow

### Phase 1 — Competitor Identification

If the user hasn't identified competitors:

1. **Search primary keywords** — note which domains consistently appear in top 10
2. **Categorize competitors**:
   - **Direct** — same services/products, same area
   - **Indirect** — different offering but ranking for same keywords
   - **SERP competitors** — ranking for target keywords regardless of business type
3. **Select 3-5 competitors** for analysis (prioritize direct + SERP competitors)

Collect for each competitor:
- Domain URL
- Business description
- Estimated domain authority / traffic (if tools available)
- Primary service/product overlap with user's business

### Phase 2 — Keyword Gap Analysis

Compare keyword profiles between user and competitors:

#### Keyword Categories

| Category | Definition | Priority |
|----------|-----------|----------|
| **Missing keywords** | Competitors rank, user doesn't rank at all | High |
| **Weak keywords** | User ranks page 2-3, competitors rank page 1 | Critical |
| **Declining keywords** | User lost rankings competitors now hold | High |
| **Untapped long-tail** | Low competition keywords competitors target | Medium |
| **Question keywords** | PAA/FAQ queries competitors answer | Medium |

#### Analysis Process

1. Use web search to check user's rankings for primary keywords
2. Search competitor domains with `site:competitor.com [keyword]`
3. Analyze which queries return competitor content but not user's
4. Map keyword intent (informational, commercial, transactional, navigational)
5. Estimate difficulty vs. opportunity for each gap

Output as prioritized table:

```markdown
| Keyword | Monthly Volume | User Rank | Comp A Rank | Comp B Rank | Intent | Gap Type | Priority |
```

### Phase 3 — Content Gap Analysis

Compare content strategies:

#### Content Inventory Comparison

For each competitor, catalog:

1. **Blog/resource frequency** — posts per month
2. **Content types** — blogs, guides, videos, tools, case studies
3. **Content depth** — average word count, comprehensiveness
4. **Topic clusters** — how they organize content
5. **Freshness** — when content was last updated
6. **Top-performing pages** — pages ranking for most keywords

#### Gap Identification

Map content gaps in a matrix:

```markdown
| Topic/Keyword | User Content | Comp A | Comp B | Comp C | Opportunity |
|---------------|-------------|--------|--------|--------|-------------|
| [topic 1]     | None        | Guide  | Blog   | Video  | Create guide|
| [topic 2]     | Blog (thin) | Long guide | — | FAQ  | Expand content|
| [topic 3]     | Good guide  | —      | —      | —      | Defend position|
```

### Phase 4 — Technical SEO Comparison

Compare technical factors using publicly available data:

| Factor | How to Check | What to Compare |
|--------|-------------|-----------------|
| Page speed | Web search for PageSpeed results | Core Web Vitals |
| Mobile UX | Browse on mobile / responsive check | Mobile-friendliness |
| Schema markup | View source / web tools | Types and completeness |
| Site structure | Crawl sitemap.xml | Depth, organization |
| Internal linking | Browse navigation | Link structure |
| HTTPS | Check URL | Security implementation |
| Meta tags | View source | Title/description quality |

### Phase 5 — Backlink & Authority Comparison

Analyze link profiles (from publicly available data):

1. **Domain authority signals** — brand mentions, Wikipedia links, press coverage
2. **Content cited by others** — which competitor pages get linked/cited
3. **Local citations** — directory presence comparison
4. **Social signals** — social media presence and engagement
5. **PR & media** — press mentions, interview features

### Phase 6 — Opportunity Report

Generate the analysis report using `references/gap-report-template.md`:

#### Report Structure

1. **Executive Summary**
   - Top 5 biggest opportunities ranked by potential impact
   - Quick wins (achievable in 30 days)
   - Strategic plays (3-6 months)

2. **Keyword Gap Report**
   - Missing keywords with estimated volume
   - Weak keywords to improve
   - Priority ranking by impact x effort

3. **Content Opportunities**
   - Content to create (topics competitors cover, user doesn't)
   - Content to improve (existing pages underperforming vs. competitors)
   - Content to defend (user ranks well, competitors catching up)

4. **Technical Advantages/Disadvantages**
   - Where competitors have technical edge
   - Where user has technical edge
   - Fixes to close technical gaps

5. **Authority & Link Building**
   - Link gap analysis
   - Citation opportunities
   - Content formats that attract links in this niche

6. **Action Plan**
   - 30-day quick wins
   - 90-day strategy
   - Ongoing competitive monitoring recommendations

---

## Competitive Advantage Framework

Score each competitor across dimensions:

| Dimension | Weight | User | Comp A | Comp B | Comp C |
|-----------|--------|------|--------|--------|--------|
| Content Quality | 25% | ?/10 | ?/10 | ?/10 | ?/10 |
| Technical SEO | 20% | ?/10 | ?/10 | ?/10 | ?/10 |
| Keyword Coverage | 25% | ?/10 | ?/10 | ?/10 | ?/10 |
| Authority/Links | 20% | ?/10 | ?/10 | ?/10 | ?/10 |
| Local Signals | 10% | ?/10 | ?/10 | ?/10 | ?/10 |
| **Weighted Total** | 100% | — | — | — | — |

---

## Additional Resources

### Reference Files

> Only read these files when generating the final report output (Phase 6). Do not read them during earlier phases.

- **`references/gap-report-template.md`** — Full competitor gap analysis report template
- **`references/keyword-gap-methodology.md`** — Detailed methodology for keyword gap analysis with examples and prioritization frameworks

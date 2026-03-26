---
name: AI Search Readiness Checker
description: This skill should be used when the user asks to "check AI search readiness", "optimize for AI search", "AI overview optimization", "SGE optimization", "optimize for ChatGPT search", "optimize for Perplexity", "AI citations audit", "LLM visibility check", "generative search optimization", "check if AI mentions my brand", "AI search audit", or wants to evaluate how well a website or brand appears in AI-generated search results (Google AI Overviews, ChatGPT, Perplexity, Claude).
version: 1.0.0
---

# AI Search Readiness Checker

Evaluate how well a website is positioned to appear in AI-generated search results — Google AI Overviews, ChatGPT Browse, Perplexity, and other LLM-powered search engines. Identify gaps and provide actionable optimization recommendations.

---

## Core Workflow

### Phase 1 — Information Gathering

Collect from the user:

1. **Website URL** and **brand name**
2. **Primary topics/services** the brand should be known for
3. **Target audience** (B2B/B2C, industry, geography)
4. **Top 5 queries** they want to appear in AI search results for
5. **Known competitors** appearing in AI results (optional)

### Phase 2 — Content Structure Analysis

Analyze the website for AI-crawlability and citation-worthiness:

#### Technical Accessibility
- **robots.txt** — check for blocks on AI crawlers (GPTBot, Google-Extended, anthropic-ai, ClaudeBot, PerplexityBot, Bytespider)
- **Sitemap.xml** — exists, valid, includes key pages
- **Crawl depth** — important content within 3 clicks of homepage
- **Page speed** — fast-loading pages are more likely crawled
- **Clean URL structure** — descriptive, keyword-rich paths

#### Content Quality Signals

| Signal | Check | Impact |
|--------|-------|--------|
| Structured headings | H1-H3 hierarchy with clear topics | High |
| Direct answers | Concise definitions/answers in first paragraph | Critical |
| Data & statistics | Original data, cited sources | High |
| Author expertise | Author bios, credentials, E-E-A-T signals | High |
| Freshness | Content updated within 6 months | Medium |
| Comprehensiveness | Topic coverage depth vs competitors | High |
| Unique perspective | Original research, case studies, first-party data | Critical |
| List/table format | Structured data AI can easily extract | Medium |

#### Schema & Structured Data
- FAQPage schema for Q&A content
- HowTo schema for tutorial content
- Article schema with author and dateModified
- Organization schema with complete entity info
- BreadcrumbList for site hierarchy

### Phase 3 — Entity & Brand Presence

Check brand entity recognition across AI systems:

1. **Search brand name** in ChatGPT, Perplexity, and Google AI Overviews
2. **Evaluate responses** for accuracy, recency, and sentiment
3. **Check entity associations** — is the brand correctly linked to its industry, products, and location?
4. **Wikipedia/Wikidata presence** — strong signal for entity recognition
5. **Knowledge panel** — does Google show a knowledge panel?

Document findings in a structured format:

```
| AI Platform | Brand Mentioned? | Accuracy | Sentiment | Recency |
|-------------|-----------------|----------|-----------|---------|
| Google AIO  | Yes/No          | 1-5      | +/0/-     | Date    |
| ChatGPT     | Yes/No          | 1-5      | +/0/-     | Date    |
| Perplexity  | Yes/No          | 1-5      | +/0/-     | Date    |
```

### Phase 4 — Citation Opportunity Analysis

For each target query, analyze what AI platforms currently cite:

1. Run each query through available AI search tools
2. Document which sources are cited
3. Identify patterns in cited content (format, length, authority)
4. Map gaps between current citations and user's content
5. Score citation potential per query (Low/Medium/High)

### Phase 5 — Recommendations Report

Generate the readiness report using `references/readiness-report-template.md`:

1. **AI Readiness Score** (0-100)
2. **Crawler Access Status** — which AI bots can/cannot crawl the site
3. **Content Optimization** — specific pages to improve for AI citation
4. **Entity Building** — steps to strengthen brand entity recognition
5. **Schema Gaps** — missing structured data implementations
6. **Citation Strategy** — content to create/optimize for AI search visibility
7. **Monitoring Plan** — how to track AI search appearances over time

### Scoring System

| Category | Weight |
|----------|--------|
| Technical Accessibility (crawlers, speed, structure) | 20% |
| Content Quality & Format | 30% |
| Entity & Brand Recognition | 25% |
| Schema & Structured Data | 15% |
| Citation Presence | 10% |

---

## Key Principles

- AI search engines favor **authoritative, well-structured, concise content** that directly answers queries
- **Original data and unique perspectives** dramatically increase citation probability
- **E-E-A-T signals** (Experience, Expertise, Authoritativeness, Trustworthiness) matter even more for AI search
- Blocking AI crawlers is a business decision — document tradeoffs, do not assume one answer
- AI search is evolving rapidly — recommendations should be framed as current best practices

---

## Additional Resources

### Reference Files

- **`references/readiness-report-template.md`** — Full report template with scoring rubric
- **`references/ai-crawler-list.md`** — Complete list of known AI crawler user-agents and their robots.txt directives

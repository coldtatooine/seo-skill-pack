---
name: geo-content-brief
description: This skill should be used when the user asks to "create a content brief", "GEO content brief", "SEO content outline", "keyword-driven content brief", or wants to generate a structured content brief designed to rank in both traditional and generative/AI search results.
version: 1.0.0
---

# GEO Content Brief Generator

Generate comprehensive content briefs optimized for both traditional SEO and Generative Engine Optimization (GEO). Each brief includes target keywords, search intent mapping, content structure, E-E-A-T requirements, and AI-citation optimization guidance.

---

## Core Workflow

### Phase 1 — Input & Research

Collect from the user:

1. **Primary keyword/topic** — the main search query to target
2. **Business context** — what the business does, target audience
3. **Content type** — blog post, landing page, guide, FAQ, comparison
4. **Geographic focus** — local, national, or international
5. **Existing content** — URL of current page to improve (optional)

Then research:

1. **SERP analysis** — search the primary keyword, analyze top 10 results
2. **Search intent** — classify as informational, navigational, commercial, or transactional
3. **Related keywords** — identify LSI keywords, questions, and long-tail variations
4. **SERP features** — note featured snippets, PAA, local pack, AI overviews
5. **Content gaps** — what top results miss that can be covered

### Phase 2 — Keyword Mapping

Build the keyword map:

| Tier | Keywords | Search Intent | Target Section |
|------|----------|--------------|----------------|
| Primary | Main keyword (1) | Classified intent | H1 / Title |
| Secondary | Related terms (3-5) | Related intents | H2 headings |
| Supporting | Long-tail, questions (5-10) | Various | H3s, body, FAQ |
| LSI/Semantic | Contextual terms (10-15) | — | Natural usage |

### Phase 3 — Content Structure

Generate the brief structure:

#### Meta Elements
- **Title tag** — primary keyword + modifier + brand (max 60 chars)
- **Meta description** — value prop + CTA + keyword (max 155 chars)
- **URL slug** — short, keyword-rich, hyphenated

#### Content Outline
```
H1: [Primary keyword + unique angle]
  Intro (100-150 words)
  - Hook with statistic or question
  - Define the topic concisely (AI-citation target)
  - Preview what the reader will learn

  H2: [Secondary keyword 1]
    H3: [Supporting keyword]
    H3: [Supporting keyword]

  H2: [Secondary keyword 2]
    H3: [Supporting keyword]
    H3: [Supporting keyword]

  H2: [Secondary keyword 3]
    - Include data table or comparison chart

  H2: Expert Tips / Best Practices
    - E-E-A-T signal section

  H2: FAQ
    - Top 5 PAA questions with concise answers

  Conclusion + CTA
```

#### Word Count & Format Guidance
- Analyze top-ranking content word counts
- Recommend target word count (typically within range of top 5)
- Specify required formats: tables, lists, images, videos, infographics

### Phase 4 — GEO Optimization Layer

Add generative search optimization to the brief:

1. **Direct Answer Blocks** — for each H2, write a 2-3 sentence "citation-ready" summary that AI can extract
2. **Structured Data** — recommend specific schema types (FAQ, HowTo, Article)
3. **Statistic Integration** — identify 3-5 data points to include with sources
4. **Unique Value** — specify what original insight, data, or perspective to add
5. **Entity Optimization** — list entities to mention and link (people, brands, concepts)
6. **Quotable Statements** — craft 2-3 definitive statements AI might quote

### Phase 5 — E-E-A-T Requirements

Specify for the brief:

- **Experience** — what first-hand experience to demonstrate
- **Expertise** — author credentials to highlight, technical depth needed
- **Authoritativeness** — sources to cite, data to reference, expert quotes
- **Trustworthiness** — disclosures needed, methodology transparency

### Phase 6 — Brief Output

Generate the final brief using `references/brief-template.md`. Include:

1. **Brief Header** — topic, target keyword, intent, content type, word count
2. **Keyword Map** — full tier table
3. **SERP Landscape** — what currently ranks and why
4. **Content Outline** — full H1-H3 structure with guidance per section
5. **GEO Optimization Notes** — citation targets, direct answers, schema
6. **E-E-A-T Checklist** — specific requirements for this topic
7. **Internal Linking** — pages to link to/from
8. **Visual Assets** — images, charts, tables needed
9. **Competitor Differentiation** — what to do differently from top results

---

## Content Type Templates

Adapt the brief structure based on content type:

| Type | Focus | Key Sections |
|------|-------|-------------|
| Blog Post | Informational depth | Research, examples, expert takes |
| Landing Page | Conversion + local intent | Benefits, social proof, CTAs, schema |
| Guide/Tutorial | Step-by-step completeness | HowTo schema, screenshots, video |
| Comparison | Decision support | Tables, pros/cons, verdict |
| FAQ Page | Direct answers | FAQPage schema, concise answers |
| Location Page | Local relevance | LocalBusiness schema, reviews, map |

---

## Additional Resources

### Reference Files

> Only read these files when generating the final brief output (Phase 6). Do not read them during research or outlining phases.

- **`references/brief-template.md`** — Full content brief template with all sections
- **`references/geo-optimization-guide.md`** — Deep dive into Generative Engine Optimization techniques and patterns

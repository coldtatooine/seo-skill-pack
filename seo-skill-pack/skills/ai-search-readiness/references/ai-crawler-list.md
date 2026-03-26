# AI Crawler User-Agents & robots.txt Directives

## Known AI Crawlers (as of 2026)

### OpenAI

| Crawler | User-Agent | Purpose |
|---------|-----------|---------|
| GPTBot | `GPTBot` | Training data + ChatGPT Browse |
| ChatGPT-User | `ChatGPT-User` | Real-time browsing by ChatGPT |
| OAI-SearchBot | `OAI-SearchBot` | SearchGPT search results |

**robots.txt to block:**
```
User-agent: GPTBot
Disallow: /

User-agent: ChatGPT-User
Disallow: /

User-agent: OAI-SearchBot
Disallow: /
```

**To allow browsing but block training:**
```
User-agent: GPTBot
Disallow: /

User-agent: ChatGPT-User
Allow: /

User-agent: OAI-SearchBot
Allow: /
```

### Google

| Crawler | User-Agent | Purpose |
|---------|-----------|---------|
| Googlebot | `Googlebot` | Standard search indexing |
| Google-Extended | `Google-Extended` | Gemini/AI training data |

**To allow search but block AI training:**
```
User-agent: Google-Extended
Disallow: /
```

Note: Blocking `Google-Extended` does NOT affect standard Google Search indexing.

### Anthropic

| Crawler | User-Agent | Purpose |
|---------|-----------|---------|
| ClaudeBot | `ClaudeBot` | Training data collection |
| anthropic-ai | `anthropic-ai` | General crawling |

**robots.txt:**
```
User-agent: ClaudeBot
Disallow: /

User-agent: anthropic-ai
Disallow: /
```

### Perplexity

| Crawler | User-Agent | Purpose |
|---------|-----------|---------|
| PerplexityBot | `PerplexityBot` | Search results and citations |

**robots.txt:**
```
User-agent: PerplexityBot
Disallow: /
```

**Note:** Blocking PerplexityBot means your content won't be cited in Perplexity answers.

### Meta

| Crawler | User-Agent | Purpose |
|---------|-----------|---------|
| FacebookBot | `FacebookBot` | Standard crawling (Open Graph) |
| Meta-ExternalAgent | `Meta-ExternalAgent` | AI training data |
| Meta-ExternalFetcher | `Meta-ExternalFetcher` | AI real-time fetching |

**To allow social sharing but block AI training:**
```
User-agent: Meta-ExternalAgent
Disallow: /

User-agent: Meta-ExternalFetcher
Disallow: /
```

### Other AI Crawlers

| Crawler | User-Agent | Company | Purpose |
|---------|-----------|---------|---------|
| Bytespider | `Bytespider` | ByteDance/TikTok | AI training |
| CCBot | `CCBot` | Common Crawl | Open dataset (used by many AI) |
| Diffbot | `Diffbot` | Diffbot | Data extraction |
| Applebot-Extended | `Applebot-Extended` | Apple | Apple Intelligence training |
| cohere-ai | `cohere-ai` | Cohere | AI training |
| Amazonbot | `Amazonbot` | Amazon | Alexa / AI training |
| YouBot | `YouBot` | You.com | AI search |
| Timpibot | `Timpibot` | Timpi | Decentralized search |
| VelenPublicWebCrawler | `VelenPublicWebCrawler` | Velen | AI training |
| omgili | `omgili` | Webz.io | Data collection |
| Kangaroo Bot | `Kangaroo Bot` | Kangaroo LLM | AI training |
| PetalBot | `PetalBot` | Huawei | Search + AI |

---

## Recommended robots.txt Strategy

### Allow All AI (Maximum Visibility)
```
# No specific AI bot blocks needed
# All bots follow standard Googlebot rules
```

### Allow Search, Block Training (Balanced)
```
# Block AI training bots
User-agent: GPTBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: anthropic-ai
Disallow: /

User-agent: Meta-ExternalAgent
Disallow: /

User-agent: Bytespider
Disallow: /

User-agent: CCBot
Disallow: /

# Allow AI search bots for visibility
User-agent: ChatGPT-User
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /
```

### Block All AI (Maximum Protection)
```
User-agent: GPTBot
Disallow: /

User-agent: ChatGPT-User
Disallow: /

User-agent: OAI-SearchBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: anthropic-ai
Disallow: /

User-agent: PerplexityBot
Disallow: /

User-agent: Meta-ExternalAgent
Disallow: /

User-agent: Meta-ExternalFetcher
Disallow: /

User-agent: Bytespider
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: Applebot-Extended
Disallow: /

User-agent: cohere-ai
Disallow: /

User-agent: Amazonbot
Disallow: /
```

---

## HTTP Headers Alternative

In addition to robots.txt, some AI companies respect HTTP headers:

### X-Robots-Tag
```
X-Robots-Tag: noai
X-Robots-Tag: noimageai
```

### Meta Tags (in HTML)
```html
<meta name="robots" content="noai, noimageai">
```

**Note:** Not all AI crawlers respect these. robots.txt is more widely supported.

---

## Decision Framework

| Business Goal | Recommendation |
|--------------|---------------|
| Want to appear in AI search results | Allow: ChatGPT-User, OAI-SearchBot, PerplexityBot, Googlebot |
| Want to be cited as a source | Allow all AI crawlers + create citation-worthy content |
| Want search visibility, no training | Block: GPTBot, Google-Extended, ClaudeBot. Allow: search-specific bots |
| Want maximum content protection | Block all AI crawlers (accept reduced AI search visibility) |
| Want to monetize AI access | Look into licensing programs (AP, NYT model) |

**Key tradeoff:** Blocking AI crawlers protects content but reduces AI search visibility. For most businesses seeking traffic, allowing AI search bots while blocking training bots is the best balance.

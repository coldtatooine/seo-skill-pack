---
name: local-schema-markup
description: This skill should be used when the user asks to "generate schema markup", "add structured data", "JSON-LD for local business", "schema markup generator", "rich results markup", or wants to generate JSON-LD structured data for any schema.org type.
version: 1.0.0
---

# Local Schema Markup Generator

Generate valid JSON-LD structured data markup for local businesses and their web properties. Cover all relevant schema.org types including LocalBusiness, Organization, Service, Product, FAQPage, Event, Review, BreadcrumbList, and more. Output ready-to-paste code with validation.

---

## Core Workflow

### Phase 1 — Information Gathering

Collect business and page details:

1. **Business type** — restaurant, dentist, plumber, law firm, etc.
2. **Business name, address, phone, email, website**
3. **Business hours** (regular + special/holiday)
4. **Geographic service area** (if applicable)
5. **Services or products offered** with descriptions
6. **Page URL** where schema will be placed
7. **Page type** — homepage, service page, location page, blog, FAQ, contact

### Phase 2 — Schema Type Selection

Map page type to required schema types:

| Page Type | Primary Schema | Additional Schema |
|-----------|---------------|-------------------|
| Homepage | LocalBusiness (or subtype) | Organization, WebSite, SearchAction |
| Service Page | Service + LocalBusiness | Offer, AggregateRating |
| Location Page | LocalBusiness + Place | GeoCoordinates, OpeningHours |
| FAQ Page | FAQPage | LocalBusiness (reference) |
| Blog Post | Article + BlogPosting | Author, Organization, BreadcrumbList |
| Product Page | Product | Offer, AggregateRating, Review |
| Contact Page | LocalBusiness + ContactPoint | PostalAddress |
| Event Page | Event | Place, Offer, Performer |
| About Page | Organization + Person | sameAs links |
| Review/Testimonial | Review + LocalBusiness | AggregateRating |

### Phase 3 — Schema Generation

Generate JSON-LD following these rules:

#### LocalBusiness Schema (Core)

Select the most specific schema.org LocalBusiness subtype (e.g., Dentist, Restaurant, Attorney, DaySpa, AutoRepair). Full subtype reference is in `references/schema-templates.md` if needed.

#### Required Properties (LocalBusiness)

Always include:

```json
{
  "@context": "https://schema.org",
  "@type": "Dentist",
  "@id": "https://example.com/#dentist",
  "name": "Business Name",
  "url": "https://example.com",
  "telephone": "+1-555-123-4567",
  "email": "info@example.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main St",
    "addressLocality": "City",
    "addressRegion": "ST",
    "postalCode": "12345",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 40.7128,
    "longitude": -74.0060
  },
  "openingHoursSpecification": [],
  "image": "https://example.com/photo.jpg",
  "priceRange": "$$",
  "sameAs": []
}
```

#### Recommended Properties

Add when available:

- `description` — business description (max 300 chars)
- `areaServed` — service area (GeoCircle, City, or State)
- `hasOfferCatalog` — services/products listing
- `aggregateRating` — average rating + review count
- `review` — individual reviews
- `paymentAccepted` — payment methods
- `currenciesAccepted` — currencies
- `logo` — business logo URL
- `founder` — person/people who founded the business
- `foundingDate` — when business was established

### Phase 4 — Multi-Schema Assembly

For pages requiring multiple schema types, use `@graph`:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "LocalBusiness", ... },
    { "@type": "WebSite", ... },
    { "@type": "BreadcrumbList", ... }
  ]
}
```

Cross-reference entities using `@id`:

```json
{
  "@type": "Service",
  "provider": { "@id": "https://example.com/#business" }
}
```

### Phase 5 — Validation & Output

1. **Validate JSON** — ensure valid JSON syntax (no trailing commas, proper escaping)
2. **Check required fields** — all mandatory properties present per schema type
3. **Verify URLs** — all URLs use https and are absolute
4. **Check types** — correct @type for the business category
5. **Test nesting** — @id references resolve correctly within @graph

Output format:

```html
<script type="application/ld+json">
{generated JSON-LD here}
</script>
```

Include implementation notes:
- Where to place in HTML (inside `<head>`, before `</head>`)
- One `<script type="application/ld+json">` per schema block, or combined with `@graph`
- Test with Google Rich Results Test after implementation

---

## Common Schema Combinations

Quick-reference for typical local business pages:

| Business + Page | Schema Combination |
|----------------|--------------------|
| Any homepage | LocalBusiness + WebSite + SearchAction + BreadcrumbList |
| Restaurant menu | LocalBusiness + Menu + MenuItem |
| Service provider | LocalBusiness + Service + Offer + AggregateRating |
| Multi-location | Organization (parent) + LocalBusiness (per location) |
| Blog on business site | BlogPosting + Organization + BreadcrumbList |
| FAQ section | FAQPage + LocalBusiness reference |
| Event listing | Event + Place + Offer + Organization |

---

## Additional Resources

### Reference Files

> Only read `schema-templates.md` if the user needs a ready-made template for a specific business type. Only read `schema-validation-guide.md` if validation errors occur. Do not read both proactively.

- **`references/schema-templates.md`** — Ready-to-use JSON-LD templates for all common local business types
- **`references/schema-validation-guide.md`** — Detailed validation rules, common errors, and testing instructions

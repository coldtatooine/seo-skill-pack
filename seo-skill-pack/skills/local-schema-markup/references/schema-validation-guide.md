# Schema Markup Validation Guide

## Validation Tools

### Google Rich Results Test
- **URL**: https://search.google.com/test/rich-results
- **Purpose**: Test if schema qualifies for Google rich results
- **Accepts**: URL or code snippet
- **Shows**: Valid items, warnings, errors

### Schema.org Validator
- **URL**: https://validator.schema.org/
- **Purpose**: Validate against full schema.org spec
- **More permissive**: Shows all valid schema, not just Google-supported

### Google Search Console — Rich Results Report
- **Location**: Search Console > Enhancements > [Schema Type]
- **Purpose**: Monitor schema health across entire site
- **Shows**: Valid items, warnings, errors per page

---

## Common Validation Errors

### Syntax Errors

| Error | Cause | Fix |
|-------|-------|-----|
| Invalid JSON | Trailing comma | Remove comma before closing `}` or `]` |
| Invalid JSON | Single quotes | Use double quotes `"` not `'` |
| Invalid JSON | Unescaped characters | Escape `"` as `\"`, newlines as `\n` |
| Missing @context | No context declaration | Add `"@context": "https://schema.org"` |
| Missing @type | No type declaration | Add `"@type": "LocalBusiness"` |

### Property Errors

| Error | Cause | Fix |
|-------|-------|-----|
| Unknown property | Misspelled property name | Check schema.org for correct spelling |
| Wrong value type | String where object expected | Use proper nested object structure |
| Missing required property | Required field absent | Add all required properties for the type |
| Invalid URL | Relative URL or malformed | Use absolute URLs with https:// |
| Invalid date | Wrong format | Use ISO 8601: `YYYY-MM-DD` or `YYYY-MM-DDTHH:MM:SS±HH:MM` |
| Invalid enum | Wrong enumeration value | Use full URL: `https://schema.org/InStock` |

### Google-Specific Warnings

| Warning | Meaning | Action |
|---------|---------|--------|
| "Missing recommended field" | Optional but advised | Add field for better rich results |
| "Page is not indexed" | Google can't access page | Fix indexing issues first |
| "Self-referencing review" | Business reviewing itself | Use only third-party reviews |
| "aggregateRating on non-eligible type" | Rating on wrong schema type | Move to Product, LocalBusiness, or Organization |

---

## Property-Level Validation Rules

### Address (PostalAddress)
- `streetAddress`: full street address including suite/unit
- `addressLocality`: city name only
- `addressRegion`: state/province abbreviation (TX, CA, ON)
- `postalCode`: string, not number (to preserve leading zeros)
- `addressCountry`: ISO 3166-1 alpha-2 code (US, CA, GB)

### Phone (telephone)
- Format: `+1-555-123-4567` (E.164 with country code)
- Alternatively: `+15551234567`
- Must match visible phone on page

### Opening Hours
- Use ISO 8601 day names: `Monday`, `Tuesday`, etc.
- Time format: `HH:MM` in 24-hour (08:00, 17:30)
- For 24-hour businesses: `"opens": "00:00", "closes": "23:59"`
- For closed days: omit from specification (don't set opens/closes)

### GeoCoordinates
- `latitude`: decimal degrees (-90 to 90)
- `longitude`: decimal degrees (-180 to 180)
- Precision: at least 4 decimal places
- Verify coordinates point to actual business location

### URLs
- Always use `https://` (not `http://`)
- Use absolute paths (not relative)
- Ensure URLs return 200 status
- No trailing whitespace

### Images
- Must be accessible (200 status code)
- Supported formats: JPEG, PNG, GIF, SVG, WebP
- Google recommended sizes:
  - Logo: at least 112x112px
  - Images: at least 696px wide
  - Aspect ratio: 16x9, 4x3, or 1x1

### Ratings
- `ratingValue`: number (e.g., "4.8")
- `bestRating`: highest possible (usually "5")
- `worstRating`: lowest possible (usually "1")
- `reviewCount`: integer, total number of reviews
- Must reflect real, third-party reviews

---

## Testing Workflow

### Before Implementation
1. Draft JSON-LD in a text editor
2. Validate JSON syntax (jsonlint.com or similar)
3. Test in Google Rich Results Test (paste code)
4. Fix any errors or warnings
5. Test in Schema.org Validator for completeness

### After Implementation
1. Deploy schema to the page
2. Verify in Google Rich Results Test (via URL)
3. Request indexing in Google Search Console
4. Monitor Rich Results report in Search Console over next 2-4 weeks
5. Address any new errors that appear

### Ongoing Monitoring
- Check Search Console Rich Results monthly
- Re-validate after any content changes
- Update `dateModified` when content changes
- Review aggregate ratings periodically (must match actual ratings)

---

## Schema Implementation Best Practices

### Placement
- Place `<script type="application/ld+json">` inside `<head>` or `<body>`
- Prefer `<head>` for consistency
- One schema block per `<script>` tag OR one block with `@graph`
- Both approaches are valid; `@graph` is cleaner for multiple types

### Performance
- JSON-LD has no impact on page render performance
- Keep schema size reasonable (< 10KB per page)
- Don't duplicate information unnecessarily

### Content Matching
- Schema MUST match visible page content
- Google will penalize/ignore schema that contradicts page content
- If the page says "4.5 stars from 89 reviews", schema must match exactly
- Don't include schema for content not present on the page

### Multi-Page Consistency
- Use consistent `@id` across pages for same entities
- Homepage: define the main LocalBusiness with `@id`
- Other pages: reference with `{ "@id": "https://example.com/#business" }`
- This creates a connected entity graph Google can understand

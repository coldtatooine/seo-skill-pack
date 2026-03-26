# Common Technical SEO Issues & Fixes

## Crawlability Issues

### Missing robots.txt
**Issue**: No robots.txt file at domain root
**Impact**: Medium — crawlers proceed without guidance
**Fix**: Create `/robots.txt` with:
```
User-agent: *
Allow: /

Sitemap: https://example.com/sitemap.xml
```

### Blocked Important Pages
**Issue**: robots.txt blocks key pages from crawling
**Impact**: Critical — pages won't be indexed
**Fix**: Review Disallow rules, ensure important paths are not blocked

### Missing Sitemap
**Issue**: No XML sitemap found
**Impact**: High — crawlers may miss pages
**Fix by CMS**:
- **WordPress**: Install Yoast SEO or RankMath (auto-generates at /sitemap_index.xml)
- **Shopify**: Auto-generated at /sitemap.xml (no action needed)
- **Custom**: Generate with a sitemap tool or code, submit to Search Console

### Redirect Chains
**Issue**: A → B → C → D (multiple hops)
**Impact**: Medium — wastes crawl budget, dilutes link equity
**Fix**: Update redirects to point directly to final destination (A → D)

### Soft 404s
**Issue**: Missing pages return 200 status instead of 404
**Impact**: High — wastes crawl budget on non-existent content
**Fix**: Ensure missing pages return proper 404 status code

---

## Indexing Issues

### Missing Canonical Tags
**Issue**: No `<link rel="canonical">` on pages
**Impact**: Medium — risk of duplicate content issues
**Fix**: Add self-referencing canonical to every page:
```html
<link rel="canonical" href="https://example.com/current-page" />
```

### Accidental Noindex
**Issue**: `<meta name="robots" content="noindex">` on pages that should be indexed
**Impact**: Critical — pages are explicitly excluded from search
**Common causes**:
- Staging/dev noindex not removed before launch
- CMS setting accidentally enabled
- Plugin misconfiguration
**Fix**: Remove the noindex tag, re-submit in Search Console

### Duplicate Content
**Issue**: Same content accessible at multiple URLs
**Impact**: High — search engines don't know which to rank
**Common causes**:
- www vs non-www (both resolve)
- http vs https (both resolve)
- trailing slash vs no trailing slash
- URL parameters creating duplicates
**Fix**:
1. Choose one canonical version
2. 301 redirect all variants to canonical
3. Add canonical tags

---

## Performance Issues

### Unoptimized Images
**Issue**: Large image files slowing page load
**Impact**: High — directly affects LCP
**Fix**:
- Convert to WebP or AVIF format
- Set explicit width and height attributes
- Lazy load below-fold images: `loading="lazy"`
- Use responsive images with `srcset`
- Compress images (aim for < 200KB per image)

### Render-Blocking Resources
**Issue**: CSS/JS files block page rendering
**Impact**: High — delays FCP and LCP
**Fix**:
- Critical CSS: inline above-fold CSS in `<head>`
- Defer non-critical JS: `<script defer>`
- Async non-critical JS: `<script async>`
- Preload key resources: `<link rel="preload">`

### Missing Font Optimization
**Issue**: Web fonts cause layout shift or slow rendering
**Impact**: Medium — affects CLS and FCP
**Fix**:
```css
@font-face {
  font-family: 'CustomFont';
  font-display: swap; /* Critical: prevents invisible text */
  src: url('/fonts/custom.woff2') format('woff2');
}
```
Also preload: `<link rel="preload" href="/fonts/custom.woff2" as="font" type="font/woff2" crossorigin>`

### No Compression
**Issue**: Server not compressing responses
**Impact**: Medium — increases transfer size
**Fix by server**:
- **Apache**: Enable mod_deflate in .htaccess
- **Nginx**: Enable gzip in nginx.conf
- **Cloudflare/CDN**: Usually enabled by default
- **Vercel/Netlify**: Automatic

### Excessive Third-Party Scripts
**Issue**: Too many external scripts (analytics, ads, chat widgets, social)
**Impact**: High — each script adds DNS lookups, connections, and execution time
**Fix**:
1. Audit all third-party scripts
2. Remove unused scripts
3. Defer non-essential scripts
4. Self-host scripts where possible
5. Use `<link rel="dns-prefetch">` for remaining external domains

---

## On-Page SEO Issues

### Missing or Poor Title Tags
**Issue**: No title tag, generic title ("Home"), or poorly optimized
**Impact**: Critical — primary ranking factor and SERP display
**Fix**: Write unique, keyword-rich titles for every page (see Meta Optimizer skill)

### Missing Meta Descriptions
**Issue**: No meta description tag
**Impact**: Medium — Google may generate its own (often poor)
**Fix**: Write unique, compelling descriptions for every page (see Meta Optimizer skill)

### Missing or Multiple H1 Tags
**Issue**: Page has no H1, or has multiple H1 tags
**Impact**: High — H1 signals page topic to search engines
**Fix**: Exactly one H1 per page, containing the primary keyword

### Broken Heading Hierarchy
**Issue**: H3 after H1 (skipping H2), or H1 inside content blocks
**Impact**: Medium — reduces content structure clarity
**Fix**: Follow strict hierarchy: H1 > H2 > H3 > H4 (no skipped levels)

### Images Missing Alt Text
**Issue**: `<img>` tags without `alt` attribute
**Impact**: Medium — missed keyword opportunity, accessibility issue
**Fix**: Add descriptive alt text to all meaningful images:
```html
<img src="dental-office.jpg" alt="Modern dental examination room at Bright Smile Dental in Austin" />
```
Decorative images: `alt=""` (empty, not missing)

### Missing Schema Markup
**Issue**: No structured data on the page
**Impact**: Medium — missing rich result opportunities
**Fix**: Add relevant JSON-LD schema (see Local Schema Markup skill)

---

## Mobile Issues

### Non-Responsive Design
**Issue**: Page doesn't adapt to mobile viewports
**Impact**: Critical — Google uses mobile-first indexing
**Fix**: Implement responsive CSS with media queries or use a responsive framework

### Missing Viewport Meta
**Issue**: No viewport meta tag
**Impact**: Critical — page won't render correctly on mobile
**Fix**: Add to `<head>`:
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

### Small Touch Targets
**Issue**: Buttons/links too small or too close together
**Impact**: Medium — frustrates mobile users
**Fix**: Minimum 48x48px touch targets with at least 8px spacing

### Small Font Size
**Issue**: Body text smaller than 16px on mobile
**Impact**: Medium — users must zoom to read
**Fix**: Set base font size to at least 16px

### Intrusive Interstitials
**Issue**: Full-screen popups on mobile
**Impact**: High — Google penalizes intrusive interstitials
**Allowed**: Age verification, legal requirements, small banners
**Fix**: Use small banners or delayed popups that don't cover content

---

## Security Issues

### Mixed Content
**Issue**: HTTPS page loads HTTP resources (images, scripts, stylesheets)
**Impact**: High — browsers may block resources, show warnings
**Fix**: Update all resource URLs to HTTPS, or use protocol-relative URLs

### Missing Security Headers
**Issue**: Important security headers not set
**Impact**: Medium — reduced security posture
**Fix**: Add headers (in server config or CDN):
```
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Referrer-Policy: strict-origin-when-cross-origin
```

### SSL Certificate Issues
**Issue**: Expired, self-signed, or misconfigured SSL
**Impact**: Critical — browsers show security warning, users leave
**Fix**: Renew certificate, use Let's Encrypt for free SSL, verify configuration

---

## CMS-Specific Issues

### WordPress
| Issue | Fix |
|-------|-----|
| Plugin bloat (20+ plugins) | Audit and remove unused plugins |
| Auto-generated pages (tag, author, date archives) | Noindex with SEO plugin or disable |
| Large database slowing queries | Optimize database, enable object caching |
| Default permalink structure | Change to /%postname%/ |
| Missing breadcrumbs | Enable in Yoast/RankMath |

### Shopify
| Issue | Fix |
|-------|-----|
| Duplicate /collections and /products URLs | Canonical tags (usually auto-handled) |
| Paginated collection pages | Ensure proper canonical and navigation |
| Limited robots.txt control | Use Shopify's robots.txt.liquid |
| Default blog URL structure | Can't change /blogs/ prefix (limitation) |
| Missing alt text on product images | Add in product editor for each image |

### Wix
| Issue | Fix |
|-------|-----|
| JavaScript-heavy rendering | Enable server-side rendering in settings |
| Auto-generated URLs | Customize URL slugs in page settings |
| Limited schema options | Use Wix SEO patterns or custom code embed |
| No direct robots.txt access | Use Wix SEO settings panel |
| Image optimization limited | Pre-optimize images before upload |

# JSON-LD Schema Templates for Local Businesses

## 1. LocalBusiness — Full Template

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://example.com/#business",
  "name": "Business Name",
  "alternateName": "DBA or Common Name",
  "description": "Brief description of the business (max 300 chars)",
  "url": "https://example.com",
  "telephone": "+1-555-123-4567",
  "email": "info@example.com",
  "logo": "https://example.com/logo.png",
  "image": [
    "https://example.com/photo1.jpg",
    "https://example.com/photo2.jpg"
  ],
  "priceRange": "$$",
  "currenciesAccepted": "USD",
  "paymentAccepted": "Cash, Credit Card, Debit Card",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main Street, Suite 100",
    "addressLocality": "Austin",
    "addressRegion": "TX",
    "postalCode": "78701",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 30.2672,
    "longitude": -97.7431
  },
  "areaServed": [
    {
      "@type": "City",
      "name": "Austin"
    },
    {
      "@type": "City",
      "name": "Round Rock"
    }
  ],
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "08:00",
      "closes": "18:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Saturday",
      "opens": "09:00",
      "closes": "14:00"
    }
  ],
  "sameAs": [
    "https://www.facebook.com/businessname",
    "https://www.instagram.com/businessname",
    "https://www.linkedin.com/company/businessname",
    "https://www.yelp.com/biz/businessname"
  ],
  "founder": {
    "@type": "Person",
    "name": "Founder Name"
  },
  "foundingDate": "2010",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "156",
    "bestRating": "5",
    "worstRating": "1"
  },
  "review": [
    {
      "@type": "Review",
      "author": {
        "@type": "Person",
        "name": "John Doe"
      },
      "datePublished": "2026-01-15",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": "5",
        "bestRating": "5"
      },
      "reviewBody": "Excellent service! Highly recommend."
    }
  ]
}
```

## 2. Restaurant Template

```json
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "@id": "https://example.com/#restaurant",
  "name": "Restaurant Name",
  "servesCuisine": ["Italian", "Mediterranean"],
  "menu": "https://example.com/menu",
  "acceptsReservations": true,
  "hasMenu": {
    "@type": "Menu",
    "name": "Main Menu",
    "hasMenuSection": [
      {
        "@type": "MenuSection",
        "name": "Appetizers",
        "hasMenuItem": [
          {
            "@type": "MenuItem",
            "name": "Bruschetta",
            "description": "Toasted bread with tomato and basil",
            "offers": {
              "@type": "Offer",
              "price": "12.00",
              "priceCurrency": "USD"
            }
          }
        ]
      }
    ]
  }
}
```

## 3. Service + Offer Template

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": "https://example.com/services/keyword/#service",
  "name": "Service Name",
  "description": "Description of the service",
  "provider": {
    "@id": "https://example.com/#business"
  },
  "areaServed": {
    "@type": "City",
    "name": "Austin"
  },
  "serviceType": "Service Category",
  "offers": {
    "@type": "Offer",
    "price": "150.00",
    "priceCurrency": "USD",
    "priceSpecification": {
      "@type": "UnitPriceSpecification",
      "price": "150.00",
      "priceCurrency": "USD",
      "unitText": "per session"
    }
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "87"
  }
}
```

## 4. FAQPage Template

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the question?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The answer to the question. Can include <a href=\"https://example.com\">HTML links</a> and basic formatting."
      }
    },
    {
      "@type": "Question",
      "name": "Second question here?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Second answer here."
      }
    }
  ]
}
```

## 5. WebSite + SearchAction Template (Sitelinks Search Box)

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://example.com/#website",
  "name": "Site Name",
  "url": "https://example.com",
  "publisher": {
    "@id": "https://example.com/#business"
  },
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://example.com/search?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
```

## 6. BreadcrumbList Template

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://example.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Services",
      "item": "https://example.com/services"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Specific Service",
      "item": "https://example.com/services/specific-service"
    }
  ]
}
```

## 7. Event Template

```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "Event Name",
  "description": "Event description",
  "startDate": "2026-04-15T09:00:00-05:00",
  "endDate": "2026-04-15T17:00:00-05:00",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "location": {
    "@type": "Place",
    "name": "Venue Name",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "123 Main St",
      "addressLocality": "Austin",
      "addressRegion": "TX",
      "postalCode": "78701",
      "addressCountry": "US"
    }
  },
  "organizer": {
    "@id": "https://example.com/#business"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/event-tickets",
    "price": "50.00",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "validFrom": "2026-03-01"
  },
  "image": "https://example.com/event-photo.jpg"
}
```

## 8. Article / BlogPosting Template

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "@id": "https://example.com/blog/article-slug/#article",
  "headline": "Article Headline (max 110 chars)",
  "description": "Brief summary of the article",
  "datePublished": "2026-03-15",
  "dateModified": "2026-03-20",
  "author": {
    "@type": "Person",
    "name": "Author Name",
    "url": "https://example.com/team/author-name",
    "jobTitle": "Job Title",
    "worksFor": {
      "@id": "https://example.com/#business"
    }
  },
  "publisher": {
    "@id": "https://example.com/#business"
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://example.com/blog/article-slug"
  },
  "image": {
    "@type": "ImageObject",
    "url": "https://example.com/blog/article-image.jpg",
    "width": 1200,
    "height": 630
  },
  "wordCount": 2500,
  "keywords": ["keyword1", "keyword2", "keyword3"]
}
```

## 9. Multi-Location Organization Template

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://example.com/#organization",
  "name": "Parent Company Name",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "sameAs": ["social-urls"],
  "subOrganization": [
    {
      "@type": "LocalBusiness",
      "@id": "https://example.com/locations/downtown/#location",
      "name": "Business - Downtown",
      "address": { "..." : "..." },
      "parentOrganization": { "@id": "https://example.com/#organization" }
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://example.com/locations/north/#location",
      "name": "Business - North",
      "address": { "..." : "..." },
      "parentOrganization": { "@id": "https://example.com/#organization" }
    }
  ]
}
```

## 10. Homepage @graph Example (Combined)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "LocalBusiness",
      "@id": "https://example.com/#business",
      "name": "Business Name",
      "url": "https://example.com",
      "...": "full LocalBusiness properties"
    },
    {
      "@type": "WebSite",
      "@id": "https://example.com/#website",
      "name": "Site Name",
      "url": "https://example.com",
      "publisher": { "@id": "https://example.com/#business" },
      "potentialAction": {
        "@type": "SearchAction",
        "target": {
          "@type": "EntryPoint",
          "urlTemplate": "https://example.com/search?q={search_term_string}"
        },
        "query-input": "required name=search_term_string"
      }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://example.com"
        }
      ]
    }
  ]
}
```

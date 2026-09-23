# Local input and delivery

## Entry points

Specified topic: accept a site, hotspot phrase, source URL, daily-report row, or file. Honor explicit topic selection even if its urgency is below the automatic threshold. If essential sources are missing, locate them with read-only research first. Ask when the event or consumer intent cannot be established; never invent inputs.

Automatic selection: read the report for the specified site and date. Prioritize high writing urgency + medium/high heat + no topic-level human review required + a nonempty writing direction. Inspect actual headers and map fields semantically, not by column position. Within high urgency, immediate/today precedes 24–48 hours; prefer higher heat within equal urgency. Explicit review flags override inference. If review status is absent and cannot be established from the report's agreed rules, do not assume no review is required. If no row qualifies, explain without silently lowering thresholds. Ask for the site if neither the request nor context identifies it.

Use the report root supplied by the user or workspace instructions. In the original SEO workspace, the relative convention is `01_内容矩阵/01_热点获取/日报/`; it is not required on other machines. Use `rg --files` within the configured workspace to locate site/date files, favoring the exact date. Select the site's latest file only when asked for “latest,” record its real date, and never call an old report today's. Do not assume a nonexistent report was generated; request a specified hotspot if needed. Accept XLSX, CSV, online tables, or pasted rows. Read with available tools, using the spreadsheet skill read-only when available; do not modify the report.

Retain site, hotspot phrase, report date, heat, urgency, writing direction, source URLs, and human-review status. Preserve metric definitions: category outbound clicks must not be relabeled as searches for an individual product.

## Product modes

- `public-test`: current local default. Authentic, publicly accessible non-DHgate product pages may be used for testing; disclose this in Chinese notes. This does not authorize external-store recommendations in production.
- `dhgate`: use only after the user supplies usable API documentation, configured authorized read access, or authentic product data. Check fields, SKU/variant, and provenance before recommending. Without an interface, do not guess endpoints, request plaintext secrets, or claim integration.
- When switching modes, reverify images, prices/currencies, CTAs, and recommendation reasoning, not just URLs. Preserve the visual layout while regenerating claims from the new product evidence.

## Saving and deliverables

Use the user's directory if specified. In the original SEO workspace, use the relative convention `01_内容矩阵/01_热点获取/文章打样/<YYYY-MM-DD>-<slug>/` when that parent exists; otherwise use `outputs/<YYYY-MM-DD>-<slug>/` within the current workspace. Never assume another user's absolute home path. Retain only the final pair for this run:

1. `article.html`: complete English page with semantic HTML, title, description, viewport, and a single H1. Use `noindex,nofollow` for local testing. Do not invent a production canonical, author, or Review/Rating schema.
2. `review.md`: brief Chinese review notes, optionally with a compact evidence table. Do not automatically create a five-sheet workbook, long report, or raw-data copy.

Do not silently overwrite existing deliverables. Default to paired versions such as `article-v2.html` and `review-v2.md` unless the user explicitly requests replacement. Store temporary research and validation artifacts in a directory created with `mktemp -d`. Do not delete files from other tasks.

Include only these items in `review.md`:

- Input provenance, site, consumer question, and product mode.
- Chosen task-led structure and a brief reason; refined product-retrieval tags and English query combinations (relevant category/IP/style/scenario/required attributes/preferences/exclusions only). Keep selection targets distinct from verified SKU facts.
- Same-intent articles actually read and specific added value, with URLs and brief explanations; do not claim coverage of the entire SERP.
- A compact gain record: added answer, judgment changed, evidence/conditions, body location, and unresolved questions. Separately assess valid-information retention (no prior-draft baseline when applicable), important-gap closure, and supported new answers. Target upper-moderate (中等偏上); report body quality separately from technical checks and human-review status. Keep full working plans temporary rather than adding deliverable files.
- Key product fields used, evidence URLs, retrieval dates, distinctions between facts/image observations/editorial inference, and unverified fields.
- Status using exactly one of these Chinese labels: `待人工审阅` (awaiting human review), `正文完成待补商品` (body complete; products pending), or `研究受阻待补证据` (research blocked; evidence pending). These are not publication approvals.
- A few human-review priorities and checks performed/not performed, including the default omission of site-similarity checks.

Keep workflow text such as “placeholder image,” “waiting for API,” or “the reviewer will see this” out of the article. When a product is missing, use a nonrendered comment of the form `<!-- PRODUCT_MODULE_SLOT: concrete selection requirements in English -->`, replacing the example text with actual requirements. Document missing fields in the notes; do not add fictional cards, prices, or dead links. Do not call an outline a complete article merely to produce two files.

## Test sample

If the user supplies a prior sample, use it only to understand useful presentation and analytical specificity. Do not copy its section structure, prices, product choices, or outdated conclusions. No historical sample is bundled or required. Current rules—no forced compression, no default product count, and unknown does not mean absent—override residual sample wording.

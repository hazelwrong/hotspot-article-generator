---
name: hotspot-product-blog
description: Turn specified trends or daily hotspot selections into product-decision blogs for North American English-speaking consumers across DHgate's six sites. Research same-intent content for added value, verify products, and deliver English HTML plus brief Chinese review notes. Use for new trend-led articles and revisions to this skill's drafts, not trend collection, scheduled delivery, or automatic publishing.
---

# Hotspot Product Blog

Source: [hotspot-article-generator](https://github.com/hazelwrong/hotspot-article-generator), branch `main`, directory `hotspot-product-blog/`. Keep the installed skill and this source synchronized when updating; do not publish workspace reports, article drafts, credentials, or personal paths.

Local trial version. Turn screened hotspots into useful what / why / how-to / guide / comparison / review / explainer / tutorial / inspiration articles. Product content is not limited to reviews: the trend opens the conversation; consumer decisions form the substance. Deliver drafts for an intern or editor to inspect, never automatically publish.

## Working agreement

- Address individual consumers in North America and other English-speaking markets. Write natural American English articles and Chinese review notes. The consumer intent must fit the target site.
- Accept either a specified hotspot or automatic selection from a specified daily report. Default to one article; batch only the number requested, not the entire report.
- Inherit the report's heat signals and writing direction. Do not rerun trend discovery, expiration checks, or popularity validation. Factual, product, and technical claims used in the article still require evidence; an authoritative discovery source does not validate every inference.
- Do not search for or merge similar on-site articles or make publication decisions. The user handles these later. Never claim duplicate checks passed.
- Do not modify older skills, daily reports, automations, Feishu, CMS, or company API configuration. Do not integrate a DHgate API that has not been supplied.
- Deliver only English HTML and brief Chinese review notes. Keep research scripts, screenshots, and debugging artifacts in a temporary directory for this run, not scattered around the project.

## Workflow and editable prompts

Read the appropriate references as work progresses. Every article passes through all six stages, but these are not six mandatory article sections. Return to earlier stages when research or revision requires it.

1. Read [Local input and delivery](references/local-contract.md) and [Site scope](references/site-scope.md) to establish input, target site, product mode, and output location.
2. Read [01 Turn the trend into a consumer question](references/01-topic.md) to define the article task and key questions.
3. Read [02 Information-gain planning and research](references/02-research.md): diagnose current coverage, separate defects from gain opportunities, plan added answers before drafting, then conduct question-led research including relevant original use feedback. Keep evidence scope and independence explicit.
4. Read [03 Turn product evidence into recommendations](references/03-products.md): derive retrieval tags from the consumer task before sourcing; verify SKUs, explain tradeoffs, and preserve unknowns. Refine the gain plan as product evidence develops.
5. Read [04 Structure and writing](references/04-writing.md): write a complete article around the key questions.
6. Read [05 Product and image integration](references/05-presentation.md): assemble navigation, visual product modules, and useful images. Reuse [CSS](assets/article.css) when helpful; adapt structure to intent.
7. Read [06 Quality review and revision](references/06-review.md): read the integrated full text and evidence, separately assess information retention, important gaps, and added answers; fix repetition, template-driven structure, and overclaims before validating delivery.

These reusable prompts were distilled from the Aviator vs. Barn Jacket test process and user feedback. They are not a claim that an unchanged, verbatim historical master prompt exists. That sample supports the research–explanation–product–visualization approach; it does not establish that all six sites have been tested.

## Non-negotiable boundaries

- Similar external products can inform analytical dimensions, but their materials, care, measurements, performance, reviews, or test results must not be transferred to a DHgate product.
- Unverified performance means insufficient evidence to recommend for that purpose, not proof that the product lacks that capability. Unknowns are not cons; actual design tradeoffs are.
- Target at least upper-moderate information gain (中等偏上): key questions adequately answered, important facts supported, differences translated into concrete tradeoffs, and no core misleading conclusion. Judge against actually read same-intent content, not just hotspot news. Rewriting, aggregation, and improved formatting alone are insufficient.
- Never invent prices, stock, certifications, tests, author experience, ratings, or internal data. Structural analysis can support a recommendation, but must not masquerade as hands-on testing.
- Do not impose a word count, a 15–20% reduction target, a fixed product count, or a fixed structure. Retain necessary repetition; revise repetition that adds no value.
- Choose article structure and product placement from the reader task, not the site name or a default comparison followed by two cards. Shared visual styling is allowed; substantive benefits/tradeoffs need not use identical blocks. Derive internal product-search tags before sourcing and include refined tags in the Chinese notes.
- New images are optional, not a body-quality gate. The text must independently answer the reader's task; existing image mismatches and nonexistent image references still require handling.
- When no product qualifies, a complete body with products pending is acceptable. When core evidence is missing, do not claim quality clearance or readiness to publish. Use the delivery statuses below.

## Validation

Run `python3 scripts/check_article.py /absolute/path/article.html` to check basic HTML structure, contents anchors, image alt text, product CTAs, and debugging text. This is a static check, not proof of truth, semantic quality, image availability, or live indexability.

Preview desktop and mobile layouts, images, and navigation when tools permit. If preview access is blocked, respect the restriction and document the unperformed check; do not bypass it. The user will request real writing tests for other sites later. Do not add articles or external actions automatically.

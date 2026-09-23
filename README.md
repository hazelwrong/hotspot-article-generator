# Hotspot Article Generator

A research-first Codex skill for turning selected trends into useful product-decision articles for English-speaking consumers.

## Included skill

[hotspot-product-blog/SKILL.md](hotspot-product-blog/SKILL.md)

The installed skill name remains `hotspot-product-blog`. The repository name is `hotspot-article-generator`.

- Six site scopes: Fashion, Sports, Beauty, Tech, Home & Garden, and Lifestyle.
- Two inputs: a specified trend or selections from a supplied daily report.
- Independent information-gain planning, targeted research, original feedback analysis, and evidence-aware recommendations.
- Product retrieval tags covering relevant category, IP/entity, style, scenario, requirements, preferences, exclusions, and English queries.
- Task-led structure and product placement, not a fixed two-product template.
- English HTML plus concise Chinese review notes; no automatic publishing.

## Installation

Copy the complete `hotspot-product-blog` directory into your Codex skills directory (normally `~/.codex/skills/`). If already installed, review differences before replacing it; preserve local customizations.

Invoke `$hotspot-product-blog` with a site, trend/source or report location, product data/mode, and output directory. For example:

> Use $hotspot-product-blog for a Home & Garden article about the trend and source I provide. Research the consumer decision, generate product-search tags, use verified public product pages for a local test, and save English HTML plus Chinese review notes in my chosen output directory. Do not publish.

Supply actual trend evidence; this skill is not a trend collector or scheduled delivery service. Workspace report/source locations are optional conventions, not included data.

## Product and image boundaries

Public product pages may be used for local testing. DHgate mode requires authentic product records or a separately supplied authorized API; no credentials, connector, API integration, or platform publishing capability is included. Product claims cannot be copied across SKUs.

Use imagery within the user's actual authorization or applicable license. Public visibility does not establish reuse rights.

## Validation

Python 3 is needed only for the optional static HTML checker:

```sh
python3 hotspot-product-blog/scripts/check_article.py /absolute/path/article.html
```

This checks HTML structure, anchors, image attributes, and CTA format—not evidence quality, product performance, remote asset availability, or publication readiness. Research, reasoning, and editorial acceptance are performed by the executing LLM. The skill does not select or call a separate model API.

## Editing and synchronization

Edit the six prompts in `hotspot-product-blog/references/` for topic selection, research, products, writing, presentation, and review. The installed skill and this source directory should stay synchronized. Source repository: https://github.com/hazelwrong/hotspot-article-generator (branch: `main`).

This repository contains instructions, a CSS asset, and a checker only. It excludes private reports, article drafts, account data, and temporary research artifacts.

No license has been selected for this repository; public visibility alone does not grant a general reuse license.


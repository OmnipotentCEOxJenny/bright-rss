# Changelog

## 1.0.2 (2026-10-22)
- Example feed: the CutList item now points to the renamed plugin, Scene Order (github.com/OmnipotentCEOxJenny/sceneorder).

## 1.0.1 (2026-10-22)
- Example feed (`examples/feed.json`, `examples/feed.xml`): the PlanPilot item now points to the renamed plugin, PlanOmega (github.com/OmnipotentCEOxJenny/planomega).

## 1.0.0 (2026-10-22)
- First version: skills `bright-rss-build` and `bright-rss-check`, rule `pillars-and-scope.mdc`, optional builder and checker `scripts/bright_rss.py`, example feed of real plugin releases, plain-language README.
- Format reference: RSS 2.0 specification (RSS Advisory Board).
- Tests: `tests/check_frontmatter.py` and `tests/test_feed.py`.
- 40 search keywords (single words lowercase, joined words PascalCase, no hyphens, Bright RSS-specific, per Rob's keyword rules) in the manifest plus `keywords.md`; 23 machine-translated summaries (not native-reviewed).
- Local tests only; not tested in-app. Not submitted to the marketplace.

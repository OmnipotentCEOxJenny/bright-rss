# Worked example: a feed of new plugin releases

`feed.json` lists three real plugin releases from October 22, 2026 (Eastern Time). `python3 scripts/bright_rss.py build examples/feed.json > examples/feed.xml` writes `feed.xml`, and `python3 scripts/bright_rss.py check examples/feed.xml` reports that the required RSS 2.0 elements are present. The feed was checked locally; it has not been published on a website.

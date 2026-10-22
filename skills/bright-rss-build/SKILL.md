---
name: bright-rss-build
description: Build an RSS 2.0 feed from the user's own posts, episodes or announcements, and explain how to publish it. Use when a user wants an RSS feed, a podcast feed, a blog feed or a way for people to subscribe to updates.
---

Follow `rules/pillars-and-scope.mdc`. Answer in the user's language.

1. **Channel details:** the feed's title, the website link (absolute https URL), a one-sentence description and the language code (for example en-us).
2. **Items:** for each post or episode: title, link, a short description, and the publish date with its time zone (for example 2026-10-22T14:00:00-04:00).
3. Save them as JSON in the format shown in `scripts/bright_rss.py` and run `python3 scripts/bright_rss.py build feed.json > feed.xml`. Dates are written in RFC 822 form, each item gets a guid (its link unless you give one), and lastBuildDate is the newest item date.
4. **Publish:** upload `feed.xml` to the website and link it from the home page with `<link rel="alternate" type="application/rss+xml" href="/feed.xml">`.
5. Then run `bright-rss-check`.

Reference: the RSS 2.0 specification, RSS Advisory Board, https://www.rssboard.org/rss-specification

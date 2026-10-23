---
name: bright-rss-check
description: Check an RSS 2.0 feed for its required elements, date formats, absolute links and unique guids. Use when a user asks to check, fix or validate an RSS feed.
---

Follow `rules/scope.mdc`. Answer in the user's language.

1. Run `python3 scripts/bright_rss.py check feed.xml` when Python is available.
2. Check the root is `<rss version="2.0">` with one `<channel>`.
3. Check the channel has `title`, `link` (absolute URL) and `description`.
4. Check each item has a title or a description, absolute links, an RFC 822 `pubDate` and a unique `guid`.
5. Report each problem with the exact fix. This check does not fetch the feed or its links; open them yourself to confirm they work.

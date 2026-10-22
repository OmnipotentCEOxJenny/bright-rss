# Bright RSS

Bright RSS helps your AI assistant make an RSS feed, a small file on your website that lets people follow your blog, podcast or announcements in a feed reader app. You give it your posts: title, link, a short summary and the date. It writes the feed file in the standard RSS 2.0 format and checks it has every required part, the dates are in the right form, and no entry is listed twice. Why would you want this? A feed lets followers see every update, in order, without relying on a social media algorithm. It's free.

![Bright RSS logo](assets/logo.png)

## Project status: done, pending, uncertain
**Done**
- 2026-10-22: v1.0.0 built and pushed to GitHub. Local tests: manifest valid JSON and valid against Cursor's plugin schema, skill and rule front matter valid (`tests/check_frontmatter.py`), and `tests/test_feed.py` confirms the example feed builds and checks clean with RFC 822 dates, matches `examples/feed.xml`, and that a broken feed's four problems are caught.

**Pending**
- Not tested inside Cursor or Grok yet (no in-app test has been done).
- Not submitted to the marketplace.
- Translated summaries are machine-made and not reviewed by native speakers.

## Quick start
1. Install (see Installation).
2. Ask: "Make an RSS feed for my blog from these three posts."
3. Then ask: "Check my feed.xml."

## Installation
Install from this repository: https://github.com/OmnipotentCEOxJenny/bright-rss (Cursor plugin format: `.cursor-plugin/plugin.json`, `skills/`, `rules/`). Free. No API keys, no accounts, no paid services. The optional builder and checker need only Python 3 (standard library).

## Testing
1. `python3 tests/check_frontmatter.py` (needs PyYAML).
2. `python3 tests/test_feed.py`. Expected: PASS.
3. Compare with `examples/`.

## Search keywords
BrightRss, JennyEcho, OmnipotentCeo, rss, feed, feeds, syndication, rss2, xml, podcast, ShowNotes, newsletter, blog, blogging, subscribe, subscribers, FeedReader, NewsFeed, channel, items, episodes, PubDate, guid, validator, validation, microblog, announcements, ChangelogFeed, ReleaseNotes, website, aggregator, headlines, WebFeed, followers, RssFeed, IndieWeb, NoAlgorithm, XmlFeed, entries, permalinks. The full list with plain-word meanings is in [keywords.md](keywords.md).

## Credits
- Inventor and publisher: Rob Domaine / Omnipotent Media LLC
- Builder: Jenny Echo
- Format: the RSS 2.0 specification published by the RSS Advisory Board (https://www.rssboard.org/rss-specification). Bright RSS is independent and not endorsed by the RSS Advisory Board.

## Rob Domaine's four pillars
1. Trustworthy, honest, real data, truthful: never invent; anything unchecked is marked UNVERIFIED.
2. Use only legitimate means: free, legitimate tools and sources only.
3. Double-check everything: results are checked before they are called done.
4. Stay within the law and rules always: local, county, state, federal and platform rules.

## Components
- `skills/bright-rss-build`: build a feed from the user's posts.
- `skills/bright-rss-check`: check a feed's required parts.
- `scripts/bright_rss.py`: optional builder and checker (standard library only).
- `examples/`: a real feed of plugin releases.
- `tests/`: front-matter check and functional feed test.
- `rules/pillars-and-scope.mdc`: the pillars and scope.
- `keywords.md`: the search keyword list.

## Languages
The AI answers in the user's language and keeps commands, file names and code unchanged. Summaries in 23 languages are in [TRANSLATIONS.md](TRANSLATIONS.md). They are machine translations, not yet reviewed by native speakers; the English text is authoritative.

## License
MIT. See `LICENSE`.

## Honest assessment: what this plugin cannot do
- It has not been tested inside Cursor or Grok yet; only local tests on one computer have been run.
- It does not host or publish your feed; you upload the file to your own website.
- The checker covers RSS 2.0's required elements and common mistakes; it is not a full validator and does not check Atom or podcast-directory extras such as iTunes tags.
- It does not fetch your links, so a broken link will not be caught unless you open it.
- It is not legal advice about republishing content.
- Marketplace: not submitted; it is not an approved listing.
- Translations are machine-made and not reviewed by native speakers.
- Rules and compliance: it follows all local, county, state and federal laws and every platform's rules, uses no paid services, never bypasses logins or security settings, and never claims a feature it does not have.

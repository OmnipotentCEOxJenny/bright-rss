#!/usr/bin/env python3
"""Functional test: build the example feed, confirm it checks clean and keeps every item with an
RFC 822 date, and confirm a broken feed (no channel link, relative item link, duplicate guid, bad date) is caught."""
import json, pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root / "scripts"))
import bright_rss as b
import xml.etree.ElementTree as ET
feed = json.load(open(root / "examples/feed.json", encoding="utf-8"))
xml = b.build(feed)
probs = b.check(xml)
items = ET.fromstring(xml).find("channel").findall("item")
print("example problems:", probs, "items:", len(items), "first date:", items[0].findtext("pubDate"))
ok = not probs and len(items) == len(feed["items"]) and items[0].findtext("pubDate").endswith("-0400")
ok &= xml == (root / "examples/feed.xml").read_text(encoding="utf-8")
broken = ('<rss version="2.0"><channel><title>T</title><description>D</description>'
          '<item><title>a</title><link>/post</link><guid>1</guid></item>'
          '<item><title>b</title><guid>1</guid><pubDate>yesterday</pubDate></item></channel></rss>')
bp = b.check(broken); print("broken feed problems:", bp)
ok &= len(bp) == 4
print("PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)

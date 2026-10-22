#!/usr/bin/env python3
"""Bright RSS feed builder and checker (standard library only).
Build:  python3 scripts/bright_rss.py build FEED.json > feed.xml
Check:  python3 scripts/bright_rss.py check feed.xml
FEED.json = {"title": "...", "link": "https://...", "description": "...", "language": "en-us",
             "items": [{"title": "...", "link": "https://...", "description": "...", "date": "2026-10-22T14:00:00-04:00", "guid": "optional"}]}
Builds an RSS 2.0 feed and checks one against the RSS 2.0 specification's required elements:
channel title, link and description; each item has a title or a description; dates in RFC 822 form;
links are absolute http(s) URLs; guids are unique. Exit 0 = ok, 1 = problems, 2 = usage error.
It does not fetch anything from the internet and is not a full validator."""
import json, re, sys, datetime
import xml.etree.ElementTree as ET
from email.utils import format_datetime, parsedate_to_datetime

def build(feed):
    rss = ET.Element("rss", version="2.0")
    ch = ET.SubElement(rss, "channel")
    for k in ("title", "link", "description", "language"):
        if feed.get(k): ET.SubElement(ch, k).text = feed[k]
    ET.SubElement(ch, "generator").text = "Bright RSS"
    dates = []
    for it in feed.get("items", []):
        el = ET.SubElement(ch, "item")
        for k in ("title", "link", "description"):
            if it.get(k): ET.SubElement(el, k).text = it[k]
        g = it.get("guid") or it.get("link")
        if g: ET.SubElement(el, "guid", isPermaLink="true" if g == it.get("link") else "false").text = g
        if it.get("date"):
            d = datetime.datetime.fromisoformat(it["date"])
            if d.tzinfo is None: raise ValueError(f"date {it['date']!r} needs a time zone offset, e.g. -04:00")
            dates.append(d); ET.SubElement(el, "pubDate").text = format_datetime(d)
    if dates:
        lb = ET.Element("lastBuildDate"); lb.text = format_datetime(max(dates)); ch.insert(3, lb)
    ET.indent(rss)
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(rss, encoding="unicode") + "\n"

def check(xml_text):
    probs = []
    try: root = ET.fromstring(xml_text)
    except ET.ParseError as e: return [f"not well-formed XML: {e}"]
    if root.tag != "rss" or root.get("version") != "2.0": probs.append("root must be <rss version=\"2.0\">")
    ch = root.find("channel")
    if ch is None: return probs + ["missing <channel>"]
    for k in ("title", "link", "description"):
        if not (ch.findtext(k) or "").strip(): probs.append(f"channel is missing required <{k}>")
    url = re.compile(r"https?://[^\s]+$")
    if ch.findtext("link") and not url.match(ch.findtext("link").strip()): probs.append("channel <link> must be an absolute http(s) URL")
    seen = set()
    for i, it in enumerate(ch.findall("item"), 1):
        if not (it.findtext("title") or it.findtext("description")): probs.append(f"item {i}: needs a <title> or a <description>")
        l = it.findtext("link")
        if l and not url.match(l.strip()): probs.append(f"item {i}: <link> must be an absolute http(s) URL")
        d = it.findtext("pubDate")
        if d:
            try: parsedate_to_datetime(d)
            except (TypeError, ValueError): probs.append(f"item {i}: <pubDate> {d!r} is not an RFC 822 date")
        g = it.findtext("guid")
        if g:
            if g in seen: probs.append(f"item {i}: duplicate <guid> {g}")
            seen.add(g)
    return probs

def main(argv):
    if len(argv) < 3 or argv[1] not in ("build", "check"): print(__doc__); return 2
    if argv[1] == "build":
        out = build(json.load(open(argv[2], encoding="utf-8")))
        probs = check(out); sys.stdout.write(out)
        for p in probs: print("PROBLEM:", p, file=sys.stderr)
        return 1 if probs else 0
    probs = check(open(argv[2], encoding="utf-8").read())
    print("feed ok (required RSS 2.0 elements present)" if not probs else "\n".join("PROBLEM: " + p for p in probs))
    return 1 if probs else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))

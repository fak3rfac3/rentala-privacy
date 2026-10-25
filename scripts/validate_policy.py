#!/usr/bin/env python3
"""Dependency-free structural checks for Rentala's privacy policy page."""

from html.parser import HTMLParser
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "index.html"


class PolicyParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.title_depth = 0
        self.title = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag == "title":
            self.title_depth += 1

    def handle_endtag(self, tag):
        if tag == "title" and self.title_depth:
            self.title_depth -= 1

    def handle_data(self, data):
        if self.title_depth:
            self.title.append(data)

    def error(self, message):
        self.errors.append(message)


def main():
    if not POLICY.is_file():
        print("ERROR: index.html is missing", file=sys.stderr)
        return 1

    source = POLICY.read_text(encoding="utf-8")
    parser = PolicyParser()
    try:
        parser.feed(source)
        parser.close()
    except Exception as error:  # HTMLParser errors are reported as validation failures.
        parser.errors.append(str(error))

    if not source.lower().startswith("<!doctype html>"):
        parser.errors.append("missing HTML5 doctype")
    if not "Rentala" in "".join(parser.title):
        parser.errors.append("page title must identify Rentala")
    if '<html lang="en">' not in source:
        parser.errors.append('document should declare lang="en"')

    for href in parser.links:
        if href.startswith("#") and href[1:] not in parser.ids:
            parser.errors.append(f"broken in-page link: {href}")
        elif not href.startswith(("https://", "http://", "mailto:", "#")):
            target = (ROOT / href.split("#", 1)[0]).resolve()
            if not target.is_relative_to(ROOT) or not target.is_file():
                parser.errors.append(f"broken local link: {href}")

    if parser.errors:
        for error in parser.errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Validated {POLICY.relative_to(ROOT)} ({len(parser.links)} links checked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

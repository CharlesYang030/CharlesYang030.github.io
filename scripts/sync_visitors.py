"""Export aggregate country counts; never download individual visitor records."""

import argparse
from datetime import datetime, timezone
from html import unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://s01.flagcounter.com/countries/5FQV/"


class CountryTableParser(HTMLParser):
    """Read country cells without depending on the destination of name links."""

    def __init__(self):
        super().__init__()
        self.rows = []
        self.countries = {}
        self.text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "tr":
            self.rows.append({"cells": [], "cell": None, "flag": None})
        elif self.rows:
            row = self.rows[-1]
            if tag == "td":
                row["cell"] = []
                row["cells"].append(row["cell"])
            elif tag == "a" and row["cell"] is not None:
                match = re.search(r"(?:^|\s)flag-([a-z]{2})-png(?:\s|$)", attrs.get("class", ""), re.I)
                if match:
                    row["flag"] = (match.group(1).upper(), len(row["cells"]) - 1)

    def handle_data(self, data):
        self.text.append(data)
        if self.rows and self.rows[-1]["cell"] is not None:
            self.rows[-1]["cell"].append(data)

    def handle_endtag(self, tag):
        if not self.rows:
            return
        if tag == "td":
            self.rows[-1]["cell"] = None
        elif tag == "tr":
            row = self.rows.pop()
            if row["flag"] is None:
                return
            code, index = row["flag"]
            cells = [" ".join("".join(cell).split()) for cell in row["cells"]]
            if len(cells) <= index + 2:
                raise ValueError("Incomplete country row; keeping previous data")
            name, count = cells[index + 1:index + 3]
            count = count.replace(",", "")
            if not name or not count.isdigit() or code in self.countries:
                raise ValueError("Invalid or duplicate country row; keeping previous data")
            self.countries[code] = {"code": code, "name": name, "visitors": int(count)}


def parse_countries(html):
    parser = CountryTableParser()
    parser.feed(html)
    parser.close()
    total = re.search(r"Countries\s+\d+\s*[-–]\s*\d+\s+of\s+(\d+)", " ".join(parser.text))
    if not total or not parser.countries:
        raise ValueError("Country statistics unavailable; keeping previous data")
    return parser.countries, int(total.group(1))


def fetch_html(url):
    request = Request(url, headers={"User-Agent": "QihaoHomepage/1.0 (aggregate visitor map)"})
    for attempt in range(3):
        try:
            with urlopen(request, timeout=20) as response:
                return response.read().decode("utf-8", errors="replace")
        except (URLError, TimeoutError, ConnectionError) as error:
            if isinstance(error, HTTPError) and error.code not in (408, 429, 500, 502, 503, 504):
                raise
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)


def collect_countries():
    pending = [SOURCE]
    seen = set()
    countries = {}
    expected = None
    while pending and len(seen) < 20:
        url = pending.pop(0)
        if url in seen:
            continue
        seen.add(url)
        html = fetch_html(url)
        page, expected = parse_countries(html)
        countries.update(page)
        if len(countries) >= expected:
            break
        # Follow numbered pagination links, excluding sort and missing-country views.
        for href in re.findall(r'href=[\"\']?([^\s>\"\']+)', html, re.I):
            link = urljoin(url, unescape(href))
            parsed = urlparse(link)
            if (parsed.scheme == "https" and parsed.netloc == "s01.flagcounter.com"
                    and parsed.path == "/countries/5FQV/"
                    and re.fullmatch(r"(?:[a-z_]+=)?\d+", parsed.query)):
                if link not in seen and link not in pending:
                    pending.append(link)
    if len(countries) != expected:
        raise ValueError("Incomplete country list; keeping previous data")
    return sorted(countries.values(), key=lambda item: (-item["visitors"], item["name"]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "site-assets/visitors.json")
    args = parser.parse_args()
    positions = json.loads((ROOT / "site-assets/visitor-country-positions.json").read_text())
    countries = collect_countries()
    for country in countries:
        if country["code"] in positions:
            country["position"] = positions[country["code"]]
    previous = json.loads(args.output.read_text()) if args.output.exists() else {}
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    unchanged = previous.get("countries") == countries
    if unchanged and previous.get("checkedAt", "")[:10] == now[:10]:
        print("Visitor locations unchanged; already checked today")
        return
    data = {
        "source": SOURCE,
        "since": "2026-09-28",
        "updatedAt": previous["updatedAt"] if unchanged else now,
        "checkedAt": now,
        "countries": countries,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(f"Saved {len(countries)} countries and regions")


if __name__ == "__main__":
    main()

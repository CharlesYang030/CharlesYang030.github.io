"""Export aggregate country counts; never download individual visitor records."""

import argparse
from datetime import datetime, timezone
from html import unescape
import json
from pathlib import Path
import re
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://s01.flagcounter.com/countries/5FQV/"


def parse_countries(html):
    countries = {}
    for row in re.findall(r"<tr\b[^>]*>(.*?)</tr>", html, re.S | re.I):
        match = re.search(
            r'href=[\"\']?/factbook/([a-z]{2})/5FQV[^>]*>(.*?)</a>'
            r'.*?</td>\s*<td\b[^>]*>(.*?)</td>', row, re.S | re.I,
        )
        if not match:
            continue
        code, name, count = match.groups()
        name = unescape(re.sub(r"<[^>]*>", "", name)).strip()
        count = re.sub(r"<[^>]*>", "", count).strip().replace(",", "")
        if not count.isdigit() or not name:
            raise ValueError("Unexpected country count format; keeping previous data")
        countries[code.upper()] = {"code": code.upper(), "name": name, "visitors": int(count)}
    total = re.search(r"Countries\s+\d+\s*-\s*\d+\s+of\s+(\d+)", html)
    if not total or not countries:
        raise ValueError("Country statistics unavailable; keeping previous data")
    return countries, int(total.group(1))


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
        request = Request(url, headers={"User-Agent": "QihaoHomepage/1.0 (aggregate visitor map)"})
        with urlopen(request, timeout=30) as response:
            html = response.read().decode("utf-8", errors="replace")
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
    if previous.get("countries") == countries:
        print("Visitor locations unchanged")
        return
    data = {
        "source": SOURCE,
        "since": "2026-09-28",
        "updatedAt": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "countries": countries,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(f"Saved {len(countries)} countries and regions")


if __name__ == "__main__":
    main()

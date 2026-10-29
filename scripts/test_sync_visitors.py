import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError

from scripts import sync_visitors as sync


def row(code="sg", name="Singapore", count="1,234", legacy=False):
    href = f"/factbook/{code}/5FQV" if legacy else f"https://en.wikipedia.org/wiki/Outline_of_{name}"
    return f'''<tr><td>1.</td><td></td>
      <td><a class="flag-{code}-png" href="https://en.wikipedia.org/wiki/Flag_of_{name}"><img></a></td>
      <td><a href="{href}"><u>{name}</u></a></td><td><font>{count}</font></td>
      <td><a href="/detail30/{code}/5FQV">Chart</a></td></tr>'''


def page(rows, total=1, links=""):
    return f'<table><tr><td><table><tr><td>Countries 1 - 1 of {total}.</td></tr>{rows}</table></td></tr></table>{links}'


class VisitorSyncTests(unittest.TestCase):
    def test_legacy_and_wikipedia_links(self):
        for legacy in (True, False):
            countries, total = sync.parse_countries(page(row(legacy=legacy)))
            self.assertEqual(total, 1)
            self.assertEqual(countries["SG"], {"code": "SG", "name": "Singapore", "visitors": 1234})

    def test_nested_region_rows_are_not_countries(self):
        regions = '<tr id="hidden_us"><td><table><tr><td>California</td><td>99</td></tr></table></td></tr>'
        countries, total = sync.parse_countries(page(row("us", "United States") + regions + row(), 2))
        self.assertEqual(set(countries), {"US", "SG"})
        self.assertEqual(total, 2)

    def test_entities_and_markup(self):
        countries, _ = sync.parse_countries(page(row(name="Trinidad &amp; Tobago")))
        self.assertEqual(countries["SG"]["name"], "Trinidad & Tobago")

    def test_invalid_responses_are_rejected(self):
        for html in ("<html>Service unavailable</html>", page(row(count="unknown")), page(row() + row(), 2)):
            with self.assertRaises(ValueError):
                sync.parse_countries(html)

    def test_pagination(self):
        first = page(row(), 2, '<a href="?2">2</a><a href="?missing">Missing</a><a href="https://example.com/?3">3</a>')
        second = page(row("us", "United States", "2"), 2)
        with patch.object(sync, "fetch_html", side_effect=[first, second]) as fetch:
            self.assertEqual(len(sync.collect_countries()), 2)
            self.assertEqual(fetch.call_args_list[1].args[0], sync.SOURCE + "?2")

    def test_partial_data_does_not_overwrite_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "visitors.json"
            original = '{"countries": [{"code": "US"}]}\n'
            target.write_text(original)
            with patch("sys.argv", ["sync_visitors.py", "--output", str(target)]), patch.object(sync, "fetch_html", return_value=page(row(), 2)):
                with self.assertRaises(ValueError):
                    sync.main()
            self.assertEqual(target.read_text(), original)

    def test_network_retries_are_bounded(self):
        with patch.object(sync, "urlopen", side_effect=URLError("timeout")) as fetch, patch.object(sync.time, "sleep"):
            with self.assertRaises(URLError):
                sync.fetch_html(sync.SOURCE)
            self.assertEqual(fetch.call_count, 3)
        with patch.object(sync, "urlopen", side_effect=HTTPError(sync.SOURCE, 404, "Not Found", {}, None)) as fetch:
            with self.assertRaises(HTTPError):
                sync.fetch_html(sync.SOURCE)
            self.assertEqual(fetch.call_count, 1)

    def test_unchanged_counts_record_freshness_once_per_day(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "visitors.json"
            with patch("sys.argv", ["sync_visitors.py", "--output", str(target)]), patch.object(sync, "collect_countries", return_value=[{"code": "SG", "name": "Singapore", "visitors": 1}]):
                sync.main()
                data = json.loads(target.read_text())
                data["updatedAt"] = data["checkedAt"] = "2026-09-28T00:00:00+00:00"
                target.write_text(json.dumps(data))
                sync.main()
                new = json.loads(target.read_text())
                self.assertEqual(new["updatedAt"], data["updatedAt"])
                self.assertNotEqual(new["checkedAt"], data["checkedAt"])
                content = target.read_bytes()
                sync.main()
                self.assertEqual(target.read_bytes(), content)


if __name__ == "__main__":
    unittest.main()

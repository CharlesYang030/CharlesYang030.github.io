"""Build the atlas assets from Natural Earth land and country GeoJSON files."""

import json
from pathlib import Path
import sys

assets = Path(__file__).resolve().parents[1] / "site-assets"
land = json.loads(Path(sys.argv[1]).read_text())
countries = json.loads(Path(sys.argv[2]).read_text())


def project(lon, lat):
    return round((lon + 180) * 2, 2), round((85 - lat) * 2, 2)


parts = [
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 300">',
    '<title>World atlas</title>',
    '<desc>Natural Earth land outlines. Visitor dots represent countries and regions, not precise locations.</desc>',
    '<g fill="none" stroke="#e6eae6" stroke-width="0.65">',
]
for lon in range(-150, 180, 30):
    x, _ = project(lon, 0)
    parts.append(f'<path d="M{x} 8V288"/>')
for lat in range(-60, 90, 30):
    _, y = project(0, lat)
    parts.append(f'<path d="M8 {y}H712"/>')
parts.append('</g><g fill="#d9dfd9" stroke="#fafbf9" stroke-width="0.4">')
for feature in land["features"]:
    geometry = feature["geometry"]
    polygons = geometry["coordinates"] if geometry["type"] == "MultiPolygon" else [geometry["coordinates"]]
    for polygon in polygons:
        if all(point[1] < -65 for ring in polygon for point in ring):
            continue
        d = " ".join("M" + "L".join(f"{x},{y}" for x, y in map(lambda p: project(*p), ring)) + "Z" for ring in polygon)
        parts.append(f'<path d="{d}" fill-rule="evenodd"/>')
parts.append('</g></svg>')
(assets / "visitor-world.svg").write_text("\n".join(parts) + "\n")
positions = {}
for feature in countries["features"]:
    p = feature["properties"]
    code = p["ISO_A2_EH"]
    if len(code) == 2:
        positions[code] = project(p["LABEL_X"], p["LABEL_Y"])
(assets / "visitor-country-positions.json").write_text(json.dumps(positions, sort_keys=True) + "\n")
print(f"Built atlas and {len(positions)} country/region positions")

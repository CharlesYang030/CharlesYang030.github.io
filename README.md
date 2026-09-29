# Qihao Yang — academic homepage

Personal homepage for Qihao Yang (杨起豪), a Ph.D. student at the School of Artificial Intelligence, Shanghai Jiao Tong University. Features the current doctoral affiliation, the two owner-selected 2026 papers **SkillOpt** and **SkillLens**, and the open-source projects **CitationClaw** and **SkillOpt**.

## Preview and deployment

No build step is needed. Open `index.html`, or run:

```sh
python3 -m http.server 18765 --bind 127.0.0.1
```

GitHub Pages serves the root of `main`. `.nojekyll` disables Jekyll processing.

## Editing

- `index.html`: biography, research directions, two paper records, Projects, contact links, news, and the footer's last-updated date. Edit the visible date and its `datetime` attribute together.
- `style.css`: responsive layout and appearance.
- `script.js`: active navigation and the accessible News dialog.
- `site-assets/`: portrait, paper figures, favicon, and locally hosted fonts.

All biography and doctoral details are sourced from the owner's September CV. The full CV and earlier education are intentionally omitted. The owner explicitly requested that all papers other than SkillOpt and SkillLens be excluded.

## Visual reference

At the owner's request, the layout closely follows [Zisu Huang's homepage](https://huangzisu.github.io/): 960px content area, Pacifico name, Newsreader body, Fraunces headings, Archivo annotations, a circular portrait, blue links, thin dividers, and two-column paper cards. The earlier terracotta palette, oversized introduction, section-number sidebar, ticker, and abstract paper banner have been replaced.

The implementation uses the owner's information and photo. Personal illustrations and the tennis interaction from the reference site are not included. News includes the owner's three NeurIPS 2026 acceptances (two Spotlights), doctoral enrollment, and the two public paper releases. The biography uses “co-advised by Prof.” for the doctoral advisors.

## Sources and assets

- SkillOpt: https://arxiv.org/abs/2605.23904
- SkillOpt figure: https://microsoft.github.io/SkillOpt/skillopt-assets/teaser-1.png
- SkillLens: https://arxiv.org/abs/2605.23899
- SkillLens figure: https://microsoft.github.io/SkillLens/static/images/overview.png
- CitationClaw description and project links: https://github.com/VisionXLab/CitationClaw
- CitationClaw official logo: https://visionxlab.github.io/CitationClaw/assets/logo.png (stored locally without modification).
- Portrait: the owner's existing homepage photo.
- Fonts: Pacifico, Fraunces, Newsreader, Archivo, and Space Mono from Google Fonts. Each font's SIL Open Font License is included in `site-assets/fonts/`.
- Chinese name: Yuji Boku from [Google Fonts](https://github.com/google/fonts/tree/main/ofl/yujiboku), hosted locally as a three-character subset for “楊起豪”, with its SIL Open Font License. All three traditional characters use the same brush font. `.chinese-name` controls its appearance and size; changing the name requires updating the font subset and its Unicode range in `site-assets/fonts.css`.

The heading places contact links after the Chinese name. Narrow screens move the English name to its own row while keeping the Chinese name and contact links together. The portrait's lower-right button switches between the original mountain photo and the owner-provided Universal globe photo (`site-assets/qihao-yang-universal.jpg`). The original photo remains the default; the switch supports mouse, touch, and keyboard and is hidden without JavaScript. The supplied photo is stored unchanged; `.portrait-photo--universal` controls its circular framing in CSS.

SkillOpt was accepted to NeurIPS 2026 as a Spotlight; SkillLens was also accepted to NeurIPS 2026. These statuses were updated on September 28, 2026, at the owner's request and checked against [Zisu Huang's homepage](https://huangzisu.github.io/). The `.acceptance-card` styles use compact, 28px outlined labels: an ochre medal icon and italic Spotlight text for SkillOpt, and a slate-blue book icon for SkillLens. Research topics sit alongside each label in the same row; on narrow screens the topic text may wrap within its column. The publication grid switches to one column at 700px to preserve readability. The News total of three accepted papers, including two Spotlights, was supplied by the owner; Selected Work continues to feature only SkillOpt and SkillLens. SkillOpt's star count is a dated snapshot: 17,827 stars verified through the GitHub API on September 29, 2026, displayed as 17.8k in both Selected Work and Projects. Update both labels and tooltips together. Qihao Yang's equal-contribution status comes from the owner-provided CV.

Projects lists CitationClaw followed by SkillOpt, separated by a thin rule. SkillOpt uses a serif text heading with a decorative document-and-iteration line icon, not an official project logo. Its description and Website, Code, Docs, and Video demo links come from the [official repository](https://github.com/microsoft/SkillOpt). The project entry emphasizes the usable framework; the paper remains in Selected Work. The existing responsive project layout stacks the heading and description on small screens.

CitationClaw's 313 GitHub stars were verified through the GitHub API on September 20, 2026. This is a static snapshot; edit its visible count and tooltip in `index.html` when updating. Its linked logo replaces the separate text title. Research phrases use `.ink-mark` (amber) and `.keyword` (blue) for marker highlights that support line wrapping. Author names use `.me` for a hand-drawn underline; ordinary text links use straight underlines.

The site loads its fonts and figures locally. Content remains visible without JavaScript. The News dialog supports keyboard navigation, Escape dismissal, and focus return; motion respects `prefers-reduced-motion`.

## Visitor atlas

The Visitors section between Projects and Contact combines a locally hosted Natural Earth map, country/region dots, and a real pageview counter. Country names are not listed beneath the map. Counting began on September 28, 2026; earlier traffic cannot be reconstructed. The initial data includes setup/verification visits. No visitor IP addresses or individual visit records are stored in this repository.

- Flag Counter ID: `5FQV`, server `s01`. [Public statistics](https://info.flagcounter.com/5FQV), [country counts](https://s01.flagcounter.com/countries/5FQV/). Preserve this ID to retain the history.
- The counter image loads once per page load on `charlesyang030.github.io`, even when the visitor has not scrolled to the footer. Local previews do not increment it. Flag Counter's free image display can lag by about five minutes. Country visitor counts use the provider's daily deduplication and are distinct from pageviews.
- `.github/workflows/visitor-map.yml` runs hourly (or manually) and uses `scripts/sync_visitors.py` to export only aggregate country counts to `visitors.json` on the separate `visitor-data` branch. It commits only when counts change, without rebuilding the homepage. GitHub may delay scheduled runs.
- The browser reads that public JSON, falls back to `site-assets/visitors.json` when unavailable, and labels the fallback as a saved map. Provider errors preserve the previous dataset. Dots represent Natural Earth country label positions, not precise visitor locations. Dot details remain available through native hover tooltips and accessible labels.
- With JavaScript disabled, the base map and counter remain available; the linked statistics page provides geographic details. If the counter is blocked, its link remains visible.
- [Flag Counter FAQ](https://flagcounter.com/faq.html) describes counting and retention, including removal of free counters after 30 days without a visitor. [Provider privacy information](https://flagcounter.com/privacy.html).

`site-assets/visitor-world.svg` and `visitor-country-positions.json` were generated from Natural Earth's `ne_110m_land.geojson` and `ne_50m_admin_0_countries.geojson` using `python3 scripts/build_visitor_map.py LAND_FILE COUNTRIES_FILE`. These [public-domain map datasets](https://www.naturalearthdata.com/about/terms-of-use/) come from [natural-earth-vector](https://github.com/nvkelso/natural-earth-vector/tree/master/geojson); no runtime map library is required. The generator uses an equirectangular projection cropped below 65°S, with land silhouettes and no political borders.

## Affiliation strip

The strip beneath the biography shows Shanghai Jiao Tong University (Ph.D.), Tsinghua University (Internship), LTTC at EdUHK (Visiting), Microsoft (Internship), and Huawei (Internship), in that order, as requested by the owner. Edit the original five items in `.affiliation-set` in `index.html`; JavaScript creates the visual duplicate used for seamless scrolling. The duplicate is hidden from assistive technology. The compact strip uses larger logos, pauses on hover, and displays a manually scrollable static set when reduced motion is requested or JavaScript is unavailable. On small screens, the icons keep their size and slide into view rather than shrinking to fit five at once.

Logo sources:

- SJTU: https://cuzyoung.github.io/ZiyangGong.github.io/assets/logos/sjtu.png
- Microsoft: https://cuzyoung.github.io/ZiyangGong.github.io/assets/logos/microsoft.svg
- Huawei: https://www.huawei.com/-/media/hcomponent-header/1.0.1.20260908162100/component/img/huawei_logo.png

- Tsinghua: https://cuzyoung.github.io/ZiyangGong.github.io/assets/logos/thu.png
- LTTC EdUHK: https://lttc.eduhk.hk/wp-content/uploads/2024/09/LTTC-Logo.svg

# Qihao Yang — academic homepage

Personal homepage for Qihao Yang (杨起豪), a Ph.D. student at the School of Artificial Intelligence, Shanghai Jiao Tong University. Features the current doctoral affiliation, the two owner-selected 2026 papers **SkillOpt** and **SkillLens**, and the open-source project **CitationClaw**.

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

The implementation uses the owner's information and photo. Personal illustrations and the tennis interaction from the reference site are not included. News contains only the owner's doctoral enrollment and the two public paper releases.

## Sources and assets

- SkillOpt: https://arxiv.org/abs/2605.23904
- SkillOpt figure: https://microsoft.github.io/SkillOpt/skillopt-assets/teaser-1.png
- SkillLens: https://arxiv.org/abs/2605.23899
- SkillLens figure: https://microsoft.github.io/SkillLens/static/images/overview.png
- CitationClaw description and project links: https://github.com/VisionXLab/CitationClaw
- CitationClaw official logo: https://visionxlab.github.io/CitationClaw/assets/logo.png (stored locally without modification).
- Portrait: the owner's existing homepage photo.
- Fonts: Pacifico, Fraunces, Newsreader, Archivo, and Space Mono from Google Fonts. Each font's SIL Open Font License is included in `site-assets/fonts/`.

Both papers are 2026 arXiv preprints, under review per the September CV. The star count is a dated snapshot: SkillOpt had 17,273 GitHub stars on September 20, 2026. Qihao Yang's equal-contribution status comes from the owner-provided CV.

CitationClaw's 313 GitHub stars were verified through the GitHub API on September 20, 2026. This is a static snapshot; edit its visible count and tooltip in `index.html` when updating. Research phrases use `.ink-mark` (amber) and `.keyword` (blue) for marker highlights that support line wrapping. Author names use `.me` for a hand-drawn underline; text links use subtle wavy underlines.

The site loads its fonts and figures locally. Content remains visible without JavaScript. The News dialog supports keyboard navigation, Escape dismissal, and focus return; motion respects `prefers-reduced-motion`.

## Affiliation strip

The strip beneath the biography shows Shanghai Jiao Tong University (Ph.D.), Tsinghua University (Internship), LTTC at EdUHK (Visiting), Microsoft (Internship), and Huawei (Internship), in that order, as requested by the owner. Edit the original five items in `.affiliation-set` in `index.html`; JavaScript creates the visual duplicate used for seamless scrolling. The duplicate is hidden from assistive technology. The compact strip uses larger logos, pauses on hover, and displays a manually scrollable static set when reduced motion is requested or JavaScript is unavailable. On small screens, the icons keep their size and slide into view rather than shrinking to fit five at once.

Logo sources:

- SJTU: https://cuzyoung.github.io/ZiyangGong.github.io/assets/logos/sjtu.png
- Microsoft: https://cuzyoung.github.io/ZiyangGong.github.io/assets/logos/microsoft.svg
- Huawei: https://www.huawei.com/-/media/hcomponent-header/1.0.1.20260908162100/component/img/huawei_logo.png

- Tsinghua: https://cuzyoung.github.io/ZiyangGong.github.io/assets/logos/thu.png
- LTTC EdUHK: https://lttc.eduhk.hk/wp-content/uploads/2024/09/LTTC-Logo.svg

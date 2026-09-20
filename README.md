# Qihao Yang — academic homepage

An original, lightweight academic homepage for Qihao Yang (杨起豪), a Ph.D. student at Shanghai Jiao Tong University. Content is limited to the current doctoral affiliation and two 2026 preprints selected by the owner: SkillOpt and SkillLens.

## Run locally

No build step or packages are required. Open `index.html`, or run:

```sh
python3 -m http.server 18765 --bind 127.0.0.1
```

Visit http://127.0.0.1:18765. GitHub Pages serves the root of `main`; `.nojekyll` disables Jekyll processing.

## Edit

- `index.html`: biography, paper records, links, and metadata.
- `style.css`: responsive layout, colors, typography, motion, and print layout.
- `script.js`: scroll progress, progressive reveal, and animation control.
- `site-assets/`: the owner's existing portrait and an original SVG favicon.

When adding a paper, update the work count as well as the paper list. Clearly distinguish accepted/published work from preprints. The GitHub star figure is a dated snapshot, not a live count. The full CV is intentionally not published because it includes earlier education and research outside this page's scope.

## Content verification — 2026-09-20

The owner-provided September CV supplies the doctoral start date (September 2026), school, group, three advisors, research directions, and Qihao Yang's equal-contribution designations. Google Scholar was consulted, and publication facts were verified against the original arXiv pages. The owner explicitly requested that only SkillOpt and SkillLens appear on the homepage.

| Work      | Status shown | Source                           |
| --------- | ------------ | -------------------------------- |
| SkillOpt  | arXiv 2026   | https://arxiv.org/abs/2605.23904 |
| SkillLens | arXiv 2026   | https://arxiv.org/abs/2605.23899 |

SkillOpt had 17,273 GitHub stars on the verification date: https://github.com/microsoft/SkillOpt. No acceptance claim is made for submitted manuscripts. Other papers are omitted at the owner’s request. Earlier degrees, papers, honors, and the former Ph.D.-seeking text are omitted.

## Design

Warm paper, ink, muted olive, and terracotta; editorial serif typography; numbered research sections; a mountain portrait; and the English expression “Onward and upward.” The SkillOpt banner is an original conceptual illustration, not a figure or quantitative result from the paper.

References supplied by the owner: https://huangzisu.github.io/ (editorial clarity and academic writing), https://cuzyoung.github.io/ZiyangGong.github.io/ (lightweight movement). No reference-site source code, personal copy, or assets were copied.

Content remains readable with JavaScript disabled. Motion respects `prefers-reduced-motion`, and the moving strip has a pause control. All assets are served locally; there are no third-party fonts, tracking scripts, or runtime dependencies.

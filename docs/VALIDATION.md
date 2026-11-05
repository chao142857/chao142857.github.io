# Validation

- Real Jekyll 3.10.0 build succeeded using isolated dependencies; lockfile includes arm64-darwin-25 and x86_64-linux.
- Internal assets, links, anchors, and template placeholder checks passed on rendered output.
- Browser inspection at 1280px desktop, 390px mobile and 320px narrow mobile: document width equals viewport width; no horizontal overflow.
- Desktop sidebar / main-content layout and mobile single-column layout inspected visually. Avatar loads at native aspect ratio.
- Anchor navigation checked; mobile heading remains visible after navigation.
- First project video starts via user interaction: readyState 4, paused false, time advances. Other videos remain paused/unloaded; no autoplay attributes.
- Local video conversions succeeded; full playback of all three clips has not been manually reviewed end to end.
- Public project URLs/readmes were accessible. Profile HTTP 200. Target homepage repository returned public HTTP 404; private existence cannot be ruled out.
- No remote push or deployment performed; GitHub Actions execution remains to be verified after owner publishes.
- Browser screenshots in docs/qa/ are local QA artifacts, excluded from Git and website output.

## Round two — 2026-11-06

- Kept existing Jekyll / AcadHomepage layout; no additional packages.
- Removed Chinese name and city from page/config; email is a mailto link.
- About: two paragraphs. Each project: one sentence and three technology terms. GitHub URLs retained.
- Exactly one motto; original footer sentence removed.
- CSS moon/horizon and music SVG accents, warm-light and blue-gray dark palette inspected.
- Initial page has zero video elements; all three covers open inline players paused with autoplay false. Close removes the video and restores focus. First video manually played with readyState 4.
- Desktop 1280px and mobile 390px / 320px inspected, no horizontal overflow. All four images loaded.
- Theme switching and persistence after navigation checked; system dark mode also observed.
- Build, node syntax check, root and subpath asset/anchor validation passed.
- No push or public deployment. Updated screenshots: docs/qa/round2-*.jpg.

## GIF revision — 2026-11-06

- True GIF files generated with 86 / 107 / 159 frames and infinite loops.
- Default desktop project frames are unchanged at 240×150 CSS px. All three images loaded in browser.
- No HTML video elements or dropdown player handlers remain; Video links point directly to MP4s.
- Local Allura font, undecorated motto and owner-provided Music image inspected.

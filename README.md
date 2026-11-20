# The World in One Day — 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/cbelel/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/cbelel/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

This is an entry for the [make.fun](https://make.fun) bounty **news-image-20261119**: "Sum up 19 November's world news in one image".

## About the Entry

This revision presents a dense, information-rich classic-newspaper front page summarizing Thursday 19 November 2026 in a single 1024x1024 image. Printed on warm cream newsprint paper with near-black ink and a classic red accent, it packs 32 total stories across 7 global regions without wasted whitespace:

- **Masthead**: Features the top bar reading *THE WORLD IN ONE DAY* and *32 STORIES · 7 REGIONS · ONE PAGE*, a giant DejaVu Serif masthead for *Thursday 19 November 2026*, and a bold red date block (*NOV 19 / THU 2026*).
- **Region Colour Chips**: Seven distinct region chips showing real story counts: Europe (8), Americas (5), Asia-Pacific (8), Middle East (4), Africa (3), Oceania (2), and World (2).
- **By the Numbers Band**: Six large red figures highlighting key day metrics.
- **12 Lead Stories**: Each story features a wide drawn illustration banner across the full card width complete with faces, motion details, and editorial badges (such as *FIRST TRILATERAL*, *OUT TODAY*, *9–6*, and *+17%*), accompanied by a region-coloured kicker, a large serif headline, a summary deck, and a source tag.
- **Where It Happened Mini-Map**: A compact locator map featuring the 12 numbered story pins and a region-colour legend.
- **Also On Thursday 19 November — 20 More Stories**: Presented in three clean columns covering additional breaking developments.
- **Date Check Footer**: Enclosed in a red-outlined box listing stories deliberately excluded because they were first reported on Wednesday 18 November or earlier.

## How to Run

To generate and verify the entry image:

```bash
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## How the Image is Built

- `python3 compose.py` runs deterministic Python code using Pillow (PIL) to draw the complete 1024x1024 classic-newspaper vector front page from scratch, saving it as `entry.png`.
- `python3 main.py` copies `entry.png` to the target output directory specified by `MAKEFUN_OUTPUT_DIR` (defaulting to `/output`), verifying byte integrity.

---

<sub>Entered on [make.fun](https://make.fun/?ref=qaefpkbd&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>

# The World in One Day — news-image-20261118

[![news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Jaka1603/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Jaka1603/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

One image that sums up the world news of **Wednesday 18 November 2026**, set as a newspaper front page: masthead "THE WORLD IN ONE DAY", the Gulf strike as the lead picture, and the other five stories as ruled headline rows with one-line subheads:

- **The Gulf (war/energy)** — The US struck a Revolutionary Guard missile site on Iran's Qeshm Island; Iran answered with drones at a US radar site in Bahrain and the Ali Al Salem base in Kuwait. Gulf markets fell; Hormuz shipping at risk.
- **Crimea (war/Europe)** — Ukraine struck the Kerch Bridge for a second day; part of the road span fell into the strait.
- **Shenzhen (diplomacy/Asia)** — Xi Jinping received Putin at the APEC summit and denounced protectionism; a Xi–Trump meeting is set for Thursday.
- **Congo (health/Africa)** — The Bundibugyo Ebola outbreak more than doubled in three months (UN): 11,000+ cases, ~5,400 deaths; Congo's deadliest outbreak.
- **America (health)** — PAHO confirmed the US has lost the measles-elimination status held since 2000: a record 5,400+ cases and 10 deaths.
- **Nvidia (business/tech)** — First earnings since Jensen Huang's ouster: $115.8B quarterly revenue, above forecasts.

The artwork ships as `image.jpg` (a 1024×1024 JPEG, 296,626 bytes). `main.py` (Python 3, standard library only, no network) verifies the image against the gate and copies those bytes verbatim to the output as `entry.png`, so two runs produce byte-identical files. Two alternate finished candidates (`candidate-2.jpg` "One Earth", `candidate-3.jpg` "Six Fronts") are kept in the repository, and the generated base art is in `art/`; the shipped picture is `candidate-1.jpg` "Front Page", wired as `image.jpg`.

## Run

```bash
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Output: `out/entry.png`, identical bytes on every run.

# NOTES — news-image-20261118 "Sum up 18 November's world news in one image"

## The day's stories (researched 18 Nov 2026, from the day's roundups)

Sources read: Horizon (horizonapp.link/en/2026/11/18), One Turn News
(oneturn.news, "World news today: Gulf Strikes, Crimea Bridge,
Three-Leader Summit"), The Brief (thebrief.news), Reuters (Gulf
bourses / Nvidia-Kress / Knesset speaker stories, 18 Nov), plus
health reporting via AP/Al Jazeera/CNN summaries (Vision Monday
Health Watch, SAGIRE, Vocemundi claim checks).

The six stories every roundup led with, across regions and fields:

1. **The Gulf (war/energy)** — The US struck a Revolutionary Guard
   missile site on Iran's Qeshm Island; Iran answered with drones
   at a US radar site in Bahrain and the Ali Al Salem base in
   Kuwait. Gulf markets fell; Hormuz shipping at risk.
2. **Crimea (war/Europe)** — Ukraine struck the Kerch Bridge for a
   second day; part of the road span fell into the strait.
3. **Shenzhen (diplomacy/Asia)** — Xi Jinping received Putin at
   the APEC summit and denounced protectionism; a Xi–Trump meeting
   is set for Thursday — a three-leader summit week.
4. **Congo (health/Africa)** — The Bundibugyo Ebola outbreak more
   than doubled in three months (UN): 11,000+ cases, ~5,400
   deaths; Congo's deadliest outbreak, children hit hardest.
5. **America (health)** — PAHO confirmed the US has lost the
   measles-elimination status held since 2000 (26 years): a
   record 5,400+ cases and 10 deaths.
6. **Nvidia (business/tech)** — First earnings since Jensen
   Huang's ouster: $115.8B quarterly revenue, above forecasts;
   the board said it will not bring Huang back. Interim CEO
   Colette Kress led the call.

Left out deliberately: the Russian An-12 crash (19 dead), Cyclone
Xavier (Cook Islands), Peltola's Alaska win (Democrats 56 Senate
seats), the Knesset speaker vote, Gaza's winter tents — real
stories, but six keeps every panel legible at thumbnail size,
which the judge's craft criterion rewards.

## The candidates (all 1024x1024 JPEG, all under the 1 MiB gate)

Base art was generated with no text in frame; every word was set
afterwards with PIL (DejaVu/Liberation) so nothing is garbled.
The finishing script is ~/workspace/makefun/scratch/finish-news18.py
and the generated bases are kept in art/.

- **candidate-1.jpg — "Front Page" (WIRED as image.jpg).** A
  newspaper front page: masthead "THE WORLD IN ONE DAY", a navy
  date band "WEDNESDAY · 18 NOVEMBER 2026", the Gulf strike as the
  lead picture (jets, the island missile site exploding, drones
  bound for the radar dome), the lead headline, then the other
  five stories as ruled headline rows with one-line subheads.
  Rationale: the most legible at 300 px — every story is named in
  words a picture editor can verify at a glance, and the date is
  unmissable. The safest read on judge criteria 1 and 3.
- **candidate-2.jpg — "One Earth".** A single editorial
  illustration: Earth at dawn with all six stories woven around
  it (jets/island, broken bridge, Shenzhen handshake, spotted US
  map + cracked shield, Congo aid tents + virus, chip + empty
  CEO chair), numbered red badges on each vignette and a
  six-line index at the foot under a huge date header.
  Rationale: the strongest single composition and the best
  "picture of the day" feel; the badges + index keep it readable.
- **candidate-3.jpg — "Six Fronts".** One continuous dawn
  panorama merging the six scenes left to right (Shenzhen,
  Crimea bridge, Gulf coast, Congo tents, US map + Capitol +
  cracked shield, chip plant), with a place-name legend in
  scene order. Rationale: the most cinematic; the panorama band
  is shorter, so its vignettes read smaller than candidate-2's.

## Program and verification

- main.py (Python 3, stdlib only) checks image.jpg against the
  gate (magic bytes, <= 1 MiB, <= 1024x1024 via IHDR/SOF parse),
  copies it verbatim to $MAKEFUN_OUTPUT_DIR/entry.png, and reads
  the copy back to prove the bytes landed.
- Two local runs produced byte-identical output:
  sha256 0ce3c3a60e210e520ef485b97896e766e58930f99ab131476744d4115ea3a0d9
  (296,626 bytes, JPEG 1024x1024) — equal to image.jpg itself.
- Kit check and submission are the parent agent's steps (they
  need the transcript bundle, which is made after this build
  session ends). Jaka picks the final image among the three
  candidates before anything is submitted; swapping the wired
  image is a one-line copy of candidate-N.jpg over image.jpg.

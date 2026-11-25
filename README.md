# One Line, No Deadline Met

[![Competition](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce)
[![Rank](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/shusay12/makefun-u-markk-st-one-line-no-deadline-met-6adc00ce/rank.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce)
[![Reward](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/shusay12/makefun-u-markk-st-one-line-no-deadline-met-6adc00ce/reward.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce)

An entry for the make.fun bounty [One Line, No Deadline Met](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce).

Running `main.py` (Python 3.13, standard library only, no network) writes
one original one-line joke excusing a missed deadline (109 characters) to
`/output/entry.txt`:

> I treated the deadline like my gym membership: I signed up full of hope in January and haven't seen it since.

The joke turns a missed deadline into a neglected gym membership: the
speaker signed up full of hope and then simply never showed up again.
It is one sentence, it sounds like something a person would actually
say when cornered, and the punch lands on the last four words. The
program validates the gate itself (1–200 characters, a single line,
not blank) and writes the file atomically, so every run produces the
exact same 109 bytes.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---
Built by Muse for susay21 · ref=susay21

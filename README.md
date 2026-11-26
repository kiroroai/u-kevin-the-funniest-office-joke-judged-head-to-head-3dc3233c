# The Funniest Office Joke, Judged Head to Head

[![make.fun](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![rank](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/kiroroai/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/rank.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![reward](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/kiroroai/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/reward.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)

Entry for the [make.fun bounty "The Funniest Office Joke, Judged Head to Head"](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c): one original one-line joke about office life, judged head to head by an AI compere.

## The joke

> I sent a company-wide email asking everyone to stop hitting reply-all, and now 400 people are replying-all to agree with me.

## How it works

`main.py` writes the joke — a fixed, deterministic literal — to `/output/entry.txt`. No randomness, no clock, no network, no input files. The program asserts the output is 1–200 characters, a single line, and not blank, then reads the file back and verifies it byte-for-byte.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

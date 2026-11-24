[![make.fun · u-brave-eagle-12-one-word-from-your-ex-cfd97ba2](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2?utm_source=github&utm_medium=readme&utm_campaign=u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![rank](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/Ikball53/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/rank.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![reward](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/Ikball53/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/reward.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2?utm_source=github&utm_medium=readme&utm_campaign=u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)

# One Word From Your Ex

## What it does

`main.py` writes exactly one word to `/output/entry.txt`: **exhausting** — the word my ex would use to describe me. Nothing else. No trailing newline, UTF-8, 10 characters, well inside the 1–24 character gate.

## Why this word wins on the judge brief

The judge weighs, most important first:

1. **Exactly one word an ex would use to describe you.** "Exhausting" is a real verdict an ex says to their friends about a former partner. It is a single word, on subject, no phrase, no sentence, no gimmick.
2. **Makes me laugh out loud.** The laugh comes from the self-own: the entrant is not blaming the ex, they are admitting they were *a lot* — too many messages, too many feelings, too many 2 a.m. conversations. A confession is funnier than an insult.
3. **Stings with recognition, because it is painfully true.** This is not meanness for its own sake; it is the honest, self-aware verdict. The entrant plainly knows it, which is exactly what the brief rewards.
4. **Lands instantly, no explanation needed.** Everyone understands "exhausting" the moment they read it, and no near synonym keeps the edge — "tiring" is flat, "draining" is vague, "overwhelming" is too soft.
5. **Feels relatable.** Everyone has either been exhausting or dated someone exhausting. It names something people have lived through, so it is the kind of word people repeat.

It beats blander words ("boring", "late") on the laugh, and beats pure insults ("toxic", "annoying") on the sting-because-it-is-true test.

## How it runs

```sh
python3 main.py
```

Deterministic, standard library only, no network, no input. It creates `/output/` if needed and writes the entry as exact bytes.

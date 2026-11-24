#!/usr/bin/env python3
"""One Word From Your Ex -- make.fun entry.

Writes exactly one word to /output/entry.txt: the word my ex would use
to describe me. No trailing newline, UTF-8, deterministic, stdlib only.

Why this word
-------------
"exhausting" is the word an ex actually says, out loud, to their friends:
not a generic insult ("annoying", "toxic") and not a clinical label
("avoidant"), but the honest verdict on a partner who was too much --
too many messages, too many feelings, too many 2 a.m. conversations.
It is funny because it is self-aware: the entrant plainly knows it.
It stings because it is true, and it is relatable because everyone has
either been exhausting or dated someone exhausting. One word, no
explanation needed, and no near synonym ("tiring", "draining") lands
with the same edge.
"""

import os

ENTRY = "exhausting"

OUTPUT_PATH = "/output/entry.txt"

# Gate: 1 to 24 characters, not only white space, exactly one word.
assert 1 <= len(ENTRY) <= 24, "entry outside gate length"
assert ENTRY == ENTRY.strip(), "entry must not start or end with space"
assert " " not in ENTRY, "entry must be exactly one word"


def main() -> int:
    text = ENTRY.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


def main() -> int:
    text = ENTRY.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

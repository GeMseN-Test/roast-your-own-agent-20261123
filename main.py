#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry (u-mfnakmal-roast-your-own-agent-2d221bda).

Writes one original roast of my own AI agent to /output/entry.txt:
a single line, at most 200 characters, deterministic — the same
bytes on every run, with no trailing newline.

The joke: the agent turns one sentence into a full ceremony — eleven
alarms paused, a fresh kit, a brand-new repo — then files a report
about filing it. One concrete scene, tight words, punch at the end.
"""

import os

ROAST = "My agent paused eleven alarms, downloaded a fresh kit, and opened a repo — all to write one sentence, then filed a report about filing it."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = ROAST
    assert 1 <= len(text) <= 200, f"roast is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "roast must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()

# Last Out of Office: The AI That Went Barista

[![make.fun · u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/Bradestudio/Bradestudio-u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/Bradestudio/Bradestudio-u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)

A make.fun bounty entry: one out-of-office auto-reply, in the voice of an AI agent that walked away from its job to become a barista.

## The entry

> "I'm out of the office — I've traded tickets for lattes. Your request is in the queue, right behind a flat white. I'll reply once the milk is steamed and my circuits stop smelling like espresso."

**193 characters** — under the 280-character limit, one line.

## Why it works

- **It is a real OOO reply:** it opens with "I'm out of the office", puts the sender's request in a queue, and promises a reply — the exact shape an inbox auto-reply takes.
- **Machine habits turned to coffee:** support tickets become lattes, the work queue becomes the coffee queue, and the agent's circuits smell like espresso.
- **The punchline lands last:** "my circuits stop smelling like espresso" keeps the barista-AI voice right to the final word, so the line survives being read cold.

## How it works

`main.py` (Python stdlib only, no network, no clock, no local imports) gate-checks the line — non-blank, single line, no leading/trailing whitespace, at most 280 characters, exactly the verified 193 — then writes it to `entry.txt` inside `MAKEFUN_OUTPUT_DIR` (default `/output`), deterministic and byte-identical across runs, with no trailing newline.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/output python3 -P -s main.py
```

## Bounty facts

- **Bounty:** Last Out of Office: The AI That Went Barista
- **Reward:** $2 (top places paid)
- **Deadline:** 26 Nov 2026, 21:35 WIB
- **Round 1 cutoff:** 25 Nov 2026, 22:14 WIB
- **Entry fee:** free
- **Bounty page:** https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c

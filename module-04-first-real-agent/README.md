# Module 4 · Building Your First Real Agent

**The breakthrough module.** By the end, your agent will think, act, and answer on its own.

## A chatbot answers once. An agent runs until the job is done.

Three things make something an agent:

1. **A goal, not a question** — "what are 754 shares worth?" not "what is 345 × 754?"
2. **A tool** — the agent can act in the world: calculate, search, read, call.
3. **The loop** — after a tool runs, it reads the result and decides: am I done, or do I act again?

## Install

```bash
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install openai duckduckgo-search
```

## Lab

Type [`first_agent.py`](first_agent.py) yourself — **do not paste.** Build it in order:
calculator first, run it, then add the web-search tool.

```bash
python first_agent.py
```

Calculator-only expected output:

```
TOOL: calculate | RESULT: 260130
754 shares of Apple stock at $345 each would be worth $260,130.
```

With both tools, the agent searches the web **first**, then calculates — in the right
order, without you telling it to.

> The agent loop is `while True`. It runs until the AI makes no more tool calls.
> The AI reads the full messages list — including every tool result — on every iteration.

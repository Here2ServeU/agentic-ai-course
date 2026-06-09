# Module 4 · Building Your First Real Agent

**The breakthrough module.** By the end, your agent will think, act, and answer on its own.

## A chatbot answers once; an agent runs until the job is done

Three things make something an agent:

1. **A goal, not a question** — "what are 754 shares worth?" not "what is 345 × 754?"
2. **A tool** — the agent can act in the world: calculate, search, read, call.
3. **The loop** — after a tool runs, it reads the result and decides: am I done, or do I act again?

## Install

```bash
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install openai duckduckgo-search
export OPENAI_API_KEY='sk-...'
```

## Lab — build it in two stages, type every line

- **Lab 4.1** — build [`first_agent.py`](first_agent.py): the calculator agent (Video 2).

  ```bash
  python first_agent.py
  ```

  Expected output:

  ```text
  TOOL: calculate | RESULT: 260130
  754 shares of Apple stock at $345 each would be worth $260,130.
  ```

- **Lab 4.2** — add the web search tool. The finished two-tool version is
  [`first_agent_with_search.py`](first_agent_with_search.py). With both tools the agent
  searches the web **first**, then calculates — in the right order, without you telling it to.

  ```bash
  python first_agent_with_search.py
  ```

> Type each version yourself; use these files only to compare after yours runs.
>
> The agent loop is `while True`. It runs until the AI makes no more tool calls.
> The AI reads the full messages list — including every tool result — on every iteration.

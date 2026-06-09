# Module 9 · Observability: Knowing What Your Agent Is Doing

*Add tracing, logging, and cost tracking so you always know what your agent is doing
— and what it is costing.*

## Why this is not optional

You deploy your agent. It looks fine. Then your OpenAI bill is $1,000 and you have no
idea why. Or it gives a wrong answer and you have no logs, no trace, no way to know
which step failed.

Observability means you can see, step by step: which tools it called, what it decided,
how much it cost, how long it took, where it failed.

Three things separate a hobby project from a professional system:

1. **File logging** — every step recorded to a `.log`/`.txt` file.
2. **Cost tracking** — count tokens, estimate dollars.
3. **LangSmith tracing** — a free visual dashboard of every run.

## Install

```bash
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install openai duckduckgo-search
export OPENAI_API_KEY='sk-...'
```

For tracing, create a free account at [smith.langchain.com](https://smith.langchain.com),
then set in your environment (never hard-code the key):

```bash
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY='your-langsmith-key'
export LANGCHAIN_PROJECT='my-first-agent'
```

## Lab

1. Build [`observable_agent.py`](observable_agent.py) yourself.
2. Run it, then **open the `agent_log_YYYY-MM-DD.txt` file and read every line.**
3. Run 3 different goals and compare their costs.
4. Find your trace in the LangSmith dashboard.

```bash
python observable_agent.py
```

> Log files are git-ignored — they are runtime output, not source.

# Module 7 · Multi-Agent Teams with CrewAI

*Build 3 agents — a researcher, an analyst, and a writer — that collaborate.
Search is powered by DuckDuckGo — free, no API key needed.*

## Why a team beats a single agent

A consulting firm does not have one person do everything. A research team gathers
data, an analysis team interprets it, a writing team polishes it. Multi-agent systems
work the same way.

CrewAI's four pieces:

- **Crew** = your team.
- **Agent** = a team member with a role, a goal, and a backstory.
- **Task** = a specific piece of work.
- **Process** = the order the work happens in (here, `sequential`).

## Python 3.11 is required

CrewAI depends on `tiktoken`, which uses Rust bindings (PyO3) that do **not** support
Python 3.12, 3.13, or 3.14. Build a fresh `venv` with Python 3.11 before installing:

```bash
python3.11 -m venv venv
source venv/bin/activate           # Windows: venv\Scripts\activate
python --version                   # MUST show 3.11.x — the safety check
```

## Install

```bash
pip install crewai crewai-tools duckduckgo-search
export OPENAI_API_KEY='sk-...'     # Windows CMD: set OPENAI_API_KEY=sk-...
```

> **No Serper key needed.** This module uses DuckDuckGo — free, no account, no API key.
> The tradeoff is freshness and structure: for learning and prototyping it is more than
> enough. For production, swap in Tavily or Serper — it is a four-line change and the
> rest of the file stays identical.

## Lab

1. Build [`research_crew.py`](research_crew.py) — it wraps DuckDuckGo as a `@tool` and runs it on *"AI agents in healthcare."*
2. Study [`fraud_crew.py`](fraud_crew.py): same search tool, same structure, different **roles, goals, backstories** — that is all it takes to make a domain specialist team.
3. Design your **own** 3-agent crew for your use case. Give each agent a 3–4 sentence backstory.

```bash
python research_crew.py
python fraud_crew.py
```

Watch each agent activate in sequence in the terminal output.

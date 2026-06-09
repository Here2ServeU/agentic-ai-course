# Module 7 · Multi-Agent Teams with CrewAI

*Build 3 agents — a researcher, an analyst, and a writer — that collaborate.*

## Why a team beats a single agent

A consulting firm does not have one person do everything. A research team gathers
data, an analysis team interprets it, a writing team polishes it. Multi-agent systems
work the same way.

CrewAI's four pieces:

- **Crew** = your team.
- **Agent** = a team member with a role, a goal, and a backstory.
- **Task** = a specific piece of work.
- **Process** = the order the work happens in (here, `sequential`).

## Install

```bash
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install crewai crewai-tools
```

Get a free Serper key at [serper.dev](https://serper.dev) (2 minutes), then:

```bash
export SERPER_API_KEY='your-serper-key'    # Windows CMD: set SERPER_API_KEY=...
export OPENAI_API_KEY='sk-...'
```

## Lab

1. Build [`research_crew.py`](research_crew.py) and run it on *"AI agents in [your industry]."*
2. Study [`fraud_crew.py`](fraud_crew.py): same structure, different **roles, goals, backstories** — that is all it takes to make a domain specialist team.
3. Design your **own** 3-agent crew for your use case. Give each agent a 3–4 sentence backstory.

```bash
python research_crew.py
python fraud_crew.py
```

Watch each agent activate in sequence in the terminal output.

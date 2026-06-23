# Module 9 · Observability: Knowing What Your Agent Is Doing

*Add file logging, cost tracking, and LangSmith tracing so you always know what your
agent is doing — and what it is costing.*

## Why this is not optional

You deploy your agent. It looks fine. Then your OpenAI bill is $1,000 and you have no
idea why. Or it gives a wrong answer and you have no logs, no trace, no way to know
which step failed.

Observability means you can see, step by step: which tools it called, what it decided,
how much it cost, how long it took, where it failed.

Three things separate a hobby project from a professional system:

1. **File logging** — every step recorded to an `agent_log_YYYY-MM-DD.txt` file.
2. **Cost tracking** — count tokens, estimate dollars.
3. **LangSmith tracing** — a free visual dashboard of every run.

## Install

```bash
source venv/bin/activate           # Windows: venv\Scripts\activate
pip install ddgs openai agents "langsmith[openai-agents]"
export OPENAI_API_KEY='sk-...'
```

> `ddgs` is the renamed `duckduckgo-search` package. `agents` is the OpenAI Agents SDK,
> used here only by the tracing test and processor.

For tracing, create a free account at [smith.langchain.com](https://smith.langchain.com),
generate a key, then set these in your environment (never hard-code the key).
**Use the `LANGSMITH_` prefix — the old `LANGCHAIN_*` names no longer work** and are the
number-one cause of "Waiting for traces":

```bash
export LANGSMITH_TRACING=true
export LANGSMITH_ENDPOINT=https://api.smith.langchain.com
export LANGSMITH_API_KEY='lsv2_pt_your-new-key-here'
export LANGSMITH_PROJECT="default"
```

## Lab

1. **Run the test first.** Build [`langsmith_test.py`](langsmith_test.py) and run it — confirm a trace appears in the dashboard *before* touching your agent.
2. Copy your Module 4 agent to [`first_agent_with_search.py`](first_agent_with_search.py) and add the three groups: new imports, logging setup, and the logging/cost lines inside `run_agent`.
3. Run it, then **open the `agent_log_YYYY-MM-DD.txt` file and read every line.**
4. Run 3 different goals and compare their costs. Find all three in LangSmith.

```bash
python langsmith_test.py            # prove the connection
python first_agent_with_search.py   # your observable agent
```

> **The five rules:** use `LANGSMITH_` not `LANGCHAIN_`; import from
> `langsmith.wrappers`; call `set_trace_processors([...])` *before* the agent runs; run
> the test script first; never put keys in code. Log files are git-ignored — runtime
> output, not source.

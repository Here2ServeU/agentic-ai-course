# Agentic AI Systems Engineer

**A 10-module, hands-on course that takes you from two lines of Python to a deployed, observable AI agent.**

By **Rev. Dr. Emmanuel Naweji** · [www.emmanuelnaweji.com](https://www.emmanuelnaweji.com) · Transformed 2 Succeed (T2S)

---

## How to use this repository

> **Type every line yourself. Use this repo only to compare.**

This repository is the **answer key**, not a copy-paste source. The single most
important habit in this course is typing the code with your own hands. Your hands
learn what your eyes skim over.

The workflow for every module:

1. Watch the module video.
2. Open the module's lab guide (the PDF) and **type the script into your own file**.
3. Run it. Fix your own typos. Read the errors.
4. **Only then** open the matching file in this repo and compare it against yours.

If your version works and reads differently from the reference — good. There is
more than one way to write correct code. If your version breaks, the reference
file shows you what a working version looks like.

```
"A chatbot answers. An agent acts."
You are here to build the second kind.
```

---

## What you build, module by module

| Module | Folder | You build |
|-------|--------|-----------|
| 1 · What Is an AI Agent? | [`module-01-what-is-an-ai-agent`](module-01-what-is-an-ai-agent/) | `hello.py` — your first two lines |
| 2 · Python Basics | [`module-02-python-basics`](module-02-python-basics/) | `basics.py` — variables, functions, lists, dicts |
| 3 · Your First API Call | [`module-03-first-api-call`](module-03-first-api-call/) | `first_api_call.py` + 10 system prompts |
| 4 · Your First Real Agent | [`module-04-first-real-agent`](module-04-first-real-agent/) | `first_agent.py` — the agent loop, 2 tools |
| 5 · Memory & Multi-Step | [`module-05-memory-multistep`](module-05-memory-multistep/) | `memory_demo.py`, `memory_agent.py` |
| 6 · RAG | [`module-06-rag`](module-06-rag/) | `rag_agent.py` — talk to your documents |
| 7 · Multi-Agent (CrewAI) | [`module-07-multiagent-crewai`](module-07-multiagent-crewai/) | `research_crew.py`, `fraud_crew.py` |
| 8 · Cloud Deployment | [`module-08-cloud-deployment`](module-08-cloud-deployment/) | `agent_api.py`, `Dockerfile` |
| 9 · Observability | [`module-09-observability`](module-09-observability/) | logging, cost tracking, LangSmith |
| 10 · Capstone | [`module-10-capstone`](module-10-capstone/) | the full deployed Fraud Investigation Agent |

---

## The one habit you repeat every module

Every module begins and ends the same way. Build this into muscle memory.

```bash
# CREATE (once per module folder)
python3 -m venv venv          # Mac/Linux
python  -m venv venv          # Windows

# ACTIVATE (every time you open a new terminal)
source venv/bin/activate          # Mac/Linux
venv\Scripts\activate             # Windows Command Prompt
.\venv\Scripts\Activate.ps1       # Windows PowerShell

# You will see (venv) in your prompt. That means it is working.

# DEACTIVATE (when you are done for the day)
deactivate
```

> **Windows PowerShell only** — if you get an error about running scripts:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

---

## Before you start (Module 1 setup)

1. Install **Python 3.11+** from [python.org/downloads](https://www.python.org/downloads) — on Windows, check **"Add Python to PATH."**
2. Install **VS Code** from [code.visualstudio.com](https://code.visualstudio.com).
3. Create an **OpenAI API key** at [platform.openai.com](https://platform.openai.com). Save it somewhere safe.

Set your key as an environment variable **every new terminal session** — never put it in your code:

```bash
# Mac or Linux
export OPENAI_API_KEY='sk-your-actual-key-here'

# Windows Command Prompt
set OPENAI_API_KEY=sk-your-actual-key-here
```

---

## Security rules (non-negotiable)

- **Never** commit your API key. Use environment variables. It belongs in `.env`, which is git-ignored.
- **Never** push the `venv/` folder. Anyone cloning makes their own.
- On Render (or any host), set your key in the dashboard — **not in the code**.

---

## About the instructor

**Rev. Dr. Emmanuel Naweji** is the CEO and Founder of **Transformed 2 Succeed (T2S)**.
A pastor, builder, and mentor, he is a cloud architect and AI engineer who built this
course for someone exactly like you — the person who shows up, does the work, and
builds something real.

> "The people who change industries are not always the ones with the most
> credentials. They are the ones who showed up, did the work, and built something real."

· [www.emmanuelnaweji.com](https://www.emmanuelnaweji.com) · Transformed 2 Succeed (T2S)

---

## License

Course materials © Emmanuel Naweji / Transformed 2 Succeed (T2S). Provided for
enrolled students' personal learning use. See [LICENSE](LICENSE).

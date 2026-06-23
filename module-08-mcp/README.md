# Module 8 · Giving Agents Superpowers with MCP

*MCP — the Model Context Protocol — is the universal plug that lets any agent connect
to any tool without writing custom glue code for each one. You build your own MCP
server and connect an agent to it.*

## MCP is USB-C for AI agents

Before USB-C, every device had its own cable. Then one shape replaced them all — the
same port charges your phone, drives your monitor, reads your camera.

In Module 4 you hand-wired every tool: you wrote the function, the schema, and the
dispatch yourself. That works for two tools. A real agent needs ten — a database, a
calendar, a file store, a payment system. Hand-wiring ten tools means ten brittle glue
scripts. **MCP is the agreed-upon shape.** Any tool that speaks MCP plugs into any agent
that speaks MCP. Build the tool once; every agent can use it.

Two sides, one relationship:

- **Server** = the tool. It offers what it can do (`list_tools`) and does the work (`call_tool`).
- **Client** = the agent (or the program that speaks for it). It asks what's available, then asks the server to run one.

## Python 3.11 is required

The MCP Python SDK shares CrewAI's dependency chain (`tiktoken` → PyO3), which does not
support Python 3.12+. Reuse the Module 7 `venv`, or build a fresh 3.11 one:

```bash
python3.11 -m venv venv
source venv/bin/activate           # Windows: venv\Scripts\activate
python --version                   # MUST show 3.11.x — the safety check
```

## Install

```bash
pip install "mcp[cli]" openai
export OPENAI_API_KEY='sk-...'      # Windows CMD: set OPENAI_API_KEY=sk-...
```

## Lab

1. Build [`weather_server.py`](weather_server.py) — a server with one tool, `get_forecast`. Run it; it waits quietly for a client.
2. Build [`mcp_agent.py`](mcp_agent.py) — the client. It launches the server for you, discovers its tools automatically (no hand-written schema), and lets GPT-4o call them.

```bash
python3 mcp_agent.py     # Windows: python mcp_agent.py
```

3. **The key lab:** add a second `@mcp.tool()` (e.g. `packing_advice`) to the server, change *only* the goal in the agent, and watch the agent pick up the new tool with **zero changes to the agent code**. That is *build once, use everywhere.*

> **The rule:** no server, no tool. The server must be reachable for the agent to use it
> — here the client launches it for you, so you run one command.

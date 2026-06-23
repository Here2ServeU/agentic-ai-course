# research_crew.py
# Install:  pip install crewai crewai-tools duckduckgo-search
# Python:   3.11 required
# Key:      export OPENAI_API_KEY='sk-...'  (macOS/Linux)
#           set OPENAI_API_KEY=sk-...        (Windows CMD)
# Run:      python3 research_crew.py

from crewai import Agent, Task, Crew, Process
from crewai.tools import tool
from duckduckgo_search import DDGS


# ── SEARCH TOOL — DuckDuckGo (free, no API key needed) ───────────
@tool('Search the web')
def search_web(query: str) -> str:
    """Search the web using DuckDuckGo and return results."""
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=5))
    return '\n'.join([
        f"Title: {r['title']}\nURL: {r['href']}\nSummary: {r['body']}"
        for r in results
    ])


# ── AGENT 1: Researcher ───────────────────────────────────────────
researcher = Agent(
    role="Healthcare AI Researcher",
    goal="Find the latest real-world deployments of AI agents in healthcare",
    backstory=(
        "You are a senior research specialist with 15 years of experience "
        "in healthcare technology. You find accurate, current information "
        "and summarize it with precision. You never speculate. "
        "You report only what you can verify."
    ),
    tools=[search_web],
    verbose=True
)

# ── AGENT 2: Analyst ──────────────────────────────────────────────
analyst = Agent(
    role="Healthcare Data Analyst",
    goal="Identify the 3 most important trends from the research findings",
    backstory=(
        "You are a senior analyst who turns raw research into structured insight. "
        "You look for patterns, rank findings by impact, and explain "
        "why each trend matters. You write for decision-makers who need clarity."
    ),
    verbose=True
)

# ── AGENT 3: Writer ───────────────────────────────────────────────
writer = Agent(
    role="Technical Writer",
    goal="Write a clear 3-paragraph summary for a non-technical audience",
    backstory=(
        "You specialize in making complex AI topics accessible to everyone. "
        "You write in plain English and ensure every sentence serves the reader. "
        "Your writing is accurate, concise, and engaging."
    ),
    verbose=True
)

# ── TASK 1: Research ──────────────────────────────────────────────
research_task = Task(
    description=(
        "Search for the latest real-world deployments of AI agents in {topic}. "
        "Focus on specific applications and measurable outcomes. "
        "Return a detailed list of at least 5 findings with sources."
    ),
    expected_output="A detailed list of at least 5 findings with sources.",
    agent=researcher
)

# ── TASK 2: Analysis ──────────────────────────────────────────────
analysis_task = Task(
    description=(
        "Review the research findings about {topic}. "
        "Identify the 3 most important trends. "
        "For each trend, write a heading and a clear explanation."
    ),
    expected_output="3 clearly labeled trends with explanations.",
    agent=analyst
)

# ── TASK 3: Writing ───────────────────────────────────────────────
writing_task = Task(
    description=(
        "Write a 3-paragraph summary of the analysis findings about {topic}. "
        "Write for someone with no AI background. Use plain English."
    ),
    expected_output="A 3-paragraph plain English summary ready to share.",
    agent=writer
)

# ── CREW ──────────────────────────────────────────────────────────
crew = Crew(
    agents=[researcher, analyst, writer],
    tasks=[research_task, analysis_task, writing_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff(inputs={"topic": "AI agents in healthcare"})
print(result.raw)

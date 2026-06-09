# Module 7 · research_crew.py
# Install: pip install crewai crewai-tools
# Get a free Serper key at serper.dev, then set SERPER_API_KEY below or in your env.

from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
import os

os.environ['SERPER_API_KEY'] = 'your-serper-key'  # free at serper.dev
search_tool = SerperDevTool()

# ── The three agents — researcher, analyst, writer ────────────────────
researcher = Agent(
    role="Senior Research Analyst",
    goal="Find the most relevant, current facts about {topic}",
    backstory="You are a meticulous researcher who gathers primary sources and recent "
              "data. You never settle for surface-level information.",
    tools=[search_tool],
    verbose=True
)

analyst = Agent(
    role="Domain Analyst",
    goal="Interpret the research and surface the key insights about {topic}",
    backstory="You turn raw findings into meaning. You spot patterns, risks, and "
              "opportunities others miss.",
    verbose=True
)

writer = Agent(
    role="Report Writer",
    goal="Produce a clear, polished report about {topic}",
    backstory="You write executive-ready prose. Clear structure, no jargon, every "
              "claim grounded in the analysis you were given.",
    verbose=True
)

# ── The three tasks — research, analysis, writing ─────────────────────
research_task = Task(
    description="Research {topic}. Gather the most important and current facts.",
    expected_output="A bullet list of 8-12 key findings with brief context.",
    agent=researcher
)

analysis_task = Task(
    description="Analyze the research findings on {topic}. Identify the top insights.",
    expected_output="A short analysis naming the 3-5 most important insights and why.",
    agent=analyst
)

writing_task = Task(
    description="Write a polished report on {topic} using the analysis.",
    expected_output="A structured report with an intro, key sections, and a conclusion.",
    agent=writer
)

crew = Crew(
    agents=[researcher, analyst, writer],
    tasks=[research_task, analysis_task, writing_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff(inputs={"topic": "AI agents in healthcare"})
print(result.raw)

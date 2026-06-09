# Module 7 · Multi-Agent Teams with CrewAI
# A 3-person AI research team: researcher -> analyst -> writer.
# TYPE THIS YOURSELF.
#
# Install:  pip install crewai crewai-tools
# Keys:     export OPENAI_API_KEY='sk-...'
#           export SERPER_API_KEY='your-serper-key'   (free at serper.dev)

import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

# A free web-search tool for the crew. Get a key at https://serper.dev
# (Prefer not to hard-code keys — set SERPER_API_KEY in your environment instead.)
search_tool = SerperDevTool()

# ── The three team members. Each has a role, a goal, and a backstory. ──
researcher = Agent(
    role="Senior Research Analyst",
    goal="Find the most relevant, current facts about {topic}",
    backstory=(
        "You are a meticulous researcher who gathers primary sources and recent data. "
        "You never settle for surface-level information."
    ),
    tools=[search_tool],
    verbose=True,
)

analyst = Agent(
    role="Domain Analyst",
    goal="Interpret the research and surface the key insights about {topic}",
    backstory=(
        "You turn raw findings into meaning. You spot patterns, risks, and "
        "opportunities others miss."
    ),
    verbose=True,
)

writer = Agent(
    role="Report Writer",
    goal="Produce a clear, polished report about {topic}",
    backstory=(
        "You write executive-ready prose. Clear structure, no jargon, every claim "
        "grounded in the analysis you were given."
    ),
    verbose=True,
)

# ── The three tasks, flowing in logical order. ────────────────────────
research_task = Task(
    description="Research {topic}. Gather the most important and current facts.",
    expected_output="A bullet list of 8-12 key findings with brief context.",
    agent=researcher,
)

analysis_task = Task(
    description="Analyze the research findings on {topic}. Identify the top insights.",
    expected_output="A short analysis naming the 3-5 most important insights and why.",
    agent=analyst,
)

writing_task = Task(
    description="Write a polished report on {topic} using the analysis.",
    expected_output="A well-structured report with an intro, key sections, and a conclusion.",
    agent=writer,
)

crew = Crew(
    agents=[researcher, analyst, writer],
    tasks=[research_task, analysis_task, writing_task],
    process=Process.sequential,
    verbose=True,
)

if __name__ == "__main__":
    result = crew.kickoff(inputs={"topic": "AI agents in healthcare"})
    print(result.raw)

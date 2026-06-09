# Module 7 · Customizing Your Crew for Your Domain
# Same CrewAI structure as research_crew.py — but the roles, goals, and backstories
# turn it into a fraud-investigation specialist team. That is all it takes.
# TYPE THIS YOURSELF, then design your OWN domain crew.
#
# Install:  pip install crewai crewai-tools
# Keys:     export OPENAI_API_KEY='sk-...'
#           export SERPER_API_KEY='your-serper-key'

from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

investigator = Agent(
    role="Senior Fraud Investigator",
    goal="Examine the case for fraud signals: timing, amounts, payees, and patterns",
    backstory=(
        "You have investigated over 10,000 fraud cases at a major bank. You notice the "
        "details others overlook and you never jump to conclusions without evidence."
    ),
    tools=[search_tool],
    verbose=True,
)

risk_analyst = Agent(
    role="Risk Analyst",
    goal="Score the overall risk and explain the reasoning clearly",
    backstory=(
        "You translate investigative findings into a defensible LOW / MEDIUM / HIGH "
        "risk rating, always grounded in the evidence."
    ),
    verbose=True,
)

report_writer = Agent(
    role="Investigation Report Writer",
    goal="Produce a clear, professional investigation report",
    backstory=(
        "You write reports that a compliance officer can act on immediately: findings, "
        "risk level, and recommended next steps."
    ),
    verbose=True,
)

investigation_task = Task(
    description="Investigate this case for fraud signals: {case}",
    expected_output="A list of specific risk signals found, each with a short justification.",
    agent=investigator,
)

risk_task = Task(
    description="Score the overall fraud risk for the case and justify it.",
    expected_output="A risk level of LOW, MEDIUM, or HIGH with clear reasoning.",
    agent=risk_analyst,
)

report_task = Task(
    description="Write the final investigation report for: {case}",
    expected_output="A professional report: summary, signals, risk level, recommended action.",
    agent=report_writer,
)

crew = Crew(
    agents=[investigator, risk_analyst, report_writer],
    tasks=[investigation_task, risk_task, report_task],
    process=Process.sequential,
    verbose=True,
)

if __name__ == "__main__":
    result = crew.kickoff(
        inputs={
            "case": "A $9,800 wire transfer at 3:14am to a newly added overseas payee, "
            "from an account that normally sees only small domestic purchases."
        }
    )
    print(result.raw)

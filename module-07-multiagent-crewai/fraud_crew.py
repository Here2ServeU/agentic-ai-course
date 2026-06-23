# fraud_crew.py — FinTech domain
# Same search tool. Same structure. Different domain.
# Install:  pip install crewai crewai-tools duckduckgo-search
# Python:   3.11 required
# Run:      python3 fraud_crew.py

from crewai import Agent, Task, Crew, Process
from crewai.tools import tool
from duckduckgo_search import DDGS


@tool('Search the web')
def search_web(query: str) -> str:
    """Search the web using DuckDuckGo and return results."""
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=5))
    return '\n'.join([
        f"Title: {r['title']}\nURL: {r['href']}\nSummary: {r['body']}"
        for r in results
    ])


investigator = Agent(
    role="Financial Fraud Investigator",
    goal="Gather evidence of suspicious transaction patterns for {case}",
    backstory=(
        "You are a certified fraud examiner with 10 years at a major bank. "
        "You trace transaction chains, identify anomalies, and document evidence. "
        "You follow AML protocols and never speculate without data."
    ),
    tools=[search_web],
    verbose=True
)

risk_analyst = Agent(
    role="Financial Risk Analyst",
    goal="Assess risk level and regulatory exposure for {case}",
    backstory=(
        "You specialize in financial risk and regulatory compliance. "
        "You translate investigative findings into risk scores and flags. "
        "You know FINRA, AML, and SOX requirements in detail."
    ),
    verbose=True
)

report_writer = Agent(
    role="Compliance Report Writer",
    goal="Produce a formal incident report for {case} ready for legal review",
    backstory=(
        "You write regulatory documents for financial institutions. "
        "Your reports are precise, structured, and defensible in court."
    ),
    verbose=True
)

investigation_task = Task(
    description="Investigate suspicious patterns for {case}. Document findings.",
    expected_output="Evidence report with flagged transactions.",
    agent=investigator
)
risk_task = Task(
    description="Assess risk and compliance exposure for {case}.",
    expected_output="Risk assessment with regulatory flags.",
    agent=risk_analyst
)
report_task = Task(
    description="Write a formal incident report for {case} for legal review.",
    expected_output="Structured incident report for compliance review.",
    agent=report_writer
)

crew = Crew(
    agents=[investigator, risk_analyst, report_writer],
    tasks=[investigation_task, risk_task, report_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff(inputs={"case": "suspicious wire transfers — Account 7723"})
print(result.raw)

# Module 9 · langsmith_test.py — prove LangSmith tracing works before touching your agent.
# This is the "Captain Obvious" test from the official LangSmith docs.
# Install: pip install ddgs openai agents "langsmith[openai-agents]"
# Set in terminal (note the LANGSMITH_ prefix, not LANGCHAIN_):
#   export LANGSMITH_TRACING=true
#   export LANGSMITH_ENDPOINT=https://api.smith.langchain.com
#   export LANGSMITH_API_KEY='lsv2_pt_your-new-key-here'
#   export LANGSMITH_PROJECT="default"
# Run:     python langsmith_test.py  ->  a trace appears at smith.langchain.com

import asyncio
from agents import Agent, Runner, set_trace_processors
from langsmith.wrappers import OpenAIAgentsTracingProcessor


async def main():
    agent = Agent(
        name="Captain Obvious",
        instructions="You are Captain Obvious, the world's most literal technical support agent.",
    )
    question = "Why is my code failing when I try to divide by zero? I keep getting this error message."
    result = await Runner.run(agent, question)
    print(result.final_output)


if __name__ == "__main__":
    set_trace_processors([OpenAIAgentsTracingProcessor()])
    asyncio.run(main())

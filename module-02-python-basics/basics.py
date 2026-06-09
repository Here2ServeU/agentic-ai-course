# Module 2 · basics.py
# Type this yourself. Compare with this file only after yours runs.

# ── Part 1: Variables ─────────────────────────────────────────────────
your_name = "Emmanuel"
your_goal = "Build a fraud agent"
your_industry = "FinTech"
max_steps = 10
verbose = True

print(your_name)
print(your_goal)
print(your_industry)
print(max_steps)
print(verbose)


# ── Part 2: Functions ─────────────────────────────────────────────────
def introduce_agent(name, purpose):
    """Returns a sentence introducing an agent."""
    intro = name + " is an agent that " + purpose
    return intro


result = introduce_agent("FraudBot", "investigates suspicious transactions")
print(result)


def calculate(expression):
    """Evaluates math. Use for any calculations."""
    try:
        return str(eval(expression))
    except:
        return "Error: could not calculate"


print(calculate("228 * 500"))
print(calculate("100 / 4"))


# ── Part 3: Lists ─────────────────────────────────────────────────────
my_tools = ["calculate", "search_web", "send_email", "read_file"]
print(my_tools)
print(my_tools[0])
print(len(my_tools))

for tool in my_tools:
    print("Tool:", tool)


# ── Part 4: Dictionaries ──────────────────────────────────────────────
message = {
    "role": "user",
    "content": "Find the Apple stock price."
}
print(message["role"])
print(message["content"])

conversation = [
    {"role": "system", "content": "You are a helpful agent."},
    {"role": "user", "content": "Find Apple stock price."},
]
print(len(conversation))
print(conversation[0])

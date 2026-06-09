# Module 2 · Python Basics for Agent Builders
# Variables, functions, lists, dictionaries — the only Python you need to start.
# TYPE THIS YOURSELF. Only compare with this file after you have run yours.

# ──────────────────────────────────────────────────────────────────────
# Part 1: Variables — how agents store information
# ──────────────────────────────────────────────────────────────────────

your_name = "Emmanuel"          # text — always in quotes
your_goal = "Build a fraud agent"
your_industry = "FinTech"
max_steps = 10                  # number — no quotes
verbose = True                  # True or False — capital, no quotes

print(your_name)
print(your_goal)
print(your_industry)
print(max_steps)
print(verbose)


# ──────────────────────────────────────────────────────────────────────
# Part 2: Functions — every tool your agent has is written as a function
# ──────────────────────────────────────────────────────────────────────

def introduce_agent(name, purpose):
    """Returns a sentence introducing an agent."""
    intro = name + " is an agent that " + purpose
    return intro


result = introduce_agent("FraudBot", "investigates suspicious transactions")
print(result)


def calculate(expression):
    """Evaluates a math expression. Use for any calculations."""
    try:
        return str(eval(expression))
    except Exception:
        return "Error: could not calculate"


print(calculate("228 * 500"))   # 114000
print(calculate("100 / 4"))     # 25.0


# ──────────────────────────────────────────────────────────────────────
# Part 3: Lists — hold multiple items in order
# ──────────────────────────────────────────────────────────────────────

my_tools = ["calculate", "search_web", "send_email", "read_file"]
print(my_tools)
print(my_tools[0])              # first item — lists start at 0
print(len(my_tools))            # 4

for tool in my_tools:
    print("Available tool:", tool)


# ──────────────────────────────────────────────────────────────────────
# Part 4: Dictionaries — the format every AI API uses
# ──────────────────────────────────────────────────────────────────────

message = {
    "role": "user",
    "content": "Find the Apple stock price.",
}
print(message["role"])
print(message["content"])

# A conversation is a LIST of dictionaries. Every AI API uses this exact shape.
conversation = [
    {"role": "system", "content": "You are a helpful agent."},
    {"role": "user", "content": "Find the Apple stock price."},
]
print(len(conversation))        # 2
print(conversation[0])          # the system message
print(conversation[1])          # the user message

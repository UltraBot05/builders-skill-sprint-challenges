"""
Challenge 3: Agent with Persistent Memory
Give your agent memory that survives restarts using FAISS.
Model: Amazon Nova Pro via Bedrock

Instructions:
  1. Fill in the TODO sections below
  2. Run: python starter.py
  3. Store some facts, then quit and restart to verify persistence
"""

import os; os.environ["BYPASS_TOOL_CONSENT"] = "true"
from strands import Agent
from strands_tools import mem0_memory

MODEL = "us.amazon.nova-pro-v1:0"

agent = Agent(
    model=MODEL,
    tools=[mem0_memory],
    system_prompt=(
        "You are a helpful assistant with persistent memory. "
        "When the user tells you something about themselves, ALWAYS use mem0_memory to store it. "
        "When asked about the user, ALWAYS search memory first."
    )
)

print("🧠 Memory Agent Ready! Type 'quit' to exit.")
print("Bonus tip: store your name, city, and favourite food — then restart and ask 'What do you know about me?'\n")

while True:
    try:
        user_input = input("You: ").strip()
        if not user_input: continue
        if user_input.lower() in ("quit", "exit", "q"):
            print("Bye! 👋"); break
        agent(user_input)
        print()
    except KeyboardInterrupt:
        print("\nBye! 👋"); break

print("\n✅ Challenge 3 complete!")
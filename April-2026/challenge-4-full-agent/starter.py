"""
Challenge 4: The Full Agent — Tools + Memory + Streaming
Combine everything into one powerful agent.
Model: Amazon Nova Pro via Bedrock

Instructions:
  1. Fill in ALL the TODO sections
  2. Run: python starter.py
  3. Have a full conversation using all tools!
"""

import os; os.environ["BYPASS_TOOL_CONSENT"] = "true"
import requests
from datetime import date
from strands import Agent, tool
from strands_tools import calculator, mem0_memory

MODEL = "us.amazon.nova-pro-v1:0"

def stream_callback(**kwargs):
    if "data" in kwargs:
        print(kwargs["data"], end="", flush=True)
    elif "current_tool_use" in kwargs and kwargs["current_tool_use"].get("name"):
        print(f"\n🔧 Using tool: {kwargs['current_tool_use']['name']}")

@tool
def weather(city: str) -> str:
    """Get the current weather for a city.
    Args:
        city: The name of the city.
    """
    try:
        return requests.get(f"https://wttr.in/{city}?format=3", timeout=5).text.strip()
    except Exception as e:
        return f"Could not fetch weather: {e}"

@tool
def age_calculator(birth_date: str) -> str:
    """Calculate age from a birth date.
    Args:
        birth_date: Date of birth in YYYY-MM-DD format.
    """
    try:
        birth = date.fromisoformat(birth_date)
        today = date.today()
        age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        return f"Someone born on {birth_date} is {age} years old."
    except Exception as e:
        return f"Error: {e}"

# Bonus: countdown to a date
@tool
def days_until(target_date: str) -> str:
    """Calculate how many days until a future date.
    Args:
        target_date: Target date in YYYY-MM-DD format.
    """
    try:
        target = date.fromisoformat(target_date)
        today = date.today()
        delta = (target - today).days
        if delta > 0:
            return f"There are {delta} days until {target_date}."
        elif delta == 0:
            return f"Today is {target_date}!"
        else:
            return f"{target_date} was {abs(delta)} days ago."
    except Exception as e:
        return f"Error: {e}"

agent = Agent(
    model=MODEL,
    tools=[calculator, weather, age_calculator, days_until, mem0_memory],
    callback_handler=stream_callback,
    system_prompt=(
        "You are a helpful assistant with tools and persistent memory. "
        "Store personal info with mem0_memory. Search memory before answering personal questions. "
        "Use tools for math, weather, age, and date countdown questions."
    )
)

print("🤖 Full Agent Ready! Type 'quit' to exit.")
print("Try: 'How many days until 2025-12-25?' or 'What's the weather in Bangalore?'\n")

while True:
    try:
        user_input = input("You: ").strip()
        if not user_input: continue
        if user_input.lower() in ("quit", "exit", "q"):
            print("Bye! 👋"); break
        print("\nAgent: ", end="")
        agent(user_input)
        print()
    except KeyboardInterrupt:
        print("\nBye! 👋"); break

print("\n✅ Challenge 4 complete! 🏆")
"""
Challenge 2: Adding Tools to Your Agent
Give your agent a calculator, weather tool, and age calculator.
Model: Amazon Nova Pro via Bedrock

Instructions:
  1. Fill in the TODO sections below
  2. Run: python starter.py
  3. Needs AWS credentials configured (aws configure)
"""

import os; os.environ["BYPASS_TOOL_CONSENT"] = "true"
import requests
from datetime import date
from strands import Agent, tool
from strands_tools import calculator

MODEL = "us.amazon.nova-pro-v1:0"

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

# Bonus: km to miles converter
@tool
def km_to_miles(km: float) -> str:
    """Convert kilometers to miles.
    Args:
        km: Distance in kilometers.
    """
    miles = km * 0.621371
    return f"{km} km = {miles:.2f} miles"

agent = Agent(model=MODEL, tools=[calculator, weather, age_calculator, km_to_miles])

print("🧮 Math test:")
agent("What is 42 * 17?")

print("\n🌤️ Weather test:")
agent("What's the weather in Chennai?")

print("\n\n🎂 Age test:")
agent("How old is someone born on 2000-05-15?")

print("\n\n⭐ Bonus — two tools at once:")
agent("What's 20% of 714 and what's the weather in Mumbai?")

print("\n\n✅ Challenge 2 complete!")
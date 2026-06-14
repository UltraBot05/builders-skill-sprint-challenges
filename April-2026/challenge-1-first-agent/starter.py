"""
Challenge 1: Your First AI Agent
Build a simple agent using Strands SDK + Ollama (runs locally!)

Instructions:
  1. Fill in the TODO sections below
  2. Run: python starter.py
  3. Make sure 'ollama serve' is running in another terminal
"""

from strands import Agent
from strands.models.ollama import OllamaModel

model = OllamaModel(host="http://localhost:11434", model_id="llama3.2:3b")

# Normal agent
agent = Agent(model=model, system_prompt="You are a helpful assistant who gives fun, concise answers.", tools=[])

print("🤖 Challenge 1 - First Agent (Ollama)\n")
response = agent("Tell me a fun fact about Python programming language.")
print("\n")
# Bonus: pirate mode
print("\n🏴‍☠️ Bonus — Pirate mode!\n")
pirate_agent = Agent(model=model, system_prompt="You are a helpful pirate. Speak like one, arrr!", tools=[])
response2 = pirate_agent("Tell me a fun fact about Python programming language.")
print("\n")
print("\n✅ Challenge 1 complete!")
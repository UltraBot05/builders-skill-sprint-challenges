"""
Challenge 5 (Innovate): Build Your Own MCP-Powered Agent

YOUR TASK:
  Build an innovative agent from scratch that connects to any MCP server.
  The most creative and useful agent gets a special shoutout! 🏆

RULES:
  - Must use Strands Agents SDK
  - Must use at least one MCP server
  - Must use Amazon Nova Pro (or any Bedrock model)
  - Must have an interactive chat loop
  - Must be YOUR OWN idea — be creative!

EXAMPLE MCP SERVERS:
  pip install awslabs.aws-documentation-mcp-server   # AWS Docs
  uvx awslabs.cdk-mcp-server@latest                  # AWS CDK
  uvx awslabs.cost-analysis-mcp-server@latest        # AWS Pricing

BROWSE MORE: https://github.com/modelcontextprotocol/servers

RESOURCES:
  - Strands MCP docs: https://strandsagents.com/latest/user-guide/concepts/tools/mcp-tools/
  - AWS MCP servers: https://github.com/awslabs/mcp

Build something that makes us go "whoa!" 🚀
"""

# Your code here — build the entire agent from scratch!

"""
Challenge 5 (Innovate): Dev Productivity Agent
An AI-powered code assistant that reads your local files via MCP filesystem server.

Model: Amazon Nova Pro via Bedrock
MCP: @modelcontextprotocol/server-filesystem
"""

import os
os.environ["BYPASS_TOOL_CONSENT"] = "true"

from mcp import StdioServerParameters, stdio_client
from strands import Agent
from strands.models import BedrockModel
from strands.tools.mcp import MCPClient

MODEL = "us.amazon.nova-pro-v1:0"
WORKSPACE = os.path.abspath(".")

mcp_client = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="npx",
            args=["-y", "@modelcontextprotocol/server-filesystem", WORKSPACE],
        )
    )
)

with mcp_client:
    tools = mcp_client.list_tools_sync()
    model = BedrockModel(model_id=MODEL)

    agent = Agent(
        model=model,
        tools=tools,
        system_prompt=(
            "You are a senior software engineer and code reviewer. "
            f"You have access to the local filesystem at: {WORKSPACE}. "
            "You can read files, list directories, and help the user understand, "
            "review, debug, or improve their code. "
            "Always read the relevant file before answering code questions. "
            "Be concise, practical, and cite specific line numbers when relevant."
        )
    )

    print("💻 Dev Productivity Agent Ready!")
    print(f"📁 Workspace: {WORKSPACE}")
    print("Try: 'List all files here' or 'Review my starter.py'\n")

    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("quit", "exit", "q"):
                print("Bye! 👋")
                break
            agent(user_input)
            print()
        except KeyboardInterrupt:
            print("\nBye! 👋")
            break

    print("\n✅ Challenge 5 complete!")
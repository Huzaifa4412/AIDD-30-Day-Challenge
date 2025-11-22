# app.py
import sys
import os

# Add the virtual environment's site-packages to sys.path
# This is a workaround for ModuleNotFoundError when running via Chainlit
# It constructs the path relative to the current file.
current_dir = os.path.dirname(os.path.abspath(__file__))
venv_path = os.path.join(current_dir, '.venv')
site_packages_path = os.path.join(venv_path, 'Lib', 'site-packages') # For Windows
# For Linux/macOS, it would be: os.path.join(venv_path, 'lib', 'pythonX.Y', 'site-packages')

if site_packages_path not in sys.path:
    sys.path.insert(0, site_packages_path)

import chainlit as cl
from openai_agents import Runner
from agent import agent # Import the configured agent

@cl.on_chat_start
async def start():
    """
    Initializes the agent and sends a static welcome message when a new chat starts.
    """
    cl.user_session.set("agent_runner", Runner(agent))
    await cl.Message(content="Hello, how can I assist you today?").send()

@cl.on_message
async def main(message: cl.Message):
    """
    Handles incoming user messages, passes them to the agent, and sends the agent's response back to the UI.
    """
    agent_runner = cl.user_session.get("agent_runner")  # type: Runner

    # Run the agent with the user's message
    result = await agent_runner.run(message.content)

    # Send the final output from the agent to the UI
    await cl.Message(content=result.final_output).send()

    # Debug: Print tool outputs if any
    if result.tool_calls:
        for tool_call in result.tool_calls:
            print(f"Tool Called: {tool_call.name} with args {tool_call.arguments}")
    if result.tool_outputs:
        for tool_output in result.tool_outputs:
            print(f"Tool Output: {tool_output.output}")

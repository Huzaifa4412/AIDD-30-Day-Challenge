# agent.py
import os
from openai import AsyncOpenAI
from openai_agents import Agent, OpenAIChatCompletionsModel
from tools import read_user_profile, update_user_profile
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

# API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
MODEL_NAME = "gemini-2.0-flash"

# Initialize AsyncOpenAI client for Gemini
gemini_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=BASE_URL,
)

# Initialize OpenAIChatCompletionModel adapted for Gemini
gemini_model = OpenAIChatCompletionsModel(
    model=MODEL_NAME,
    openai_client=gemini_client,
)

# Configure the Agent
agent = Agent(
    name="PersonalChatbot",
    instructions="Greet users by name if known. Detect when users share personal info and save it using tools.",
    tools=[read_user_profile, update_user_profile],
    model=gemini_model,
)

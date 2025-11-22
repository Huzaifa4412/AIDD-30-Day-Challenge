import os
import asyncio
from openai_agents import Agent

def get_gemini_config():
    """
    Constructs the LLM configuration for using a Gemini model via OpenRouter.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return "Error: GEMINI_API_KEY environment variable not set."

    return {
        "model_name": "google/gemini-2.0-flash-001",
        "provider": "openai_endpoint",
        "openai_endpoint_url": "https://openrouter.ai/api/v1",
        "api_key": api_key,
    }

def generate_summary(text):
    """
    Generates a structured summary from the given text using a Gemini model
    via the openai-agents SDK.
    """
    llm_config = get_gemini_config()
    if isinstance(llm_config, str):
        return llm_config

    instructions = f"""
    You are a professional summarizer.
    Generate a comprehensive and well-structured summary of the provided text.
    The summary should be formatted as follows:

    1.  **Bullet-Point Notes:** Key takeaways and important facts in a concise list.
    2.  **Structured Summary:** A clean, paragraph-based summary of the main topics.
    3.  **Key Concepts & Definitions:** A list of important terms and their definitions from the text.
    4.  **Multi-Section Insights:** Deeper insights or connections found across different sections of the text.
    
    The final output should be ONLY the summary, without any conversational preamble or sign-off.
    """
    
    agent = Agent(
        llm_config=llm_config,
        instructions=instructions,
        name="Summarizer",
        auto_run=True,
    )

    prompt = f"""
    Here is the text to summarize:
    ---
    {text}
    ---
    """
    
    try:
        # Run the agent asynchronously
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(agent.arun(prompt=prompt))
        loop.close()
        
        # The result is often an object/dictionary, extract the core message
        if hasattr(result, 'message'):
            return result.message
        return str(result)
    except Exception as e:
        return f"An error occurred during summary generation: {e}"





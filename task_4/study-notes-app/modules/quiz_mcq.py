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

def generate_mcq_quiz(text):
    """
    Generates an MCQ quiz from the given text using a Gemini model
    via the openai-agents SDK.
    """
    llm_config = get_gemini_config()
    if isinstance(llm_config, str):
        return llm_config

    instructions = f"""
    You are an expert quiz generator. Your task is to create a multiple-choice question (MCQ) quiz
    based on the provided text. Adhere strictly to the following format for each question:

    Q1: [Question text]?
    A. Option 1
    B. Option 2
    C. Option 3
    D. Option 4
    Correct Answer: [Letter of correct option, e.g., C]

    Generate at least 5 MCQs. Ensure the questions and options are directly derived from the text
    and there is only one correct answer per question. The final output should contain ONLY the quiz,
    without any conversational preamble or sign-off.
    """
    
    agent = Agent(
        llm_config=llm_config,
        instructions=instructions,
        name="MCQ_Quiz_Generator",
        auto_run=True,
    )

    prompt = f"""
    Here is the text from which to generate the MCQ quiz:
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
        
        if hasattr(result, 'message'):
            return result.message
        return str(result)
    except Exception as e:
        return f"An error occurred during MCQ quiz generation: {e}"

"""
Groq LLM Configuration
Stitches By S AI Chatbot
"""

from langchain_groq import ChatGroq
from config import GROQ_API_KEY, LLM_MODEL


def get_llm(temperature: float = 0.2):
    """
    Return a configured Groq LLM instance.
    """

    if not GROQ_API_KEY:
        raise ValueError(
            "GROQ_API_KEY not found. Please create a .env file and add your API key."
        )

    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model=LLM_MODEL,
        temperature=temperature,
    )

    return llm

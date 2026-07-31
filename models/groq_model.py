"""
Groq LLM Configuration
Stitches By S AI Chatbot
"""

import os

from langchain_groq import ChatGroq
from config import LLM_MODEL


def get_llm(temperature: float = 0.2):
    """
    Return a configured Groq LLM instance.
    """

    # Always read the latest environment variable
    groq_api_key = os.getenv("GROQ_API_KEY")

    if not groq_api_key:
        raise ValueError(
            "GROQ_API_KEY not found. Set it in your environment or .env file."
        )

    llm = ChatGroq(
        api_key=groq_api_key,
        model=LLM_MODEL,
        temperature=temperature,
    )

    return llm

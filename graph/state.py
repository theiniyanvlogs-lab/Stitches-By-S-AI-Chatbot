"""
==========================================================
Stitches By S AI Chatbot
LangGraph State
==========================================================
"""

from typing import TypedDict


class ChatState(TypedDict):
    """
    Shared state across the LangGraph workflow.
    """

    question: str
    route: str
    answer: str
    history: str

"""
==========================================================
Stitches By S AI Chatbot
LangGraph Nodes
==========================================================
"""

from models.groq_model import get_llm

from agents.fabric_agent import FabricAgent
from agents.tailoring_agent import TailoringAgent
from agents.business_agent import BusinessAgent

from graph.state import ChatState


llm = get_llm()

fabric = FabricAgent()
tailoring = TailoringAgent()
business = BusinessAgent()


def supervisor_node(state: ChatState):

    question = state["question"]

    prompt = f"""
You are a routing AI.

Available experts

fabric

tailoring

business

Return ONLY one word.

Question:

{question}
"""

    response = llm.invoke(prompt)

    return {
        "route": response.content.strip().lower()
    }


def fabric_node(state: ChatState):

    answer = fabric.ask(state["question"])

    return {
        "answer": answer
    }


def tailoring_node(state: ChatState):

    answer = tailoring.ask(state["question"])

    return {
        "answer": answer
    }


def business_node(state: ChatState):

    answer = business.ask(state["question"])

    return {
        "answer": answer
    }

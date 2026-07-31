"""
==========================================================
Stitches By S AI Chatbot
Supervisor Agent
==========================================================

Routes user questions to the appropriate
AI agent(s).

Author : Sugumar R
==========================================================
"""

from models.groq_model import get_llm

from agents.fabric_agent import FabricAgent
from agents.tailoring_agent import TailoringAgent
from agents.business_agent import BusinessAgent


class SupervisorAgent:
    """
    Routes user questions to the correct expert.
    """

    def __init__(self):

        self.llm = get_llm()

        self.fabric = FabricAgent()

        self.tailoring = TailoringAgent()

        self.business = BusinessAgent()

    def route(self, question: str):

        prompt = f"""
You are an AI Supervisor.

Decide which expert should answer the question.

Available Experts

1. fabric
2. tailoring
3. business

Rules

Return ONLY one of:

fabric

tailoring

business

Question:

{question}
"""

        response = self.llm.invoke(prompt)

        agent = response.content.strip().lower()

        if "fabric" in agent:
            return self.fabric.ask(question)

        elif "tailoring" in agent:
            return self.tailoring.ask(question)

        elif "business" in agent:
            return self.business.ask(question)

        return (
            "Sorry, I couldn't determine the "
            "correct expert for this question."
        )

"""
==========================================================
Stitches By S AI Chatbot
Business Expert AI Agent
==========================================================

Answers tailoring business-related questions
using RAG + Groq LLM.

Author : Sugumar R
==========================================================
"""

from langchain_core.prompts import ChatPromptTemplate

from models.groq_model import get_llm
from rag.retriever import KnowledgeRetriever


class BusinessAgent:
    """
    AI Agent specializing in tailoring business.
    """

    def __init__(self):

        self.llm = get_llm()

        self.retriever = KnowledgeRetriever()

        self.prompt = ChatPromptTemplate.from_template(
            """
You are an experienced tailoring business consultant.

Answer ONLY using the retrieved knowledge.

If the answer is unavailable, clearly say:

"I couldn't find this information in the Business Knowledge Base."

Context:

{context}

Question:

{question}

Provide:

• Direct Answer

• Business Recommendation

• Best Practices

• Additional Tips
"""
        )

    def ask(self, question: str):

        docs = self.retriever.search(
            category="business",
            query=question,
            k=4,
        )

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        chain = self.prompt | self.llm

        response = chain.invoke(
            {
                "context": context,
                "question": question,
            }
        )

        return response.content

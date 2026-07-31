"""
==========================================================
Stitches By S AI Chatbot
Fabric Expert AI Agent
==========================================================

Answers fabric-related questions using
RAG + Groq LLM.

Author : Sugumar R
==========================================================
"""

from langchain_core.prompts import ChatPromptTemplate

from models.groq_model import get_llm
from rag.retriever import KnowledgeRetriever


class FabricAgent:
    """
    AI Agent specializing in fabrics.
    """

    def __init__(self):

        self.llm = get_llm()

        self.retriever = KnowledgeRetriever()

        self.prompt = ChatPromptTemplate.from_template(
            """
You are an expert textile consultant.

Answer ONLY using the retrieved knowledge.

If the answer is unavailable, clearly say:

"I couldn't find this information in the Fabric Knowledge Base."

Context:

{context}

Question:

{question}

Provide:

• Direct Answer

• Additional Tips

• Best Practices
"""
        )

    def ask(self, question: str):

        docs = self.retriever.search(
            category="fabric",
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

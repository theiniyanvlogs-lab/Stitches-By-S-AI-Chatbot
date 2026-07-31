"""
==========================================================
Stitches By S AI Chatbot
Semantic Retriever
==========================================================

Loads FAISS vector databases and retrieves
the most relevant document chunks.

Author : Sugumar R
==========================================================
"""

from config import (
    FABRIC_DB,
    TAILORING_DB,
    BUSINESS_DB,
)

from rag.vector_store import VectorStoreManager


class KnowledgeRetriever:
    """
    Semantic search over FAISS databases.
    """

    def __init__(self):

        manager = VectorStoreManager()

        self.fabric_db = manager.load_vector_store(
            FABRIC_DB
        )

        self.tailoring_db = manager.load_vector_store(
            TAILORING_DB
        )

        self.business_db = manager.load_vector_store(
            BUSINESS_DB
        )

    def search(
        self,
        category: str,
        query: str,
        k: int = 4,
    ):
        """
        Search one knowledge base.
        """

        databases = {

            "fabric": self.fabric_db,

            "tailoring": self.tailoring_db,

            "business": self.business_db,

        }

        if category not in databases:

            raise ValueError(
                f"Unknown category: {category}"
            )

        retriever = databases[
            category
        ].as_retriever(

            search_type="similarity",

            search_kwargs={
                "k": k
            }

        )

        return retriever.invoke(query)

    def search_all(
        self,
        query: str,
        k: int = 3,
    ):
        """
        Search every knowledge base.
        """

        return {

            "fabric":
                self.search(
                    "fabric",
                    query,
                    k,
                ),

            "tailoring":
                self.search(
                    "tailoring",
                    query,
                    k,
                ),

            "business":
                self.search(
                    "business",
                    query,
                    k,
                ),

        }

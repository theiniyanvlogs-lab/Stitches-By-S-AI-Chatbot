"""
==========================================================
Stitches By S AI Chatbot
FAISS Vector Store
==========================================================

Creates, saves, and loads FAISS vector databases.

Author : Sugumar R
==========================================================
"""

from pathlib import Path

from langchain_community.vectorstores import FAISS

from rag.embeddings import get_embedding_model


class VectorStoreManager:
    """
    Handles FAISS vector database operations.
    """

    def __init__(self):

        self.embedding_model = get_embedding_model()

    def create_vector_store(self, documents):
        """
        Create FAISS index from documents.
        """

        if not documents:
            raise ValueError("No documents available to create vector store.")

        print(f"Creating vector store from {len(documents)} chunks...")

        vector_store = FAISS.from_documents(
            documents=documents,
            embedding=self.embedding_model,
        )

        return vector_store

    def save_vector_store(
        self,
        vector_store,
        save_path: str,
    ):
        """
        Save FAISS index to disk.
        """

        save_dir = Path(save_path)
        save_dir.mkdir(parents=True, exist_ok=True)

        vector_store.save_local(str(save_dir))

        print(f"Vector store saved to: {save_dir}")

    def load_vector_store(
        self,
        save_path: str,
    ):
        """
        Load FAISS index from disk.
        """

        save_dir = Path(save_path)

        if not save_dir.exists():
            raise FileNotFoundError(
                f"Vector database not found: {save_dir}"
            )

        print(f"Loading vector store: {save_dir}")

        return FAISS.load_local(
            str(save_dir),
            self.embedding_model,
            allow_dangerous_deserialization=True,
        )

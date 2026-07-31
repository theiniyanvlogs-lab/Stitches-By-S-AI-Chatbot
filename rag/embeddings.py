"""
==========================================================
Stitches By S AI Chatbot
Embedding Model
==========================================================

Creates SentenceTransformer embeddings
for FAISS vector database.

Author : Sugumar R
==========================================================
"""

from langchain_huggingface import HuggingFaceEmbeddings

from config import EMBEDDING_MODEL


class EmbeddingModel:
    """
    Singleton embedding model.

    Loads the embedding model only once.
    """

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance.embedding = HuggingFaceEmbeddings(

                model_name=EMBEDDING_MODEL,

                model_kwargs={
                    "device": "cpu"
                },

                encode_kwargs={
                    "normalize_embeddings": True
                }

            )

        return cls._instance

    def get_embedding(self):

        return self.embedding


def get_embedding_model():
    """
    Returns embedding model.
    """

    return EmbeddingModel().get_embedding()

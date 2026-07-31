"""
==========================================================
Stitches By S AI Chatbot
Build Tailoring Knowledge Base
==========================================================
"""

from config import (
    TAILORING_DATA,
    TAILORING_DB,
)

from rag.loader import PDFLoader
from rag.splitter import DocumentSplitter
from rag.vector_store import VectorStoreManager


def main():

    print("=" * 60)
    print("Building Tailoring Knowledge Base")
    print("=" * 60)

    # Load PDFs
    loader = PDFLoader(TAILORING_DATA)
    documents = loader.load_documents()

    # Split Documents
    splitter = DocumentSplitter()
    chunks = splitter.split(documents)

    # Create Vector Store
    manager = VectorStoreManager()
    vector_store = manager.create_vector_store(chunks)

    # Save Vector Store
    manager.save_vector_store(
        vector_store,
        TAILORING_DB,
    )

    print("\nTailoring Knowledge Base Created Successfully!")


if __name__ == "__main__":
    main()

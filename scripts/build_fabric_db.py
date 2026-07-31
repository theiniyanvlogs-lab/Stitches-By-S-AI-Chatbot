"""
==========================================================
Stitches By S AI Chatbot
Build Fabric Knowledge Base
==========================================================
"""

from config import (
    FABRIC_DATA,
    FABRIC_DB,
)

from rag.loader import PDFLoader
from rag.splitter import DocumentSplitter
from rag.vector_store import VectorStoreManager


def main():

    print("=" * 60)
    print("Building Fabric Knowledge Base")
    print("=" * 60)

    # Load PDFs
    loader = PDFLoader(FABRIC_DATA)
    documents = loader.load_documents()

    # Split Documents
    splitter = DocumentSplitter()
    chunks = splitter.split(documents)

    # Build Vector Store
    manager = VectorStoreManager()
    vector_store = manager.create_vector_store(chunks)

    # Save
    manager.save_vector_store(
        vector_store,
        FABRIC_DB,
    )

    print("\nFabric Knowledge Base Created Successfully!")


if __name__ == "__main__":
    main()

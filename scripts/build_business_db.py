"""
==========================================================
Stitches By S AI Chatbot
Build Business Knowledge Base
==========================================================
"""

# ==========================================================
# FIX PYTHON IMPORT PATH
# ==========================================================

import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# ==========================================================
# IMPORTS
# ==========================================================

from config import (
    BUSINESS_DATA,
    BUSINESS_DB,
)

from rag.loader import PDFLoader
from rag.splitter import DocumentSplitter
from rag.vector_store import VectorStoreManager


# ==========================================================
# BUILD VECTOR DATABASE
# ==========================================================

def main():

    print("=" * 60)
    print("Building Business Knowledge Base")
    print("=" * 60)

    # Load PDFs
    loader = PDFLoader(BUSINESS_DATA)
    documents = loader.load_documents()

    print(f"Loaded {len(documents)} documents")

    # Split Documents
    splitter = DocumentSplitter()
    chunks = splitter.split(documents)

    print(f"Created {len(chunks)} chunks")

    # Create Vector Store
    manager = VectorStoreManager()
    vector_store = manager.create_vector_store(chunks)

    # Save Vector Store
    manager.save_vector_store(
        vector_store,
        BUSINESS_DB,
    )

    print("\n✅ Business Knowledge Base Created Successfully!")
    print(f"Saved to: {BUSINESS_DB}")


# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":
    main()

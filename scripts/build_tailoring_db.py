"""
==========================================================
Stitches By S AI Chatbot
Build Tailoring Knowledge Base
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
    TAILORING_DATA,
    TAILORING_DB,
)

from rag.loader import PDFLoader
from rag.splitter import DocumentSplitter
from rag.vector_store import VectorStoreManager


# ==========================================================
# BUILD TAILORING VECTOR DATABASE
# ==========================================================

def main():

    print("=" * 60)
    print("Building Tailoring Knowledge Base")
    print("=" * 60)

    # ------------------------------------------------------
    # Load PDFs
    # ------------------------------------------------------

    loader = PDFLoader(TAILORING_DATA)
    documents = loader.load_documents()

    print(f"✅ Loaded {len(documents)} document(s)")

    # ------------------------------------------------------
    # Split Documents
    # ------------------------------------------------------

    splitter = DocumentSplitter()
    chunks = splitter.split(documents)

    print(f"✅ Created {len(chunks)} chunk(s)")

    # ------------------------------------------------------
    # Create Vector Store
    # ------------------------------------------------------

    manager = VectorStoreManager()
    vector_store = manager.create_vector_store(chunks)

    # ------------------------------------------------------
    # Save Vector Store
    # ------------------------------------------------------

    manager.save_vector_store(
        vector_store,
        TAILORING_DB,
    )

    print("\n" + "=" * 60)
    print("✅ Tailoring Knowledge Base Created Successfully!")
    print(f"📁 Saved to : {TAILORING_DB}")
    print("=" * 60)


# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":
    main()

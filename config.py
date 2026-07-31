"""
Stitches By S AI Chatbot
Configuration File
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ===============================
# API
# ===============================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ===============================
# LLM
# ===============================

LLM_MODEL = "llama-3.3-70b-versatile"

# ===============================
# Embedding Model
# ===============================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ===============================
# Chunk Settings
# ===============================

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# ===============================
# PDF Paths
# ===============================

FABRIC_DATA = "data/fabric"
TAILORING_DATA = "data/tailoring"
BUSINESS_DATA = "data/business"

# ===============================
# Vector DB
# ===============================

FABRIC_DB = "vector_db/fabric"
TAILORING_DB = "vector_db/tailoring"
BUSINESS_DB = "vector_db/business"

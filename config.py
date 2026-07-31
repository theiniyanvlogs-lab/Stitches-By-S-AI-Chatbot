"""
Stitches By S AI Chatbot
Configuration File
"""

import os
from dotenv import load_dotenv

# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()

# ==========================================================
# Project Root
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ==========================================================
# API
# ==========================================================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ==========================================================
# LLM
# ==========================================================

LLM_MODEL = "llama-3.3-70b-versatile"

# ==========================================================
# Embedding Model
# ==========================================================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ==========================================================
# Chunk Settings
# ==========================================================

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# ==========================================================
# Data Directories
# ==========================================================

DATA_DIR = os.path.join(BASE_DIR, "data")

FABRIC_DATA = os.path.join(DATA_DIR, "fabric")
TAILORING_DATA = os.path.join(DATA_DIR, "tailoring")
BUSINESS_DATA = os.path.join(DATA_DIR, "business")

# ==========================================================
# Vector Database Directories
# ==========================================================

VECTOR_DB_DIR = os.path.join(BASE_DIR, "vector_db")

FABRIC_DB = os.path.join(VECTOR_DB_DIR, "fabric")
TAILORING_DB = os.path.join(VECTOR_DB_DIR, "tailoring")
BUSINESS_DB = os.path.join(VECTOR_DB_DIR, "business")

# ==========================================================
# Create Required Directories
# ==========================================================

os.makedirs(FABRIC_DATA, exist_ok=True)
os.makedirs(TAILORING_DATA, exist_ok=True)
os.makedirs(BUSINESS_DATA, exist_ok=True)

os.makedirs(FABRIC_DB, exist_ok=True)
os.makedirs(TAILORING_DB, exist_ok=True)
os.makedirs(BUSINESS_DB, exist_ok=True)

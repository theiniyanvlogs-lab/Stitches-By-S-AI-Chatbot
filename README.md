# 👗 Stitches By S AI Chatbot

## AI-Powered Multi-Agent Tailoring Knowledge Assistant

Stitches By S AI Chatbot is an intelligent Multi-Agent AI application built using **LangGraph**, **LangChain**, **Groq LLM**, **FAISS**, and **Gradio**.

The chatbot assists tailoring professionals and customers by answering questions related to fabrics, tailoring techniques, measurements, stitching methods, pricing, and tailoring business management using Retrieval-Augmented Generation (RAG).

---

# Features

- Multi-Agent AI Architecture
- LangGraph Workflow
- Retrieval-Augmented Generation (RAG)
- FAISS Vector Database
- Groq LLM Integration
- PDF Knowledge Base
- Conversation Memory
- Professional Gradio Interface
- Modular Python Code
- Hugging Face Deployment Ready

---

# AI Expert Agents

### 🧵 Fabric Expert

- Fabric Selection
- Fabric Properties
- Fabric Care
- Seasonal Recommendations
- Material Comparison

---

### ✂️ Tailoring Expert

- Measurements
- Cutting
- Stitching
- Neck Designs
- Sleeve Designs
- Alterations
- Sewing Tips

---

### 💼 Business Expert

- Pricing
- Profit Calculation
- Customer Management
- Marketing
- Order Management
- Business Growth

---

# Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| LangChain | RAG Pipeline |
| LangGraph | Multi-Agent Workflow |
| Groq | Large Language Model |
| Sentence Transformers | Embeddings |
| FAISS | Vector Database |
| Gradio | Web Interface |
| PyPDF | PDF Loader |
| Hugging Face Spaces | Deployment |
| GitHub | Version Control |

---

# Project Architecture

```text
                    User
                     │
                     ▼
              Gradio Interface
                     │
                     ▼
             LangGraph Workflow
                     │
              Supervisor Agent
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
Fabric Agent   Tailoring Agent   Business Agent
      │              │              │
      ▼              ▼              ▼
 Fabric DB      Tailoring DB    Business DB
      │              │              │
      └──────────────┼──────────────┘
                     ▼
                  Groq LLM
                     │
                     ▼
              Professional Answer
```

---

# Project Structure

```text
StitchesByS-AI-Chatbot/

│

├── agents/

├── graph/

├── rag/

├── prompts/

├── memory/

├── models/

├── scripts/

├── utils/

├── data/

├── vector_db/

├── static/

├── assets/

│

├── app.py

├── config.py

├── requirements.txt

├── README.md

└── LICENSE
```

---

# Installation

```bash
git clone https://github.com/YOUR_USERNAME/StitchesByS-AI-Chatbot.git

cd StitchesByS-AI-Chatbot

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

---

# Environment Variable

Create a `.env` file

```text
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

# Build Knowledge Base

```bash
python scripts/build_fabric_db.py

python scripts/build_tailoring_db.py

python scripts/build_business_db.py
```

---

# Run Application

```bash
python app.py
```

---

# Example Questions

### Fabric

- Which fabric is best for summer?
- What is the difference between cotton and linen?

### Tailoring

- How do I take blouse measurements?
- How do I stitch a princess-cut blouse?

### Business

- How should I price a designer blouse?
- How can I increase tailoring orders?

---

# Future Improvements

- Voice Chat
- Image Upload
- OCR for Measurement Sheets
- Speech-to-Text
- Text-to-Speech
- WhatsApp Integration
- Customer Order Tracking
- Appointment Scheduling

---

# License

MIT License

---

# Author

**Sugumar R**

MBA | AI Developer

AI-Powered Multi-Agent Applications

GitHub Portfolio Project

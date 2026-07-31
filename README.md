# 👗 Stitches By S AI Chatbot

> **AI-Powered Multi-Agent Tailoring Knowledge Assistant using LangGraph, LangChain, RAG, FAISS, Groq LLM, and Gradio**

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-orange)
![FAISS](https://img.shields.io/badge/VectorDB-FAISS-red)
![Groq](https://img.shields.io/badge/LLM-Groq-purple)
![Gradio](https://img.shields.io/badge/UI-Gradio-blue)

---

# 📌 Project Overview

**Stitches By S AI Chatbot** is an intelligent **Multi-Agent AI Assistant** designed for the tailoring and fashion industry.

The chatbot understands tailoring, fabrics, garment stitching, measurements, sewing techniques, and tailoring business management using **Retrieval-Augmented Generation (RAG)**.

Instead of relying only on an LLM, the chatbot retrieves accurate information from its own knowledge base stored in **FAISS Vector Databases**.

---

# 🎯 Objectives

- Build a Tailoring AI Assistant
- Implement Multi-Agent AI architecture
- Use Retrieval-Augmented Generation (RAG)
- Learn LangGraph Agent Workflow
- Perform Semantic Search using FAISS
- Build an industry-specific AI knowledge assistant

---

# 🚀 Features

✅ Multi-Agent AI Architecture

✅ Supervisor Agent

✅ Fabric Expert Agent

✅ Tailoring Expert Agent

✅ Business Expert Agent

✅ Retrieval-Augmented Generation (RAG)

✅ Semantic Search using FAISS

✅ PDF Knowledge Base

✅ LangGraph Workflow

✅ Conversation Memory

✅ Groq LLM Integration

✅ Gradio Chat Interface

---

# 🧠 Multi-Agent Architecture

```
                     User Question
                           │
                           ▼
                  Supervisor Agent
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
 Fabric Expert      Tailoring Expert     Business Expert
        │                  │                  │
        ▼                  ▼                  ▼
      FAISS             FAISS             FAISS
   Vector Store      Vector Store      Vector Store
        │                  │                  │
        └──────────────┬──────────────────────┘
                       ▼
                Retrieved Context
                       ▼
                  Groq LLM
                       ▼
                Final AI Response
```

---

# 🤖 AI Agents

## 🧵 Fabric Expert

Answers questions related to

- Cotton
- Silk
- Linen
- Rayon
- Polyester
- Fabric Care
- Fabric Selection

---

## ✂️ Tailoring Expert

Answers questions related to

- Body Measurements
- Stitch Types
- Sewing Techniques
- Pattern Making
- Fabric Cutting
- Tailoring Tips

---

## 💼 Business Expert

Answers questions related to

- Tailoring Business
- Pricing
- Customer Management
- Marketing
- Business Growth
- Profit Planning

---

# 📚 RAG Knowledge Base

The chatbot retrieves knowledge from three independent vector databases.

| Knowledge Base | Description |
|---------------|-------------|
| Fabric | Fabric properties, care, usage |
| Tailoring | Measurements, stitching, sewing |
| Business | Tailoring business management |

---

# 🧩 Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | LangChain |
| Multi-Agent | LangGraph |
| LLM | Groq (Llama 3.3 70B) |
| Embedding Model | all-MiniLM-L6-v2 |
| Vector Database | FAISS |
| PDF Loader | PyPDF |
| UI | Gradio |
| Memory | Conversation Memory |
| Environment | Python Dotenv |

---

# 📂 Project Structure

```
Stitches-By-S-AI-Chatbot/

├── agents/
│   ├── fabric_agent.py
│   ├── tailoring_agent.py
│   ├── business_agent.py
│   └── supervisor.py
│
├── graph/
│   ├── workflow.py
│   ├── nodes.py
│   └── state.py
│
├── rag/
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── retriever.py
│   └── vector_store.py
│
├── memory/
│
├── prompts/
│
├── models/
│
├── scripts/
│
├── utils/
│
├── data/
│
├── vector_db/
│
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/theiniyanvlogs-lab/Stitches-By-S-AI-Chatbot.git
```

Move into the project

```bash
cd Stitches-By-S-AI-Chatbot
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file

```
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

# ▶️ Run Application

```bash
python app.py
```

---

# 💬 Sample Questions

### Fabric

- Explain cotton fabric.
- What are the advantages of cotton?
- How should I wash cotton garments?

### Tailoring

- Explain back stitch.
- How do I take body measurements?
- What are the common stitch types?

### Business

- How can I grow my tailoring business?
- How should I price tailoring services?
- Give me tailoring marketing ideas.

---

# 📈 Future Improvements

- Voice-based chatbot
- Multilingual support
- Image-based fabric identification
- AI blouse design recommendations
- Tailoring pattern generation
- WhatsApp chatbot integration
- Mobile application
- Admin Dashboard
- Cloud Deployment

---

# 📸 Screenshots

(Add your chatbot screenshots here)

---

# 🎓 Learning Outcomes

This project demonstrates practical knowledge of

- Multi-Agent AI
- Agent Routing
- LangGraph
- LangChain
- Retrieval-Augmented Generation
- FAISS
- Prompt Engineering
- Vector Databases
- Semantic Search
- LLM Integration
- AI Chatbot Development

---

# 👨‍💻 Author

**Sugumar R**

MBA | AI Developer | Multi-Agent AI Enthusiast

📧 contact.sugumarai@gmail.com

GitHub

https://github.com/theiniyanvlogs-lab

---

# ⭐ Support

If you found this project useful,

⭐ Star this repository

🍴 Fork the repository

🤝 Contribute improvements

---

# 📄 License

This project is licensed under the MIT License.

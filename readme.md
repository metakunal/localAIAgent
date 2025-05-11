# 🧠 Local AI Agent for Restaurant Reviews

A lightweight local AI agent that lets you **query restaurant reviews from a CSV file** using **TinyLLaMA** for language generation and **mxbai-embed-large** for vector embeddings. Powered by **ChromaDB** as the vector store for fast local semantic search.

---

## 🚀 Features

- 🗂️ Load and index reviews from `realistic_restaurant_reviews.csv`
- 🤖 Uses `mxbai-embed-large` to embed your data for semantic search
- 📦 Stores embeddings locally using `ChromaDB` (no cloud, fully local)
- 🔍 Query the reviews via a local TinyLLaMA model (`tinyllama`)
- ⚡ Skips re-embedding if database already exists

---

## 🛠️ Setup Instructions

```bash
git clone https://github.com/metakunal/localAIAgent
cd localAIAgent

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt


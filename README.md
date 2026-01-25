# AI Document Assistant using Retrieval-Augmented Generation (RAG)

## 📌 Project Overview

The **AI Document Assistant** is an end-to-end Retrieval-Augmented Generation (RAG) application that converts video content into searchable knowledge and enables users to ask natural language questions to get accurate, context-aware answers. This project demonstrates practical use of **LLMs, embeddings, vector databases, and information retrieval**.

This project is **ATS-friendly** and suitable for showcasing skills in **Data Science, Machine Learning, NLP, and LLM-based application development**.

---

## 🎯 Problem Statement

Large video and document content is difficult to search and query efficiently. Traditional keyword search fails to capture semantic meaning.

**Solution:**
Build a system that:

* Converts videos into text
* Stores semantic embeddings
* Retrieves relevant context using vector search
* Generates precise answers using an LLM

---

## 🚀 Key Features

* Video to audio conversion
* Automatic speech-to-text transcription using OpenAI Whisper
* Text chunking and semantic embeddings
* Fast similarity search using FAISS
* Context-aware answer generation using LLM (RAG architecture)
* Modular and scalable pipeline

---

## 🧠 Architecture (RAG Pipeline)

1. **Ingestion**: Video → Audio → Transcript
2. **Embedding Store**: Transcript chunking → Vector embeddings → FAISS index
3. **Retriever**: Semantic search for top-k relevant chunks
4. **Generator**: LLM generates answers using retrieved context

---

## 🛠️ Technologies Used

* **Python**
* **OpenAI Whisper** (Speech-to-Text)
* **Sentence Transformers (all-MiniLM-L6-v2)**
* **FAISS** (Vector Database)
* **OpenAI API** (LLM for answer generation)
* **MoviePy** (Video processing)
* **NumPy**

---

## 📂 Project Structure

```
AI-Document-Assistant-using-RAG/
│
├── videos/                # Input video files (.mp4)
├── audio/                 # Extracted audio files
├── transcripts/           # Generated transcripts (.txt)
├── embeddings/            # FAISS index and embeddings
│   ├── faiss.index
│   └── chunks.npy
│
├── ingest.py              # Phase 1: Video → Audio → Transcript
├── embed_store.py         # Phase 2: Text chunking & embedding creation
├── retriever.py           # Phase 3: Semantic retrieval using FAISS
├── rag_pipeline.py        # Phase 4: RAG (Retriever + LLM)
├── app.py                 # Phase 5: UI layer (Streamlit web application)
├── requirements.txt       # Project dependencies
├── setup.py               # Phase 0: Initial project setup & environment validation
└── README.md
```

## ⚙️ Installation & Setup
````
```bash
# Clone repository
git clone https://github.com/your-username/AI-Document-Assistant-using-RAG.git
cd AI-Document-Assistant-using-RAG
---
---
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
---
---
# Install dependencies
pip install -r requirements.txt
````

Set your OpenAI API key:

```bash
export OPENAI_API_KEY="your_api_key"  # Windows: setx OPENAI_API_KEY "your_api_key"
```

---

## ▶️ How to Run (Phase-wise Execution)

### 🔹 Step 0: Initial Setup

```bash
python setup.py
```

* Validates environment
* Checks required folders
* Ensures dependencies are installed

---

### 🔹 Phase 1: Video to Text (Ingestion)

```bash
python ingest.py
```

* Converts video to audio
* Transcribes audio using Whisper
* Saves transcripts to `transcripts/`

---

### 🔹 Phase 2: Embedding & Vector Store Creation

```bash
python embed_store.py
```

* Splits transcripts into chunks
* Generates embeddings using Sentence Transformers
* Stores vectors in FAISS index

---

### 🔹 Phase 3: Semantic Retrieval (Optional Test)

```bash
python retriever.py
```

* Retrieves top-k relevant chunks
* Useful for debugging and validation

---

### 🔹 Phase 4: RAG Pipeline (LLM Answering)

```bash
python rag_pipeline.py
```

* Retrieves context using FAISS
* Generates answers using LLM

---

### 🔹 Phase 5: UI Layer (Streamlit App)

```bash
streamlit run app.py
```

* User-friendly web interface
* Allows users to ask questions interactively

---

## 📈 Results & Impact

* Enables semantic search over unstructured video content
* Improves answer accuracy using context-aware retrieval
* Demonstrates real-world RAG implementation
* Scalable for documents, PDFs, meetings, lectures, and tutorials

---

## 📌 Use Cases

* Educational video Q&A
* Corporate training material search
* Meeting and lecture summarization
* Knowledge base assistants

---

## 🔮 Future Enhancements

* Streamlit-based web UI
* Support for PDFs and documents
* Metadata-based filtering
* Caching and performance optimization
* Deployment using Docker

---

## 👩‍💻 Author

**Shruti Adsul**
Aspiring Data Analyst | ML & LLM Enthusiast

---

## ⭐ Call to Action

If you found this project helpful:

* ⭐ Star the repository
* 🍴 Fork it
* 💬 Share feedback


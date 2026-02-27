# AI Document Assistant using Retrieval-Augmented Generation (RAG)

## 📌 Project Overview

The **AI Document Assistant** is an end-to-end Retrieval-Augmented Generation (RAG) application that converts video content into searchable knowledge and enables users to ask natural language questions to get accurate, context-aware answers.

This project demonstrates practical implementation of:

- Semantic Search
- Vector Databases
- Local LLM Inference
- End-to-End RAG Architecture

⚡ This version uses **LLaMA3 via Ollama** for fully offline, free LLM inference (no API key required).

This project is ATS-friendly and suitable for showcasing skills in:

- Data Science  
- Machine Learning  
- NLP  
- LLM-based Application Development  

---

## 🎯 Problem Statement

Large video and document content is difficult to search and query efficiently.  
Traditional keyword search fails to capture semantic meaning.

### ✅ Solution

Build a system that:

- Converts videos into text
- Stores semantic embeddings
- Retrieves relevant context using vector search
- Generates precise answers using an LLM (RAG architecture)

---

## 🚀 Key Features

- 🎥 Video to audio conversion  
- 🎙 Automatic speech-to-text transcription using OpenAI Whisper  
- ✂ Text chunking and semantic embeddings  
- ⚡ Fast similarity search using FAISS  
- 🤖 Context-aware answer generation using LLaMA3 (via Ollama)  
- 🧩 Modular and scalable pipeline  
- 💻 Fully offline LLM inference (No API cost)  

---

## 🧠 Architecture (RAG Pipeline)

### 1️⃣ Ingestion  
Video → Audio → Transcript  

### 2️⃣ Embedding Store  
Transcript chunking → Vector embeddings → FAISS index  

### 3️⃣ Retriever  
Semantic search → Top-k relevant chunks  

### 4️⃣ Generator  
LLaMA3 (Ollama) generates answers using retrieved context  

---

## 🛠️ Technologies Used

- Python  
- OpenAI Whisper (Speech-to-Text)  
- Sentence Transformers (`all-MiniLM-L6-v2`)  
- FAISS (Vector Database)  
- Ollama  
- LLaMA3 (Local LLM)  
- MoviePy (Video processing)  
- NumPy  
- Streamlit (Web UI)  

---

## 📂 Project Structure

import os

# Project folders
folders = [
    "videos",
    "audio",
    "transcripts",
    "embeddings"
]

# Project files (ONLY placeholders, no logic)
files = {
    "app.py": "# Streamlit UI will go here\n",
    "ingest.py": "# Phase 1: Video → Audio → Transcript\n",
    "embed_store.py": "# Phase 2: Create embeddings from transcripts\n",
    "retriever.py": "# Phase 3: Retrieve relevant chunks\n",
    "rag_pipeline.py": "# Phase 4: RAG logic (Retriever + LLM)\n",
    "README.md": "# Video-based RAG Project\n",
    "requirements.txt": """moviepy
openai-whisper
sentence-transformers
faiss-cpu
transformers
torch
numpy
streamlit
"""
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for filename, content in files.items():
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

print(" project setup completed successfully!")

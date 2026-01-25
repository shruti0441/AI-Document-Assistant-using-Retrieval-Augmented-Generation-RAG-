# Phase 2: Create embeddings from transcripts
import os
import faiss 
import numpy as np
from sentence_transformers import SentenceTransformer

# Paths
TRANSCRIPT_DIR = "transcripts"
EMBEDDING_DIR = "embeddings"

os.makedirs(EMBEDDING_DIR, exist_ok=True)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def split_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks


def load_and_chunk_transcripts():
    all_chunks = []

    for file in os.listdir(TRANSCRIPT_DIR):
        if file.endswith(".txt"):
            path = os.path.join(TRANSCRIPT_DIR, file)
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
                chunks = split_text(text)
                all_chunks.extend(chunks)

    return all_chunks


def create_faiss_index(text_chunks):
    embeddings = model.encode(text_chunks, convert_to_numpy=True)
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    return index, embeddings


if __name__ == "__main__":
    print("Loading transcripts...")
    text_chunks = load_and_chunk_transcripts()

    print(f"Total chunks created: {len(text_chunks)}")

    print("Creating embeddings and FAISS index...")
    index, embeddings = create_faiss_index(text_chunks)

    faiss.write_index(index, os.path.join(EMBEDDING_DIR, "faiss.index"))
    np.save(os.path.join(EMBEDDING_DIR, "chunks.npy"), np.array(text_chunks, dtype=object))

    print(" Embeddings and FAISS index saved successfully!")

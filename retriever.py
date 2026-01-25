#  Phase 3: Retrieve relevant chunks
import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

EMBEDDINGS_DIR = "embeddings" 

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index(os.path.join(EMBEDDINGS_DIR, "faiss.index"))

# Load chunks
chunks = np.load(os.path.join(EMBEDDINGS_DIR, "chunks.npy"), allow_pickle=True)


def retrieve(query, top_k=5):
    if index.ntotal == 0:
        return []

    query_embedding = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(query_embedding, top_k)

    results = []
    for idx in indices[0]:
        results.append(chunks[idx])

    return results



if __name__ == "__main__":
    query = input("Enter your query: ")
    results = retrieve(query)

    print("\nTop relevant chunks:\n")
    for i, text in enumerate(results, 1):
        print(f"{i}. {text}")
        print("-" * 50)


# Phase 4: RAG Pipeline (Retriever + LLM)

import os
from openai import OpenAI
from retriever import retrieve  # import your retriever function

# ---------------- CONFIG ----------------
TOP_K = 5

# OpenAI client (API key must be set in environment variable)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found. Please set it in environment variables.")
# ---------------------------------------


def generate_answer(query, retrieved_chunks):
    """
    Uses retrieved document chunks as context
    and generates an answer using the LLM
    """

    context = "\n".join(retrieved_chunks)

    prompt = f"""
You are an AI assistant.
Answer the question using ONLY the context below.
If the answer is not present in the context, say "I don't know".

Context:
{context}

Question:
{query}

Answer:
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    query = input("Enter your question: ")

    # 🔹 Step 1: Retrieve relevant chunks
    retrieved_chunks = retrieve(query, top_k=TOP_K)

    if not retrieved_chunks:
        print("No relevant context found.")
    else:
        # 🔹 Step 2: Generate answer using LLM
        answer = generate_answer(query, retrieved_chunks)

        print("\nAI Answer:\n")
        print(answer)


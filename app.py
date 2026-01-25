# Phase 05 UI Part 
import streamlit as st
import os
from retriever import retrieve
from openai import OpenAI

st.set_page_config(page_title="AI Document Assistant", layout="centered")

st.title("📄 AI Document Assistant (RAG)")
st.write("Ask questions from your documents")

query = st.text_input("Enter your question:")

def generate_answer(query, chunks):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    context = "\n".join(chunks)

    prompt = f"""
You are an AI assistant.
Answer the question using ONLY the context below.

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


if st.button("Get Answer"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Retrieving answer..."):
            chunks = retrieve(query)

            if not chunks:
                st.error("No relevant context found.")
            else:
                answer = generate_answer(query, chunks)
                st.success("Answer")
                st.write(answer)


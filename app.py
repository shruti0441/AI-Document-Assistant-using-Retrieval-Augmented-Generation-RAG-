import streamlit as st
import ollama
from retriever import retrieve

MODEL_NAME = "llama3"

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="AI Document Assistant (RAG)",
    layout="wide"
)

st.title("🤖 AI Document Assistant (RAG)")
st.write("Ask questions from your documents using FAISS + LLaMA3 (Local & Free)")

# ---------------- User Input ----------------
query = st.text_input("Enter your question:")


def generate_answer(query, retrieved_chunks):
    # Clean + limit context
    cleaned_chunks = [
        chunk.strip().replace("\n", " ")
        for chunk in retrieved_chunks
    ]

    context = "\n\n".join(cleaned_chunks)

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                "You are a knowledgeable computer science tutor.\n"
                "Answer the question using ONLY the given context.\n"
                "Do NOT copy sentences directly from the context.\n"
                "Rephrase the information in your own words.\n"
                "Give a complete, clear explanation as if teaching a student.\n"
                "Do NOT mention chunks or context.\n"
                "If the answer is not present, say exactly: I don't know."
                )
            },
            {
                "role": "user",
                "content": f"""
Context:
{context}

Question:
{query}
"""
            }
        ],
        options={
            "temperature": 0.2,
            "top_p": 0.9,
            "num_ctx": 4096
        }
    )

    return response["message"]["content"]


# ---------------- Button Logic ----------------
if st.button("Get Answer"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("🔍 Retrieving relevant context..."):
            retrieved_chunks = retrieve(query)

        if not retrieved_chunks:
            st.error("No relevant context found.")
        else:
            with st.spinner("🧠 Generating answer..."):
                answer = generate_answer(query, retrieved_chunks)

            st.subheader("🧠 Answer")
            st.markdown(f"**{answer}**")

            with st.expander("📄 Retrieved Context (For Debugging)"):
                for i, chunk in enumerate(retrieved_chunks, 1):
                    st.markdown(f"**Chunk {i}:**")
                    st.write(chunk)

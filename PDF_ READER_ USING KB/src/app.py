import sys, os
from pathlib import Path

# Fix path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

import streamlit as st
from src.extract import extract_text_from_pdf
from src.graph_builder import build_graph_from_text
from src.query_engine import query_neo4j_graph


st.set_page_config(page_title="PDF Knowledge Graph", page_icon="🧠")

st.title("🧠 Local Knowledge Graph (Neo4j + Gemini 2.5 Flash)")

menu = st.sidebar.radio("Menu", ["Upload PDF", "Ask Question"])

if menu == "Upload PDF":
    st.subheader("📄 Upload one PDF")
    file = st.file_uploader("Choose a PDF", type=["pdf"])
    if file:
        os.makedirs("uploads", exist_ok=True)
        file_path = f"uploads/{file.name.replace(' ', '_')}"
        with open(file_path, "wb") as f:
            f.write(file.read())
        st.info("Extracting text...")
        text = extract_text_from_pdf(file_path)
        st.info("Building Knowledge Graph...")
        build_graph_from_text(text)
        st.success("✅ Graph built successfully for this PDF!")

elif menu == "Ask Question":
    st.subheader("💬 Ask a question based on the uploaded PDF")
    q = st.text_input("Enter your question:")
    if st.button("Ask"):
        if q.strip():
            answer = query_neo4j_graph(q)
            st.write("### 🤖 Answer:")
            st.info(answer)
        else:
            st.warning("Please enter a question first.")

import os
from google import generativeai as genai
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))
)

def query_neo4j_graph(question: str) -> str:
    with driver.session() as session:
        result = session.run("""
        MATCH (a)-[r]->(b)
        RETURN a.name AS source, type(r) AS relation, b.name AS target
        """)
        triples = [f"{r['source']} -[{r['relation']}]-> {r['target']}" for r in result]

    context = "\n".join(triples)
    if not context:
        return "⚠️ The graph is empty. Please upload a PDF first."

    model = genai.GenerativeModel("models/gemini-2.5-flash")
    prompt = f"""
    You are an AI assistant. Use this graph knowledge to answer questions.

    Graph facts:
    {context}

    Question: {question}
    Answer clearly and concisely.
    """
    response = model.generate_content(prompt)
    return response.text if response else "⚠️ No response from model."

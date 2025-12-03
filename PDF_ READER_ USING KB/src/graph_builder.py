import os
from google import generativeai as genai
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini + Neo4j
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))
)

def build_graph_from_text(text: str):
    """Extract knowledge triples using Gemini and push to Neo4j."""
    if not text:
        print("⚠️ No text extracted from PDF.")
        return

    model = genai.GenerativeModel("models/gemini-2.5-flash")
    prompt = f"""
    Extract key concepts and their relationships as triples (Subject, Relation, Object)
    from the text below. Return them in simple plain text format, one triple per line.

    Example:
    Urbanization - leads_to -> Industrialization

    Text:
    {text[:4000]}  # (limit context for performance)
    """

    response = model.generate_content(prompt)

    triples = []
    if response and response.text:
        for line in response.text.splitlines():
            if "-" in line and "->" in line:
                triples.append(line.strip())

    print(f"📊 Extracted {len(triples)} triples from text")

    if not triples:
        return

    # Clear old data
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")

    # Store triples
    with driver.session() as session:
        for triple in triples:
            try:
                parts = triple.split("->")
                if len(parts) == 2:
                    left, right = parts
                    s, p = left.split("-", 1)
                    session.run("""
                        MERGE (a:Concept {name:$s})
                        MERGE (b:Concept {name:$r})
                        MERGE (a)-[:RELATION {type:$p}]->(b)
                    """, {"s": s.strip(), "p": p.strip(), "r": right.strip()})
            except:
                pass

    print("✅ Graph built successfully in Neo4j!")

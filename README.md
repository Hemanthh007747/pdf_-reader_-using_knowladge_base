# PDF Reader Using Knowledge Base

A Python-based intelligent PDF document reader that leverages Retrieval-Augmented Generation (RAG) to create a searchable knowledge base from PDF files [web:7][web:10].

## Overview

This project enables users to extract, store, and query information from PDF documents using vector embeddings and natural language processing. The system converts PDF content into a searchable knowledge base, allowing for semantic search and question-answering capabilities without requiring model fine-tuning [web:3][web:8].

## Features

- **PDF Processing**: Extract text and content from multiple PDF files
- **Vector Embeddings**: Convert document chunks into vector embeddings for semantic search [web:9]
- **Knowledge Base Storage**: Store vectorized documents in a vector database (e.g., PgVector, Pinecone, FAISS)
- **Question Answering**: Query documents using natural language questions [web:10]
- **RAG Pipeline**: Retrieval-Augmented Generation for accurate, context-aware responses [web:7]
- **Jupyter Integration**: Interactive notebook interface using JupyterChart/AnyWidget [file:1]

## Installation

Clone the repository
git clone https://github.com/Hemanthh007747/pdf_-reader_-using_knowladge_base.git
cd pdf_-reader_-using_knowladge_base

Install required dependencies
pip install -r requirements.txt

Install additional PDF processing libraries
pip install pypdf langchain openai tiktoken chromadb

text

## Requirements

- Python 3.8+
- pypdf or PyPDF2
- LangChain
- OpenAI API key or local LLM (e.g., Llama)
- Vector database (PgVector, Pinecone, or FAISS)
- Jupyter Notebook/Lab

## Quick Start

from phi.knowledge.pdf import PDFKnowledgeBase, PDFReader
from phi.vectordb.pgvector import PgVector

Initialize knowledge base
pdf_kb = PDFKnowledgeBase(
path="data/pdfs",
vector_db=PgVector(
table_name="pdf_documents",
db_url="your_database_url"
),
reader=PDFReader(chunk=True)
)

Add documents
pdf_kb.load()

Query the knowledge base
response = pdf_kb.search("What is the main topic?")

text

## Project Structure

pdf_-reader_-using_knowladge_base/
├── data/
│ └── pdfs/ # Store your PDF files here
├── notebooks/ # Jupyter notebooks for experimentation
├── src/
│ ├── pdf_processor.py # PDF extraction logic
│ ├── embeddings.py # Vector embedding generation
│ ├── knowledge_base.py # KB management
│ └── query_engine.py # RAG query processing
├── tests/ # Unit tests
├── requirements.txt # Python dependencies
└── README.md

text

## Usage

### 1. Data Ingestion

Process PDF documents
from src.pdf_processor import PDFProcessor

processor = PDFProcessor()
processor.load_documents("data/pdfs")
processor.chunk_documents(chunk_size=512, overlap=50)

text

### 2. Create Embeddings

Generate vector embeddings
from src.embeddings import create_embeddings

embeddings = create_embeddings(
documents=processor.chunks,
model="text-embedding-ada-002"
)

text

### 3. Query Documents

Ask questions
from src.query_engine import QueryEngine

engine = QueryEngine(knowledge_base=pdf_kb)
answer = engine.query("Summarize the key findings")
print(answer)

text

## Configuration

Create a `.env` file with your API keys:

OPENAI_API_KEY=your_openai_key
VECTOR_DB_URL=postgresql://user:pass@localhost/vectordb
CHUNK_SIZE=512
CHUNK_OVERLAP=50

text

## Technologies Used

- **PDF Processing**: pypdf, PyPDF2 [web:3]
- **LLM Framework**: LangChain [web:8]
- **Embeddings**: OpenAI Embeddings or HuggingFace models [web:9]
- **Vector Database**: PgVector, Pinecone, or FAISS [web:10]
- **UI**: Jupyter Notebook with AnyWidget [file:1]

## RAG Architecture

1. **Document Loading**: PDF files are loaded and split into chunks [web:8]
2. **Vectorization**: Text chunks are converted to embeddings
3. **Storage**: Embeddings stored in vector database
4. **Retrieval**: Similar chunks retrieved based on query
5. **Generation**: LLM generates answer using retrieved context [web:7]

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

[Specify your license]

## Contact

- GitHub: [@Hemanthh007747](https://github.com/Hemanthh007747)

## Acknowledgments

- Built with [Phidata](https://docs.phidata.com/) framework [web:3][web:9]
- Inspired by RAG implementations for document QA [web:7][web:10]
- Uses AnyWidget for Jupyter integration [file:1]

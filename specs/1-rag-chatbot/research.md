# Research: RAG Chatbot for Physical AI Humanoid Robotics Textbook

## Research Summary

This research addresses the implementation of a Retrieval-Augmented Generation (RAG) chatbot system for the Physical AI & Humanoid Robotics textbook. The system will leverage Cohere embeddings, Qdrant vector database, and Gemini 1.5 Flash via OpenAI proxy.

## Decision: Use Python with agents library for RAG implementation

**Rationale**: The user specifically requested to use the agents library with Gemini 1.5 Flash via OpenAI proxy, which aligns with the requirement to use free tools and provides a structured approach for building the RAG chatbot.

**Alternatives considered**: 
- Using LangChain which is more common for RAG systems
- Using native OpenAI library directly
- Implementing a custom solution from scratch

## Decision: Three-file architecture implementation

**Rationale**: The user specifically requested a three-file system: main.py for ingestion, retrieve.py for testing, and agent.py for the live chatbot. This separation allows for clear division of responsibilities and easier testing.

**Alternatives considered**: 
- Single monolithic file
- More complex multi-file architecture with separate modules
- Microservices architecture

## Decision: Cohere embed-english-v3.0 for embeddings

**Rationale**: This is specifically required by the user (free tier) and provides 1024-dimensional embeddings that match the requirements. The model is well-documented and suitable for educational content.

**Alternatives considered**: 
- Sentence Transformers models (local but potentially less accurate)
- OpenAI embeddings (not free tier)
- Other embedding providers

## Decision: Qdrant Cloud free cluster for vector storage

**Rationale**: The user specified this free option which supports the required 1024-dimensional embeddings and COSINE distance. It's a robust vector database solution that integrates well with Python.

**Alternatives considered**: 
- Pinecone (not free tier for our usage)
- Weaviate (alternative, but user specified Qdrant)
- ChromaDB (local option, but user specified Qdrant Cloud)

## Decision: Chunk size of ~1200 characters

**Rationale**: This size balances information density with retrieval accuracy. It's large enough to contain meaningful context but small enough to maintain semantic coherence for embedding.

**Alternatives considered**: 
- Smaller chunks (lose context)
- Larger chunks (reduce retrieval precision)
- Sentence-based chunks (potential for very short chunks)

## Decision: Ingestion from sitemap.xml

**Rationale**: This is the standard approach for indexing website content and ensures all textbook pages are captured systematically.

**Alternatives considered**: 
- Manual page-by-page ingestion
- PDF parsing (if textbook existed as PDF)
- API-based extraction (if available)

## Decision: Trafilatura for text extraction

**Rationale**: Trafilatura is a specialized library for extracting text content from web pages, filtering out HTML, navigation, and ads to get the core content.

**Alternatives considered**: 
- BeautifulSoup with manual extraction
- Newspaper3k (alternative web text extraction)
- Selenium for dynamic content (overkill for static textbook)

## Decision: Gemini 1.5 Flash via OpenAI-compatible proxy

**Rationale**: The user specified this model via proxy, which provides a cost-effective solution with good performance for educational Q&A. Flash is optimized for speed.

**Alternatives considered**: 
- Gemini Pro (more expensive)
- OpenAI GPT models (not free tier as specified)
- Open source models (require local hosting, not specified in requirements)

## Decision: Environment variable management with python-dotenv

**Rationale**: This is the standard approach for managing secrets and configuration in Python applications without exposing them in code.

**Alternatives considered**: 
- Hardcoded values (security risk)
- Command-line arguments (inconvenient and visible in process lists)
- Configuration files (risk of committing to version control)

## Decision: uv for package management

**Rationale**: The user specifically requested using uv, which is a modern, fast Python package manager that is compatible with pip and virtual environments.

**Alternatives considered**: 
- pip + venv (standard but slower)
- Poetry (alternative package manager)
- Conda (different ecosystem)
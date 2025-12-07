# RAG Chatbot for Physical AI & Humanoid Robotics Textbook

This project implements a Retrieval-Augmented Generation (RAG) chatbot for the Physical AI & Humanoid Robotics textbook using Cohere embeddings, Qdrant vector database, and Gemini 1.5 Flash via OpenAI-compatible proxy.

## Prerequisites

Before starting, ensure you have:

1. **Cohere API key**: Already created account and obtained API key
2. **Qdrant Cloud**: Already created free cluster and copied URL + API key
3. **Gemini API key**: Already obtained from Google AI Studio

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Copy Environment Variables
```bash
cp backend/.env.example backend/.env
```

### 3. Edit .env File
Open `backend/.env` and paste your API keys:
```env
COHERE_API_KEY=your_cohere_api_key_here
QDRANT_URL=your_qdrant_cluster_url_here
QDRANT_API_KEY=your_qdrant_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Set Up Virtual Environment
```bash
cd backend
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 5. Install Dependencies
```bash
uv pip install agents cohere qdrant-client trafilatura python-dotenv requests
```

## Usage

### 1. Ingest Textbook Content
Run the ingestion pipeline to process the textbook content and store it in Qdrant:

```bash
uv run main.py
```

When prompted, enter the URL to your textbook's sitemap.xml file. The system will:
- Extract all URLs from the sitemap
- Download and clean text content using trafilatura
- Chunk text into ~1200 character segments
- Generate embeddings with Cohere embed-english-v3.0
- Store embeddings in Qdrant collection "humanoid_ai_book"

### 2. Test Retrieval (Optional)
Test the retrieval functionality to ensure content is properly indexed:

```bash
uv run retrieve.py
```

Enter a query to see the top 5 retrieved chunks from the textbook.

### 3. Start the Chatbot Agent
Run the RAG chatbot to interact with the textbook content:

```bash
uv run agent.py
```

The agent will prompt you for questions. Try asking "what is physical ai?" to see the tool calling in action.

## Architecture

This project follows a 3-file architecture:

1. **main.py**: One-time ingestion pipeline (sitemap.xml → trafilatura → ~1200 char chunks → Cohere embed → Qdrant upsert)
2. **retrieve.py**: Standalone retrieval test script that embeds a query and prints top 5 retrieved chunks from Qdrant
3. **agent.py**: Complete working RAG agent using the 'agents' library with Gemini 1.5 Flash via OpenAI-compatible proxy, @function_tool retrieve, verbose stdout logging, and the exact system prompt: "You are an AI tutor for the Physical AI & Humanoid Robotics textbook. First call retrieve tool. ONLY use retrieved content. If not found → I don't know."

## Troubleshooting

- If ingestion fails, verify your sitemap.xml URL is accessible and properly formatted
- If retrieval returns no results, ensure the ingestion process completed successfully
- If the agent doesn't respond, check that all API keys are valid and properly formatted in your .env file
- If you see tool calling errors, ensure all dependencies are properly installed
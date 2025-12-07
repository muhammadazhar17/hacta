# Quickstart Guide: RAG Chatbot for Physical AI Humanoid Robotics Textbook

## Setup Instructions

### Prerequisites
- Python 3.13 or higher
- uv package manager
- API keys for Cohere, Qdrant Cloud, and Gemini (via OpenAI-compatible proxy)

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Setup Virtual Environment with uv
```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
# Install dependencies using uv
uv pip install -r requirements.txt
# Or if using pyproject.toml
uv pip install -e .
```

### 4. Environment Configuration
1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit the `.env` file with your API keys and endpoints:
```env
COHERE_API_KEY=your_cohere_api_key_here
QDRANT_URL=your_qdrant_cluster_url_here
QDRANT_API_KEY=your_qdrant_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
QDRANT_COLLECTION_NAME=humanoid_ai_book
```

## Running the System

### 1. Ingest Textbook Content (One-time setup)
```bash
python src/main.py
```
This will:
- Extract URLs from sitemap.xml
- Download and clean text content using trafilatura
- Chunk text into ~1200 character segments
- Embed each chunk using Cohere embed-english-v3.0
- Store embeddings in Qdrant with collection name "humanoid_ai_book"

### 2. Test Retrieval
```bash
python src/retrieve.py
```
This will:
- Test embedding a query using Cohere
- Search Qdrant for relevant content
- Print retrieved chunks to verify the system

### 3. Run the Live Chatbot Agent
```bash
python src/agent.py
```
This will:
- Initialize the agent with the agents library
- Use Gemini 1.5 Flash via OpenAI proxy
- Allow real-time querying of the textbook content
- Show verbose logging of tool calls

## File Structure
```
backend/
├── src/
│   ├── main.py          # Ingestion pipeline
│   ├── retrieve.py      # Standalone retrieval test
│   └── agent.py         # Live RAG chatbot agent
├── pyproject.toml
├── .env                 # Environment variables (gitignored)
├── .env.example         # Example environment variables
└── README.md
```

## Troubleshooting

### Common Issues:

1. **API Keys**: Ensure all API keys in `.env` are correct and have proper permissions
2. **Qdrant Connection**: Verify your Qdrant URL and API key are correct
3. **Embedding Dimensions**: Confirm Cohere is configured to return 1024-dimensional embeddings
4. **Chunk Size**: Verify text is being chunked to approximately 1200 characters

### Verification Steps:

1. Check if content is properly ingested: `python src/retrieve.py` with a known query from the textbook
2. Verify Qdrant collection exists and has the correct vector dimensions
3. Test the agent with the query "what is physical ai?" to see if it retrieves and responds correctly
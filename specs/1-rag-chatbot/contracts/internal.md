# API Contracts: RAG Chatbot for Physical AI Humanoid Robotics Textbook

## Internal Service Contracts

### Ingestion Service (main.py)

#### Function: `extract_urls_from_sitemap(sitemap_url)`
- **Purpose**: Extract all URLs from the textbook's sitemap.xml
- **Input**: `sitemap_url` (string) - URL to the sitemap.xml file
- **Output**: List of URLs (list of strings)
- **Errors**: Raises exception if sitemap is inaccessible

#### Function: `download_and_clean_text(url)`
- **Purpose**: Download content from a URL and extract clean text
- **Input**: `url` (string) - URL to download content from
- **Output**: Clean text content (string)
- **Errors**: Raises exception if URL is inaccessible or text extraction fails

#### Function: `chunk_text(text, chunk_size=1200)`
- **Purpose**: Split text into chunks of approximately specified size
- **Input**: 
  - `text` (string) - Text to chunk
  - `chunk_size` (int) - Target size for chunks (default 1200)
- **Output**: List of text chunks (list of strings)
- **Errors**: None

#### Function: `embed_chunks(chunks)`
- **Purpose**: Generate embeddings for text chunks using Cohere
- **Input**: `chunks` (list of strings) - Text chunks to embed
- **Output**: List of embeddings (list of lists containing 1024 floats each)
- **Errors**: Raises exception if Cohere API call fails

#### Function: `store_in_qdrant(embeddings, chunks, urls)`
- **Purpose**: Store embeddings with associated text and URLs in Qdrant
- **Input**: 
  - `embeddings` (list of lists) - 1024-dimensional embeddings
  - `chunks` (list of strings) - Original text chunks
  - `urls` (list of strings) - Source URLs
- **Output**: Success status (boolean)
- **Errors**: Raises exception if Qdrant storage fails

### Retrieval Service (retrieve.py)

#### Function: `search_qdrant(query_text, top_k=5)`
- **Purpose**: Search Qdrant for relevant content based on query
- **Input**: 
  - `query_text` (string) - Natural language query
  - `top_k` (int) - Number of results to return (default 5)
- **Output**: List of relevant chunks with metadata (list of objects)
- **Errors**: Raises exception if Qdrant search fails

### Agent Service (agent.py)

#### Function: `retrieve_tool(query)`
- **Purpose**: Retrieve relevant content from the textbook based on query
- **Input**: `query` (string) - Natural language query
- **Output**: List of text chunks (list of strings)
- **Errors**: Returns empty list if no relevant content found

#### Function: `chat_agent(query)`
- **Purpose**: Process user query through RAG agent
- **Input**: `query` (string) - Natural language query from user
- **Output**: Generated response (string)
- **Errors**: Returns "I don't know" if no relevant content found
# Feature Specification: RAG Chatbot for Physical AI Humanoid Robotics Textbook

**Feature Branch**: `1-rag-chatbot-humanoid-ai`
**Created**: 2025-12-07
**Status**: Draft
**Input**: User description: "Specify a complete RAG chatbot system exactly matching the YouTube video workflow + the final working code shared by the user. The chatbot must be embedded in the Physical AI Humanoid Robotics textbook website. Use only free tools: Cohere embed-english-v3.0 (free tier), Qdrant Cloud free cluster, and Gemini 1.5 Flash via OpenAI-compatible proxy using the "agents" library (not OpenAI directly). The system has 3 files: 1. main.py → full ingestion pipeline (sitemap.xml → trafilatura → chunk → Cohere embed → Qdrant upsert) 2. retrieve.py → standalone retrieval test 3. agent.py → real agent using \`from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI\` with Gemini proxy, @function_tool retrieve, verbose logging, exact system prompt from video. Required specs: - Collection name: "humanoid_ai_book" - Embedding dimension: 1024 - Chunk size: ~1200 chars - Distance: COSINE - Always use input_type="search_query" in Cohere for queries - Agent must ALWAYS call retrieve tool first and only answer from retrieved content - Use uv + venv, python-dotenv for keys - Assume Cohere account created and API key ready, Qdrant free cluster created with URL + API key ready, Gemini API key ready - In final code, show placeholders exactly like "key-here", "url-here", "your-api_key" — user will paste real keys after generation"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Student Query Resolution (Priority: P1)

A student studying humanoid robotics wants to find specific information from the textbook that they can't remember exactly. The student accesses the embedded chatbot interface, types a query about humanoid walking gait algorithms, receives a well-formatted response based on textbook content, and continues studying.

**Why this priority**: This is the primary use case that provides immediate value to the core user group (students).

**Independent Test**: Can be fully tested by entering natural language queries about textbook content and verifying that the response is accurate, relevant, and sourced from the textbook.

**Acceptance Scenarios**:

1. **Given** student is on the textbook website, **When** student enters a specific question about humanoid robotics concepts, **Then** the chatbot returns an accurate, contextual response from the textbook content
2. **Given** student enters a query with ambiguous terms, **When** the system processes the query, **Then** the system returns the most relevant textbook content or asks for clarification

---

### User Story 2 - Researcher Information Cross-Reference (Priority: P2)

A researcher wants to cross-reference concepts from the textbook with their current work. The researcher accesses the chatbot from their institution, asks a complex question comparing two methodologies in the book, and receives a comparative response that they can validate and use in their work.

**Why this priority**: This addresses an important secondary user group (researchers) with higher-level information needs.

**Independent Test**: Can be fully tested by entering complex, comparative questions and verifying that the system synthesizes relevant information accurately.

**Acceptance Scenarios**:

1. **Given** researcher asks a complex comparative question, **When** the system processes the query, **Then** the system retrieves and presents relevant comparative information from the textbook
2. **Given** researcher asks a technical question requiring detailed explanation, **When** the system retrieves relevant content, **Then** the response is comprehensive and properly formatted

---

### User Story 3 - Instructor Resource Retrieval (Priority: P3)

An instructor is preparing a lecture and wants to pull specific examples from the textbook. The instructor accesses the chatbot through the website, asks about specific examples related to humanoid control systems, and receives relevant examples that can be used for lecture preparation.

**Why this priority**: This serves another important user group (instructors) with specific professional needs.

**Independent Test**: Can be fully tested by asking for specific examples and verifying that the system returns relevant, properly cited examples from the textbook.

**Acceptance Scenarios**:

1. **Given** instructor asks for specific examples related to a topic, **When** the system processes the request, **Then** the system returns relevant examples from the textbook content
2. **Given** instructor asks for content in a specific format, **When** the system generates a response, **Then** the response is appropriately formatted for educational use

---

### Edge Cases

- What happens when the query contains no relevant matches in the textbook content?
- How does the system handle multiple simultaneous queries during high-traffic periods?
- What occurs when the Qdrant vector database is temporarily unavailable?
- How does the system respond to queries completely unrelated to the textbook content?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST ingest content from the textbook's sitemap.xml
- **FR-002**: System MUST extract text content from web pages using trafilatura
- **FR-003**: System MUST chunk the extracted text into approximately 1200-character segments
- **FR-004**: System MUST generate embeddings for each chunk using Cohere embed-english-v3.0 with input_type="search_query" for queries
- **FR-005**: System MUST store embeddings in Qdrant vector database with collection name "humanoid_ai_book"
- **FR-006**: System MUST use 1024-dimensional embeddings with COSINE distance
- **FR-007**: System MUST accept user queries through a chat interface
- **FR-008**: System MUST perform vector similarity search in Qdrant to find relevant content
- **FR-009**: System MUST retrieve relevant text segments before generating any response
- **FR-010**: System MUST use Gemini 1.5 Flash model via OpenAI-compatible proxy for response generation
- **FR-011**: System MUST use the agents library with specific classes (Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI)
- **FR-012**: System MUST generate responses based solely on retrieved content
- **FR-013**: System MUST include verbose logging for debugging and monitoring
- **FR-014**: System MUST be packaged with uv for dependency management
- **FR-015**: System MUST securely store API keys using python-dotenv

### Key Entities

- **Textbook Content**: The source material from the Physical AI Humanoid Robotics textbook that forms the knowledge base
- **Vector Embeddings**: Numerical representations of text segments stored in Qdrant database for similarity search
- **User Query**: Input from users in natural language seeking specific information from the textbook
- **Retrieved Context**: Relevant text segments retrieved from the vector database based on query similarity
- **Generated Response**: Final output provided to the user based exclusively on retrieved context
- **System Logs**: Record of system operations, queries, and responses for monitoring and debugging

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Students can find relevant textbook information through natural language queries with 80% success rate
- **SC-002**: The system provides accurate responses with hallucination rate less than 5%
- **SC-003**: User satisfaction score averages above 4 out of 5 for responses
- **SC-004**: Query response time is under 5 seconds for 95% of requests
- **SC-005**: The system handles at least 10 concurrent user queries without performance degradation
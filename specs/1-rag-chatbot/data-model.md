# Data Model: RAG Chatbot for Physical AI Humanoid Robotics Textbook

## Entities

### Textbook Content Chunk
- **Fields**:
  - `chunk_id` (string): Unique identifier for the content chunk
  - `text` (string): The actual text content of the chunk (~1200 characters)
  - `url` (string): The URL from which the content was extracted
  - `embedding` (list[float]): 1024-dimensional vector representation of the text
  - `created_at` (datetime): Timestamp of when the chunk was created
  - `metadata` (object): Additional metadata about the content source

- **Validation**:
  - `chunk_id` is required and unique
  - `text` is required and has length between 100 and 1500 characters
  - `url` is a valid URL format
  - `embedding` is a 1024-dimensional float vector
  - `created_at` is a valid timestamp

- **State transitions**: N/A (immutable once created)

### User Query
- **Fields**:
  - `query_id` (string): Unique identifier for the query
  - `text` (string): The natural language query from the user
  - `timestamp` (datetime): When the query was submitted
  - `user_id` (string): Identifier for the user making the query (optional)

- **Validation**:
  - `query_id` is required and unique
  - `text` is required and between 5 and 500 characters
  - `timestamp` is a valid timestamp
  - `user_id` follows the required format if present

- **State transitions**: N/A (immutable once created)

### Retrieved Context
- **Fields**:
  - `retrieval_id` (string): Unique identifier for the retrieval operation
  - `query_id` (string): Reference to the original query
  - `chunks` (list[object]): List of relevant text chunks retrieved
  - `relevance_scores` (list[float]): Scores representing how relevant each chunk is
  - `timestamp` (datetime): When the retrieval was performed

- **Validation**:
  - `retrieval_id` is required and unique
  - `query_id` references a valid query
  - `chunks` array contains at least one entry
  - `relevance_scores` matches length of chunks array
  - `timestamp` is a valid timestamp

- **State transitions**: N/A (immutable once created)

### Generated Response
- **Fields**:
  - `response_id` (string): Unique identifier for the response
  - `query_id` (string): Reference to the original query
  - `retrieval_id` (string): Reference to the retrieval operation used
  - `text` (string): The generated response text
  - `timestamp` (datetime): When the response was generated
  - `source_chunks` (list[string]): IDs of chunks that informed the response

- **Validation**:
  - `response_id` is required and unique
  - `query_id` references a valid query
  - `retrieval_id` references a valid retrieval operation
  - `text` is required and between 10 and 2000 characters
  - `timestamp` is a valid timestamp
  - `source_chunks` contains valid chunk IDs

- **State transitions**: N/A (immutable once created)

## Relationships

- One `User Query` generates one `Generated Response`
- One `User Query` triggers one `Retrieved Context` operation
- One `Retrieved Context` operation can return multiple `Textbook Content Chunk` objects
- One `Generated Response` references multiple `Textbook Content Chunk` objects via `source_chunks`
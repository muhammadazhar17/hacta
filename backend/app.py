import cohere
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance, PointStruct

# -------------------------------
# Initialize Cohere client
# -------------------------------
cohere_client = cohere.Client("z6KTrRHFsu9lAs9gMO7emo5uWsJMRashq3flBGe6")

# -------------------------------
# Connect to Qdrant
# -------------------------------
qdrant = QdrantClient(
    url="https://d54c832e-1701-4554-a71f-fd62178d4468.europe-west3-0.gcp.cloud.qdrant.io",
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.QLG2zy6BxwWzcwTXgHZ3JXoCK76LllXlf0ttzNv3710"
)

def get_embedding(text):
    """Get embedding vector from Cohere Embed v3"""
    response = cohere_client.embed(
        model="embed-english-v3.0",
        input_type="search_query",  # Use search_query for queries
        texts=[text],
    )
    return response.embeddings[0]  # Return the first embedding

def retrieve(query):
    embedding = get_embedding(query)
    result = qdrant.query_points( 
        collection_name="humanoid_ai_book",
        query=embedding,
        limit=5
    )
    return [point.payload["text"] for point in result.points]

# Test
print(retrieve("What data do you have?"))

# import cohere
# from qdrant_client import QdrantClient
# import os

# # Initialize Cohere client
# cohere_client = cohere.Client("fpqhzQ1NxQwDhuECAwMwalApsRvBHekqT6Hbpr7t")

# # Connect to Qdrant
# qdrant = QdrantClient(
#     url="https://d54c832e-1701-4554-a71f-fd62178d4468.europe-west3-0.gcp.cloud.qdrant.io", 
#     api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.QLG2zy6BxwWzcwTXgHZ3JXoCK76LllXlf0ttzNv3710"
# )


# def get_embedding(text):
#     """Get embedding vector from Cohere Embed v3"""
#     response = cohere_client.embed(
#         model="embed-english-v3.0",
#         input_type="search_query",  # Use search_query for queries
#         texts=[text],
#     )
#     return response.embeddings[0]  # Return the first embedding

# def retrieve(query):
#     embedding = get_embedding(query)
#     result = qdrant.query_points(
#         collection_name="humanoid_ai_book_two",
#         query=embedding,
#         limit=5
#     )
#     return [point.payload["text"] for point in result.points]

# # Test
# print(retrieve("What data do you have?"))
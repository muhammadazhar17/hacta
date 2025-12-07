import requests
import xml.etree.ElementTree as ET
import trafilatura
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
import cohere

# -------------------------------------
# CONFIG
# -------------------------------------
SITEMAP_URL = "https://physicalhumanoidaitextbook.vercel.app/sitemap.xml"
COLLECTION_NAME = "humanoid_ai_book"

# Cohere
cohere_client = cohere.Client("z6KTrRHFsu9lAs9gMO7emo5uWsJMRashq3flBGe6")
EMBED_MODEL = "embed-english-v3.0"

# Qdrant
qdrant = QdrantClient(
    url="https://d54c832e-1701-4554-a71f-fd62178d4468.europe-west3-0.gcp.cloud.qdrant.io",
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.QLG2zy6BxwWzcwTXgHZ3JXoCK76LllXlf0ttzNv3710"
)

# -------------------------------------
# FUNCTIONS
# -------------------------------------
def get_all_urls(sitemap_url):
    try:
        xml = requests.get(sitemap_url, timeout=10).text
        root = ET.fromstring(xml)
    except Exception as e:
        print("[ERROR] Failed to fetch sitemap:", e)
        return []

    urls = []
    for child in root:
        loc_tag = child.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
        if loc_tag is not None:
            urls.append(loc_tag.text)

    print("\nFOUND URLS:")
    for u in urls:
        print(" -", u)
    return urls

def extract_text_from_url(url):
    try:
        html = requests.get(url, timeout=10).text
        text = trafilatura.extract(html)
        if not text:
            print("[WARNING] No text extracted from:", url)
        return text
    except Exception as e:
        print("[ERROR] Failed to fetch URL:", url, e)
        return None

def chunk_text(text, max_chars=1200):
    chunks = []
    while len(text) > max_chars:
        split_pos = text[:max_chars].rfind(". ")
        if split_pos == -1:
            split_pos = max_chars
        chunks.append(text[:split_pos].strip())
        text = text[split_pos:].strip()
    if text:
        chunks.append(text)
    return chunks

def embed(text):
    response = cohere_client.embed(
        model=EMBED_MODEL,
        input_type="search_query",
        texts=[text],
    )
    return response.embeddings[0]

def get_embedding_dimension():
    # Get dimension from a test embedding
    test_vector = embed("Hello world")
    return len(test_vector)

def create_collection():
    vector_dim = get_embedding_dimension()
    print(f"\nCreating Qdrant collection '{COLLECTION_NAME}' with vector dimension {vector_dim}...")
    
    # Delete old collection if exists
    if qdrant.collection_exists(COLLECTION_NAME):
        qdrant.delete_collection(COLLECTION_NAME)
    
    qdrant.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=vector_dim, distance=Distance.COSINE)
    )
    print("Collection created successfully.")

def save_chunk_to_qdrant(chunk, chunk_id, url):
    vector = embed(chunk)
    qdrant.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            PointStruct(
                id=chunk_id,
                vector=vector,
                payload={"url": url, "text": chunk, "chunk_id": chunk_id}
            )
        ]
    )

# -------------------------------------
# MAIN
# -------------------------------------
def ingest_book():
    urls = get_all_urls(SITEMAP_URL)
    if not urls:
        print("No URLs to process. Exiting.")
        return

    create_collection()
    global_id = 1

    for url in urls:
        print("\nProcessing:", url)
        text = extract_text_from_url(url)
        if not text:
            continue

        chunks = chunk_text(text)
        for ch in chunks:
            save_chunk_to_qdrant(ch, global_id, url)
            print(f"Saved chunk {global_id}")
            global_id += 1

    print("\n✔️ Ingestion completed!")
    print("Total chunks stored:", global_id - 1)

if __name__ == "__main__":
    ingest_book()



# import requests
# import xml.etree.ElementTree as ET
# import trafilatura
# from qdrant_client import QdrantClient
# from qdrant_client.models import VectorParams, Distance, PointStruct
# import cohere
# import os

# # -------------------------------------
# # CONFIG
# # -------------------------------------
# # Your Deployment Link:
# SITEMAP_URL = "https://pre-hackathon-text-book-as.vercel.app/sitemap.xml"
# COLLECTION_NAME = "humanoid_ai_book"

# cohere_client = cohere.Client("fpqhzQ1NxQwDhuECAwMwalApsRvBHekqT6Hbpr7t")
# EMBED_MODEL = "embed-english-v3.0"

# # Connect to Qdrant Cloud
# qdrant = QdrantClient(
#     url="https://d54c832e-1701-4554-a71f-fd62178d4468.europe-west3-0.gcp.cloud.qdrant.io",
#     api_key= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.QLG2zy6BxwWzcwTXgHZ3JXoCK76LllXlf0ttzNv3710")

# # -------------------------------------
# # Step 1 — Extract URLs from sitemap
# # -------------------------------------
# def get_all_urls(sitemap_url):
#     xml = requests.get(sitemap_url).text
#     root = ET.fromstring(xml)

#     urls = []
#     for child in root:
#         loc_tag = child.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
#         if loc_tag is not None:
#             urls.append(loc_tag.text)

#     print("\nFOUND URLS:")
#     for u in urls:
#         print(" -", u)

#     return urls


# # -------------------------------------
# # Step 2 — Download page + extract text
# # -------------------------------------
# def extract_text_from_url(url):
#     html = requests.get(url).text
#     text = trafilatura.extract(html)

#     if not text:
#         print("[WARNING] No text extracted from:", url)

#     return text


# # -------------------------------------
# # Step 3 — Chunk the text
# # -------------------------------------
# def chunk_text(text, max_chars=1200):
#     chunks = []
#     while len(text) > max_chars:
#         split_pos = text[:max_chars].rfind(". ")
#         if split_pos == -1:
#             split_pos = max_chars
#         chunks.append(text[:split_pos])
#         text = text[split_pos:]
#     chunks.append(text)
#     return chunks


# # -------------------------------------
# # Step 4 — Create embedding
# # -------------------------------------
# def embed(text):
#     response = cohere_client.embed(
#         model=EMBED_MODEL,
#         input_type="search_query",  # Use search_query for queries
#         texts=[text],
#     )
#     return response.embeddings[0]  # Return the first embedding


# # -------------------------------------
# # Step 5 — Store in Qdrant
# # -------------------------------------
# def create_collection():
#     print("\nCreating Qdrant collection...")
#     qdrant.recreate_collection(
#         collection_name=COLLECTION_NAME,
#         vectors_config=VectorParams(
#         size=1024,        # Cohere embed-english-v3.0 dimension
#         distance=Distance.COSINE
#         )
#     )

# def save_chunk_to_qdrant(chunk, chunk_id, url):
#     vector = embed(chunk)

#     qdrant.upsert(
#         collection_name=COLLECTION_NAME,
#         points=[
#             PointStruct(
#                 id=chunk_id,
#                 vector=vector,
#                 payload={
#                     "url": url,
#                     "text": chunk,
#                     "chunk_id": chunk_id
#                 }
#             )
#         ]
#     )


# # -------------------------------------
# # MAIN INGESTION PIPELINE
# # -------------------------------------
# def ingest_book():
#     urls = get_all_urls(SITEMAP_URL)

#     create_collection()

#     global_id = 1

#     for url in urls:
#         print("\nProcessing:", url)
#         text = extract_text_from_url(url)

#         if not text:
#             continue

#         chunks = chunk_text(text)

#         for ch in chunks:
#             save_chunk_to_qdrant(ch, global_id, url)
#             print(f"Saved chunk {global_id}")
#             global_id += 1

#     print("\n✔️ Ingestion completed!")
#     print("Total chunks stored:", global_id - 1)


# if __name__ == "__main__":
#     ingest_book()
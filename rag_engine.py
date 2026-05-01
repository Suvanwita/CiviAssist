import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer
import requests

# Load everything once
model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index("faiss_index.bin")

with open("metadata.pkl", "rb") as f:
    metadata = pickle.load(f)


def retrieve(query, k=5):
    q_embedding = model.encode([query])
    D, I = index.search(np.array(q_embedding), k)

    results = []
    for idx, dist in zip(I[0], D[0]):
        item = metadata[idx]
        item["score"] = float(1 / (1 + dist))  # confidence score
        results.append(item)

    return results


def generate_response(query, retrieved_docs):
    context = "\n".join([
        f"{doc['id']} - {doc['title']}: {doc['scope']}"
        for doc in retrieved_docs
    ])

    prompt = f"""
You are an expert in BIS standards.

User Query:
{query}

Relevant Standards:
{context}

Task:
Recommend the top 3-5 most relevant BIS standards and explain briefly why each applies.
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json()["response"]

    except:
        # fallback if LLM not running
        fallback = "Top Matching Standards:\n"
        for doc in retrieved_docs[:3]:
            fallback += f"\n{doc['id']} - {doc['title']}\n→ Relevant to {query}\n"
        return fallback


def get_recommendations(query):
    retrieved = retrieve(query)
    answer = generate_response(query, retrieved)
    return retrieved, answer
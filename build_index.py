import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle

# Load data
with open("data/bis_standards.json", "r") as f:
    data = json.load(f)

# Combine fields into searchable text
documents = [
    f"{item['id']} {item['title']} {item['scope']} {' '.join(item['keywords'])}"
    for item in data
]

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings
embeddings = model.encode(documents)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Save index + metadata
faiss.write_index(index, "faiss_index.bin")

with open("metadata.pkl", "wb") as f:
    pickle.dump(data, f)

print("✅ Index built successfully!")
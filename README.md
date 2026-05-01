# 🏗️ CiviAssist – IS Code RAG System (FAISS + Streamlit)

## 🚀 Overview

**CiviAssist** is an AI-powered **Retrieval-Augmented Generation (RAG)** system that recommends relevant **Indian Standard (IS) codes** based on user queries.

It uses **FAISS-based semantic search** to retrieve the most relevant standards from a structured dataset and displays them via a Streamlit interface.

---

## 🧠 Key Features

* 🔍 Semantic search using FAISS
* 🧠 RAG-based retrieval pipeline
* ⚡ Fast vector similarity search
* 📚 Domain-specific IS standards dataset
* 🖥️ Interactive Streamlit UI

---

## 📂 Project Structure

```id="struct2"
BIS-RAG/
│
├── data/
│   └── bis_standards.json
│
├── venv/
│
├── app.py
├── build_index.py
├── rag_engine.py
├── faiss_index.bin
├── metadata.pkl
├── requirements.txt
```

---

# ⚙️ Complete Setup Guide

## 🔹 1. Clone Repository

```bash id="c1"
git clone https://github.com/Suvanwita/civiassist.git
cd BIS-RAG
```

---

## 🔹 2. Create Virtual Environment

### ▶️ Linux / Mac:

```bash id="c2"
python3 -m venv venv
source venv/bin/activate
```

### ▶️ Windows:

```bash id="c3"
python -m venv venv
venv\Scripts\activate
```

---

## 🔹 3. Upgrade pip

```bash id="c4"
pip install --upgrade pip
```

---

## 🔹 4. Install Dependencies

```bash id="c5"
pip install -r requirements.txt
```

---

## 🔹 5. Build FAISS Index

```bash id="c6"
python build_index.py
```

This generates:

* `faiss_index.bin`
* `metadata.pkl`

---

## 🔹 6. Test Retrieval Engine (CLI Mode)

Run the RAG engine directly:

```bash id="c7"
python rag_engine.py
```

👉 This allows you to:

* Enter queries in terminal
* See retrieved IS codes
* Debug retrieval logic

---

## 🔹 7. Run Streamlit App

```bash id="c8"
streamlit run app.py
```

---

## 🔹 8. Open in Browser

```id="c9"
http://localhost:8501
```

---

# 🧪 Example Queries

* IS code for cement
* Standard for reinforced concrete
* Concrete mix design guidelines
* IS code for steel reinforcement
* Aggregates standard in construction

---

# ⚡ How It Works

### 🔹 Indexing (`build_index.py`)

* Loads dataset
* Converts text → embeddings
* Stores vectors in FAISS

### 🔹 Retrieval (`rag_engine.py`)

* Converts query → embedding
* Searches FAISS index
* Returns top matches

### 🔹 UI (`app.py`)

* Takes user input
* Displays ranked IS codes

---

# 📊 Sample Output

```json id="out2"
[
  {
    "id": "IS 456",
    "title": "Plain and Reinforced Concrete",
    "score": 0.92
  }
]
```

---

# 🔥 Future Enhancements

* 🤖 Add LLM for full RAG (answer generation)
* 📊 Visualization of similarity scores
* 🌐 FastAPI backend
* 🧠 Hybrid search (keyword + vector)
* 📄 Full document retrieval

---

# ⚠️ Limitations

* Dataset is limited
* Retrieval-only (no generative explanation yet)
* Performance depends on embeddings quality

---

# 🤝 Contributing

1. Fork the repo
2. Create branch
3. Commit changes
4. Open PR

---

# 📄 License

MIT License

---

# 💼 Author

CiviAssist is built to simplify IS code discovery using AI-driven semantic search for civil engineering applications.

---

# ⭐ Support

If you found this useful, consider giving a ⭐ on GitHub!

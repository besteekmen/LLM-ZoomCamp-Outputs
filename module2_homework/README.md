# LLM Zoomcamp 2026 — Module 2 Homework: Vector Search

This folder contains my complete implementation for the second module of the [DataTalksClub LLM Zoomcamp (2026 Cohort)](https://github.com/DataTalksClub/llm-zoomcamp).

The goal of this assignment was to build a practical **vector search pipeline** from scratch by generating embeddings for course documents and retrieving semantically relevant chunks using similarity search.

---

## 🛠️ Tech Stack & Key Implementations

* **Data Collection:** Downloaded and parsed raw lesson content directly from the course repository using `gitsource`.
* **Embedding Pipeline:** Used an ONNX-based embedding model to convert text chunks into dense vector representations for semantic retrieval.
* **Batch Processing:** Optimized embedding generation with `encode_batch()` to efficiently process multiple text chunks at once.
* **Chunking Strategy:** Split large lesson documents into manageable retrieval units while preserving semantic continuity.
* **Vector Search:** Implemented semantic similarity search using cosine similarity over embedded document vectors.

---

## 📊 Homework Highlights & Insights

### 1. Why Embeddings Matter

Traditional keyword search works well for exact term matches but struggles with semantic similarity. Vector embeddings solve this by mapping text into high-dimensional numerical space where semantically related content lies closer together.

Example:

```text
Query: "How does approximate nearest neighbor search work?"
```

Even if a document chunk does not explicitly contain the exact phrase, vector search can still retrieve relevant sections discussing:

* ANN
* IVF indexing
* HNSW graphs
* similarity-based retrieval

This makes retrieval significantly more robust than pure lexical search.

---

### 2. Brute-Force Vector Retrieval

This homework implemented **exact vector search** using brute-force similarity comparison.

For each user query, the retrieval pipeline works as follows:

```text
Encode query into a vector
→ Compare against all document embeddings
→ Compute cosine similarity scores
→ Return top-k most similar chunks
```

Advantages:

* Simple and easy to implement
* Guarantees retrieval of the true nearest chunks
* Works well for small and medium-sized datasets

Limitations:

* Computational cost grows linearly with dataset size
* Becomes inefficient for large-scale vector databases

This illustrates why production systems often adopt approximate nearest neighbor (ANN) indexing later for scalability, even though exact search is ideal for learning and experimentation.

---

### 3. Efficient Retrieval Pipeline

The complete semantic search workflow follows this structure:

```text
Raw Documents
   ↓
Chunking
   ↓
Embedding Generation (ONNX model)
   ↓
Vector Storage
   ↓
Query Embedding
   ↓
Similarity Search
   ↓
Top-k Relevant Chunks
```

This pipeline forms the retrieval backbone of modern RAG systems.

---

## 💻 Code Architecture

The implementation is organized inside a single notebook covering the full workflow:

* document preprocessing
* chunk generation
* batch embedding
* vector similarity search
* retrieval result inspection

👉 [View My Implementation Notebook](./course_vectorsearch.ipynb)

*Note: This homework uses locally generated embeddings and vector representations rather than relying solely on external APIs. Because the workflow includes downloaded model files and generated embeddings, some intermediate artifacts are intentionally stored locally and excluded from remote execution environments.*

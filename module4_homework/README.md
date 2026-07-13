# LLM Zoomcamp 2026 — Module 4 Homework: Evaluation

This folder contains my complete implementation for the fourth module of the [DataTalksClub LLM Zoomcamp (2026 Cohort)](https://github.com/DataTalksClub/llm-zoomcamp).

The goal of this assignment was to build an **evaluation framework** for Retrieval-Augmented Generation (RAG) systems by creating searchable indexes, measuring retrieval quality with standard information retrieval metrics, and comparing different search strategies using a common ground-truth dataset.

---

## 🛠️ Tech Stack & Key Implementations

- **Ground Truth Evaluation:** Loaded a labeled dataset of synthetic questions mapped to their corresponding lesson files.
- **Text Search:** Built a lexical search index using **MinSearch**, indexed by filename for document retrieval.
- **Vector Search:** Generated semantic embeddings using the Homework 2 embedding pipeline and built a **VectorSearch** index for similarity-based retrieval.
- **Evaluation Pipeline:** Reused the evaluation framework introduced in the course to measure retrieval performance consistently across search methods.
- **Search Metrics:** Computed **Hit Rate** and **Mean Reciprocal Rank (MRR)** to quantify retrieval quality.

---

## 📊 Homework Highlights & Insights

### 1. Why Evaluation Matters

Building a RAG system is only the first step. Without evaluation, it is impossible to determine whether changes to retrieval, prompts, or models actually improve performance.

This homework demonstrates how an offline evaluation framework provides an objective way to compare search systems before deployment by using a shared ground-truth dataset and reproducible metrics.

---

### 2. Comparing Search Strategies

Two retrieval approaches were implemented and evaluated:

- **Text Search (Lexical Retrieval):** Matches documents using keyword overlap.
- **Vector Search (Semantic Retrieval):** Retrieves documents based on embedding similarity, allowing semantically related content to be found even when exact keywords differ.

Using the same evaluation dataset makes it possible to compare both approaches under identical conditions and understand the trade-offs between lexical and semantic retrieval.

---

### 3. Measuring Retrieval Quality

The homework evaluates retrieval using two widely adopted information retrieval metrics:

- **Hit Rate:** Measures how often the correct document appears within the retrieved results.
- **Mean Reciprocal Rank (MRR):** Rewards systems that rank the correct document closer to the top of the result list.

Together, these metrics evaluate not only whether the correct document is retrieved, but also how effectively it is prioritized for downstream LLM generation.

---

### 4. Evaluation Workflow

The retrieval evaluation pipeline follows this structure:

```text
Ground Truth Questions
          ↓
Search Function
(Text Search / Vector Search)
          ↓
Top-k Retrieved Chunks
          ↓
Filename Matching
          ↓
Hit Rate & MRR
          ↓
Performance Comparison
```

This workflow provides a reproducible framework for benchmarking retrieval systems and forms the foundation for evaluating complete RAG pipelines.

---

## 💻 Code Architecture

The implementation is organized inside a single notebook covering the complete evaluation workflow:

- loading and preparing the ground-truth dataset
- building lexical and vector search indexes
- implementing reusable search functions
- computing retrieval relevance
- evaluating search quality using Hit Rate and MRR
- comparing search performance across retrieval methods

👉 [View My Implementation Notebook](./course_evaluation.ipynb)

*Note: This homework focuses on offline evaluation using a synthetic ground-truth dataset generated from the course materials. The evaluation framework is designed to benchmark retrieval quality before deployment and can later be extended with real user queries and online evaluation metrics.*
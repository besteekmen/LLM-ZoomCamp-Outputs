# LLM Zoomcamp 2026 — Module 1 Homework: Agentic RAG

This folder contains my complete implementation for the first module of the [DataTalksClub LLM Zoomcamp (2026 Cohort)](https://github.com/DataTalksClub/llm-zoomcamp). 

The goal of this assignment was to transition from a classic Retrieval-Augmented Generation (RAG) system into an **autonomous agent** capable of making its own search tool decisions, optimizing chunking parameters, and keeping strict tracking of token usage.

---

## 🛠️ Tech Stack & Key Implementations

- **Data Fetching:** Programmatically downloaded the raw course data directly from the DataTalksClub repository using `gitsource`.
- **Search & Retrieval:** Created an in-memory document indexing mechanism with `minsearch` to act as the primary knowledge base.
- **Chunking Strategy:** Configured advanced text segmentation by implementing a sliding window approach with a chunk size of **2000 characters** and an overlap step of **1000 characters**.
- **Agentic Workflow:** Constructed a multi-step execution loop with `toyaikit`, enabling the LLM to autonomously detect when it lacks sufficient context and call the local search index as a registered tool before finalizing answers.

---

## 📊 Homework Highlights & Insights

### 1. Token Overhead Analysis
A critical part of the assignment was mapping out token counts to observe how text architecture affects prompt sizes:
* **Base RAG Context:** Passing unfiltered documents bloated our token footprint, risking context window constraints.
* **Chunked RAG Context:** Using the optimized `(2000, 1000)` sliding window allowed the prompt to pass highly granular, targeted context blocks, significantly reducing overall generation overhead.

### 2. The Agent Loop in Action
By leveraging an agent framework rather than a hardcoded query pipeline, the model dynamically figures out its search queries. If a student asks a complex question about course policies, the system behaves as follows:

```text
[User] -> Ask a question about the course assignments
   ↓
[Agent] -> Thinks: "I need to query the index first"
   ↓
[Tool Call] -> minsearch.search(query="assignment deadlines")
   ↓
[Agent] -> Receives data segments, merges context, and generates the final response
```

---

## 💻 Code Architecture

The entire logic flow, from initialization and token analysis to the functional tool-calling loops, is structured cleanly inside a single notebook:

👉 [View My Implementation Notebook](./course_rag.ipynb)

*Note: The code utilizes an active OpenAI client session. To prevent unauthorized API token consumption, a live demo environment is intentionally omitted; however, full structural outcomes and print statements are recorded directly inside the execution blocks of the notebook.*
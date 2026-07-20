# LLM Zoomcamp 2026 — Module 5 Homework: Monitoring

This folder contains my complete implementation for the fifth module of the [DataTalksClub LLM Zoomcamp (2026 Cohort)](https://github.com/DataTalksClub/llm-zoomcamp).

The goal of this assignment was to add **observability** to a Retrieval-Augmented Generation (RAG) system by instrumenting it with **OpenTelemetry**, collecting execution metrics, and persisting trace data for later analysis. Instead of evaluating the system offline, this module focuses on monitoring how a deployed RAG application behaves during real usage.

---

## 🛠️ Tech Stack & Key Implementations

- **OpenTelemetry Instrumentation:** Added tracing to the RAG pipeline by wrapping the `rag()`, `search()`, and `llm()` methods with individual spans.
- **Custom Traced RAG:** Implemented a `RAGTraced` class extending the original `RAGBase` while preserving the existing retrieval and generation logic.
- **Span Attributes:** Recorded useful runtime metrics including:
  - input and output token counts
  - LLM API cost
  - query information
  - number of retrieved documents
  - response length
- **Custom SQLite Exporter:** Implemented a custom `SpanExporter` to persist completed spans into a SQLite database instead of printing them to the console.
- **Trace Analysis:** Queried the stored traces using SQL and pandas to analyze execution times, token usage, and system stability across multiple runs.

---

## 📊 Homework Highlights & Insights

### 1. From Offline Evaluation to Online Monitoring

The previous module focused on evaluating retrieval quality before deployment using a labeled dataset. In contrast, this homework demonstrates how to monitor a RAG application while it is running.

Rather than measuring only search quality, monitoring captures operational metrics such as response time, token usage, API cost, and execution traces. These metrics help understand how the system behaves under real user traffic and provide valuable information for debugging and optimization.

---

### 2. Instrumenting the RAG Pipeline

The original RAG implementation was extended without modifying its core logic by creating a `RAGTraced` subclass.

Three nested OpenTelemetry spans were recorded for every request:

- **rag** – represents the complete RAG pipeline.
- **search** – measures document retrieval.
- **llm** – measures the language model API call.

This hierarchical tracing structure makes it easy to understand how each component contributes to the overall execution time.

---

### 3. Recording Runtime Metrics

OpenTelemetry spans were enriched with custom attributes to capture meaningful runtime information.

Examples include:

- query text
- retrieved document count
- input tokens
- output tokens
- API cost
- generated response length

Unlike simple timing measurements, these attributes provide a richer view of application behavior and can later be visualized in monitoring dashboards.

---

### 4. Persisting Trace Data

Instead of using the default `ConsoleSpanExporter`, a custom `SQLiteSpanExporter` was implemented.

Each completed span is automatically stored inside a SQLite database containing:

- span name
- start time
- end time
- input tokens
- output tokens
- API cost

Persisting traces makes it possible to perform historical analysis, build dashboards, and compute aggregate metrics over multiple executions.

---

### 5. Analyzing Trace Data

The stored traces were queried using pandas to investigate system behavior.

The analysis showed that:

- the **LLM span** accounts for nearly all execution time, while document retrieval completes in only a few milliseconds.
- repeated executions of the same query produced **identical input token counts**, demonstrating that the retrieval pipeline consistently returned the same context.
- output tokens and total cost varied slightly between runs, reflecting the natural variability of language model responses.

These observations illustrate how monitoring can be used to identify performance bottlenecks and verify the consistency of a RAG system.

---

### 6. Monitoring Workflow

The monitoring pipeline follows this structure:

```text
User Query
     ↓
RAG Pipeline
(Search → Prompt → LLM)
     ↓
OpenTelemetry Spans
(rag, search, llm)
     ↓
Span Attributes
(tokens, cost, timing, metadata)
     ↓
SQLite Span Exporter
     ↓
SQLite Database
     ↓
SQL / pandas Analysis
```

This workflow demonstrates how OpenTelemetry enables end-to-end observability by collecting runtime information that can later be analyzed or visualized using dashboards.

---

## 💻 Code Architecture

The implementation is organized into reusable components:

- `rag_helper.py` — base RAG implementation and traced `RAGTraced` subclass
- `sqlite_exporter.py` — custom OpenTelemetry SQLite span exporter
- `starter.py` — tracing configuration and application entry point
- `course_monitoring.ipynb` — querying and analyzing trace data stored in SQLite

👉 **View My Implementation Notebook:** [course_monitoring.ipynb](./course_monitoring.ipynb)

*Note: This homework introduces observability for Retrieval-Augmented Generation systems using OpenTelemetry. By instrumenting the RAG pipeline, persisting traces, and analyzing runtime metrics, it demonstrates how monitoring complements offline evaluation and provides visibility into real-world system performance.*
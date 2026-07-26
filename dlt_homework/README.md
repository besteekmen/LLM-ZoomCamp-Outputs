# LLM Zoomcamp 2026 — dlt Homework: Trace Extraction & Analysis

This folder contains my implementation for the dlt workshop homework from the [DataTalksClub LLM Zoomcamp (2026 Cohort)](https://github.com/DataTalksClub/llm-zoomcamp).

The goal of this assignment was to instrument an AI agent with **Pydantic Logfire** for observability, export the collected traces using **dlt**, store them in **DuckDB**, and analyze the resulting telemetry data.

This homework demonstrates how modern AI applications can be monitored by collecting detailed execution traces, including agent runs, LLM calls, tool usage, and token consumption.

---

## 🛠️ Tech Stack & Key Implementations

- **Pydantic AI Agent:** Used the rewritten FAQ agent implementation based on Pydantic AI.
- **Pydantic Logfire Instrumentation:** Added Logfire tracing to automatically capture:
  - agent executions
  - LLM calls
  - tool calls
  - token usage
  - model information
- **dlt Pipeline:** Built a data loading pipeline to extract Logfire traces through the REST API and load them into DuckDB.
- **DuckDB Analysis:** Queried the normalized trace data to investigate:
  - number of generated tables
  - agent execution spans
  - input token usage across LLM calls

---

## 📊 Homework Highlights & Insights

## 1. Instrumenting the Agent with Logfire

The original FAQ agent was extended with Logfire observability:

```python
logfire.configure()
logfire.instrument_pydantic_ai()
```
This enabled automatic tracing of the agent workflow without manually adding spans.

Each agent execution generated traces containing:

- agent runs
- model requests
- tool calls
- input/output messages
- token usage metadata

This demonstrates how observability can be added to AI applications with minimal changes to the application logic.

---

## 2. Extracting Trace Data with dlt

The Logfire traces contain deeply nested JSON structures, including:

- LLM messages
- tool calls
- model metadata
- token usage information
- execution details

A dlt pipeline was created to pull this data from the Logfire API and store it locally in DuckDB.

The pipeline workflow:

Pydantic AI Agent
        ↓
Pydantic Logfire
        ↓
Logfire REST API
        ↓
dlt Pipeline
        ↓
DuckDB Database
        ↓
SQL Analysis

dlt automatically normalized the nested trace data into multiple relational tables, making the telemetry easier to query.

---

## 3. Exploring Normalized Trace Data

The dlt pipeline created multiple normalized tables inside the `agent_traces` dataset.

Examples include:

- `spans`
- `spans__values`
- nested message tables
- tool call tables
- model metadata tables
The normalized structure allows complex JSON traces to be analyzed using standard SQL queries.

---

## 4. Querying Token Usage

The LLM token usage information was stored in `gen_ai_usage_input_tokens` within the normalized `spans__values` table. For the Q3 analysis, token usage was grouped by `gen_ai_conversation_id` to separate individual agent executions.

The selected agent run produced input tokens: 3859

---

## 📝 Homework Results

The query outputs used as submission evidence are saved in:

- [q1_output.txt](./q1_output.txt) — Logfire span count analysis
- [q2_output.txt](./q2_output.txt) — dlt table count analysis
- [q3_output.txt](./q3_output.txt) — token usage analysis

These files contain the terminal outputs used to verify each homework answer.

---

## 💻 Code Architecture

The implementation contains:

- `agent.py` — Pydantic AI FAQ agent implementation
- `main.py` — Runs the agent and generates Logfire traces
- `logfire_pipeline.py` — dlt pipeline that extracts Logfire data into DuckDB

---

## 🔍 Key Takeaways

This homework demonstrates the complete observability workflow for an AI agent:

1. Instrument an agent application.
2. Collect execution traces automatically.
3. Extract telemetry data from an observability platform.
4. Normalize complex trace structures into analytical tables.
5. Query the collected data to understand system behavior.

Compared with traditional application monitoring, AI observability requires tracking additional information such as LLM calls, token usage, model behavior, and tool interactions.

By combining Pydantic Logfire and dlt, raw agent execution data can be transformed into structured analytical data suitable for debugging, monitoring, and optimization.

👉 **View My Implementation Files:**  
- [logfire_pipeline.py](./logfire_pipeline.py) — dlt pipeline for extracting Logfire traces into DuckDB  
- [main.py](./main.py) — Runs the agent and generates Logfire traces
- [q1_output.txt](./q1_output.txt), [q2_output.txt](./q2_output.txt), [q3_output.txt](./q3_output.txt) — Homework query outputs and verification results  

*Note: This homework introduces observability for AI agents using Pydantic Logfire and dlt. By collecting agent execution traces, normalizing nested telemetry data, and analyzing LLM usage metrics with DuckDB, it demonstrates how AI application behavior can be monitored, explored, and optimized using structured trace data.*


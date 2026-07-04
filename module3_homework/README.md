# LLM Zoomcamp 2026 — Module 3 Homework: AI Orchestration with Kestra

This folder contains my implementation for the third module of the [DataTalksClub LLM Zoomcamp (2026 Cohort)](https://github.com/DataTalksClub/llm-zoomcamp).

The objective of this assignment was to explore **AI workflow orchestration** using **Kestra**, learning how declarative workflows can coordinate LLM-powered applications, Retrieval-Augmented Generation (RAG) pipelines, and agentic systems. Instead of manually executing individual tasks, the workflow is defined as a series of reusable, version-controlled steps executed by Kestra.

---

## 🛠️ Tech Stack & Key Implementations

- **Kestra:** Built declarative workflows using YAML-based flow definitions.
- **Docker Compose:** Ran Kestra locally inside a containerized environment for reproducibility.
- **AI Orchestration:** Explored how LLM workflows can be organized into modular, reusable pipelines.
- **AI Copilot:** Used Kestra's AI Copilot to assist with generating and refining workflow definitions.
- **Workflow Execution:** Executed and inspected flows through the Kestra UI.

---

## 📊 Homework Highlights & Insights

### 1. Why AI Orchestration Matters

As LLM applications become more sophisticated, they often involve multiple coordinated steps such as retrieving context, calling language models, processing outputs, handling failures, and storing results. Embedding all of this logic inside a single script quickly becomes difficult to maintain.

Workflow orchestration separates **what** should happen from **how** it is executed, making AI applications more reliable, reproducible, and easier to extend.

---

### 2. Declarative Workflows

Kestra uses declarative YAML files to define workflows.

Rather than writing imperative code that manually coordinates each operation, the workflow describes:

```text
Task A
    ↓
Task B
    ↓
Task C
```

Kestra is responsible for executing each step in order, managing dependencies, logging execution, and exposing the workflow through its web interface.

This declarative approach makes workflows easier to understand, version control, and reuse.

---

### 3. Building AI Workflows

The module introduces orchestration concepts that extend traditional data pipelines into AI systems, including:

- context engineering
- RAG workflows
- agentic workflows
- multi-agent orchestration
- production considerations such as observability and maintainability

Although the examples remain relatively small, they illustrate how orchestration becomes increasingly valuable as AI applications grow in complexity.

---

## 💻 Project Structure

```
module3_homework/
├── docker-compose.yml
├── flows/
│   ├── ...
│   └── ...
└── README.md
```

- **`docker-compose.yml`** starts the local Kestra environment.
- **`flows/`** contains the workflow definitions created for the homework exercises.
- The workflows can be imported into Kestra and executed through its web interface.

---

## 🚀 Running the Project

Start the local Kestra instance:

```bash
docker compose up
```

After the services are running:

1. Open the Kestra web interface.
2. Import the flows from the `flows/` directory.
3. Execute the workflows and inspect each execution through the dashboard.

---

## 📚 Learning Outcomes

This homework introduced the foundations of AI orchestration by demonstrating how modern workflow engines can coordinate LLM-powered applications.

Key concepts explored include:

- defining workflows declaratively
- orchestrating AI tasks with Kestra
- containerized development using Docker Compose
- leveraging AI Copilot for workflow creation
- understanding how orchestration supports RAG and agentic AI systems

Together with the previous module on vector search, this module provides the orchestration layer needed to organize and manage increasingly complex AI workflows in a structured and reproducible manner.

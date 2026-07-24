# Module 5 – Monitoring

This project is my implementation of the **Monitoring** module from **DataTalksClub LLM Zoomcamp 2026**.

The goal is to monitor an LLM-powered RAG application by:

- storing conversations in PostgreSQL
- collecting metrics (latency, token usage, cost)
- collecting judge and user feedback
- visualising metrics with Streamlit and Grafana
- generating synthetic traffic for testing
- orchestrating everything with Docker Compose

---

# Technologies

- Python
- Streamlit
- PostgreSQL
- Grafana
- Docker
- Docker Compose
- OpenAI API

---

# Project Structure

```
module5_monitoring/
├── app.py                  # Streamlit chatbot UI
├── assistant.py            # Creates the RAG assistant
├── rag_helper.py           # Core RAG pipeline
├── metrics.py              # Records latency, tokens and cost
├── ingest.py               # Downloads FAQ and builds search index
├── judge.py                # LLM-based relevance evaluator
├── evaluation_utils.py     # Evaluation helper functions
├── generate_data.py        # Generates synthetic conversations
│
├── db_init.py              # Creates database tables
├── db_save.py              # Saves conversations
├── db_feedback.py          # Saves feedback
├── db_query.py             # Reads statistics from PostgreSQL
│
├── dashboard.py            # Streamlit monitoring dashboard
│
├── Dockerfile              # Builds Streamlit container
├── docker-compose.yaml     # Starts PostgreSQL, Grafana and Streamlit
├── Makefile                # Convenience commands
├── pyproject.toml          # Python dependencies
└── README.md
```

---

# Database

## conversations

Stores:

- question
- answer
- model
- prompt
- token usage
- response time
- cost
- timestamp

## feedback

Stores:

- judge relevance
- user thumbs up/down
- explanations

---

# Dashboards

## Streamlit

Runs on:

```
http://localhost:8501
```

Provides a lightweight monitoring dashboard.

---

## Grafana

Runs on:

```
http://localhost:3000
```

Default login:

```
Username: admin
Password: admin
```

Example panels:

- Response Time
- Token Usage
- Cost
- Model Usage
- Relevance Distribution
- User Feedback
- Recent Conversations

---

# Running the Project

## First time

Build and start everything:

```bash
docker compose up --build
```

Open another terminal and initialise the database:

```bash
docker compose exec streamlit python db_init.py
```

---

## Daily usage

Start existing containers:

```bash
docker compose start
```

or

```bash
docker compose up
```

---

Stop everything:

```bash
docker compose down
```

---

View running services:

```bash
docker compose ps
```

---

View logs:

```bash
docker compose logs -f
```

---

Generate synthetic traffic:

```bash
docker compose exec streamlit python generate_data.py
```

Stop with:

```
Ctrl + C
```

---

Query the database:

```bash
docker compose exec postgres \
psql -U user -d course_assistant \
-c "SELECT id, question, response_time, cost FROM conversations;"
```

---

# Docker Compose Cheat Sheet

| Command | Purpose | Keeps data? |
|----------|---------|-------------|
| `docker compose up` | Create missing containers and start them | ✅ |
| `docker compose start` | Start existing stopped containers | ✅ |
| `docker compose stop` | Stop containers | ✅ |
| `docker compose down` | Remove containers (volumes kept) | ✅ |
| `docker compose down -v` | Remove containers and Docker volumes | ❌ |

---

# Notes

### Why use `docker compose exec`?

Once the application runs inside Docker, helper scripts (such as `db_init.py` or `generate_data.py`) should also run inside the Streamlit container so they use the same network and environment variables.

Example:

```bash
docker compose exec streamlit python db_init.py
```

instead of

```bash
uv run python db_init.py
```

---

### Why does the official lesson use `uv run python db_init.py`?

The Zoomcamp lesson assumes the project itself is running directly on the host machine.

In this repository, the application runs inside Docker, so helper scripts should also be executed inside the Streamlit container using `docker compose exec`.

The monitoring concepts are identical; only the project layout differs.

---

# Summary

This module demonstrates how to monitor an LLM application using:

- PostgreSQL for persistence
- Streamlit for the chatbot and monitoring dashboard
- Grafana for advanced visualisation
- Docker Compose for orchestration
- Synthetic traffic generation
- Automated and human feedback
FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
ENV PATH="/app/.venv/bin:$PATH"

# Copy only this module's dependency definition
COPY module5_monitoring/pyproject.toml ./
#RUN uv sync --locked

# install the dependencies from this module's pyproject.toml
RUN uv sync

# added due to this particular module being run under the whole project
COPY module5_monitoring/ .

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
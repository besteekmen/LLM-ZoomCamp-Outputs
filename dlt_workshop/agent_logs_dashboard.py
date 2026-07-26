import marimo

__generated_with = "0.23.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import altair as alt
    import dlt

    return alt, dlt, mo


@app.cell
def _(mo):
    mo.md("""
    # AI Agent Logs Dashboard

    This dashboard explores the synthetic AI agent logs loaded into DuckDB
    using a dlt pipeline.

    The data contains one row per JSONL record.
    """)
    return


@app.cell
def _(dlt):
    pipeline = dlt.pipeline(
        pipeline_name="agent_logs_pipeline",
        destination="duckdb",
        dataset_name="logs",
    )

    dataset = pipeline.dataset()
    return (dataset,)


@app.cell
def _(dataset):
    overview = dataset(
        """
    SELECT
    COUNT(*) AS total_records,
    COUNT(DISTINCT session_id) AS sessions,
    COUNT(DISTINCT project) AS projects,
    MIN(timestamp) AS first_record,
    MAX(timestamp) AS last_record
    FROM log_records
    """
    ).df()
    return (overview,)


@app.cell
def _(mo, overview):
    row = overview.iloc[0]

    mo.md(
        f"""
    ## Overview

    | Metric | Value |
    |---|---:|
    | Total Records | {row.total_records} |
    | Sessions | {row.sessions} |
    | Projects | {row.projects} |
    | First Record | {row.first_record} |
    | Last Record | {row.last_record} |
    """
    )
    return


@app.cell
def _(dataset):
    df_types = dataset(
        """
    SELECT
    type,
    COUNT(*) AS records
    FROM log_records
    GROUP BY type
    ORDER BY records DESC
    """
    ).df()
    return (df_types,)


@app.cell
def _(alt, df_types):
    alt.Chart(df_types).mark_bar().encode(
        x=alt.X("type:N", sort="-y"),
        y="records:Q",
        tooltip=["type", "records"],
    ).properties(
        title="Records by Message Type",
        width=700,
    )
    return


@app.cell
def _(dataset):
    df_daily = dataset(
        """
    SELECT
    DATE_TRUNC('day', timestamp) AS day,
    type,
    COUNT(*) AS records
    FROM log_records
    GROUP BY 1,2
    ORDER BY 1
    """
    ).df()
    return (df_daily,)


@app.cell
def _(alt, df_daily):
    alt.Chart(df_daily).mark_line(point=True).encode(
        x="day:T",
        y="records:Q",
        color="type:N",
        tooltip=["day", "type", "records"],
    ).properties(
        title="Daily Activity by Message Type",
        width=700,
    )
    return


@app.cell
def _(dataset):
    df_projects = dataset(
        """
    SELECT
    project,
    COUNT(*) AS records
    FROM log_records
    GROUP BY project
    ORDER BY records DESC
    """
    ).df()
    return (df_projects,)


@app.cell
def _(alt, df_projects):
    alt.Chart(df_projects).mark_bar().encode(
        x=alt.X("project:N", sort="-y"),
        y="records:Q",
        tooltip=["project", "records"],
    ).properties(
        title="Records by Project",
        width=700,
    )
    return


@app.cell
def _(dataset):
    df_sessions = dataset(
        """
    SELECT
    session_id,
    COUNT(*) AS records
    FROM log_records
    GROUP BY session_id
    ORDER BY records DESC
    """
    ).df()
    return (df_sessions,)


@app.cell
def _(alt, df_sessions):
    alt.Chart(df_sessions).mark_bar().encode(
        x=alt.X("session_id:N", sort="-y"),
        y="records:Q",
        tooltip=["session_id", "records"],
    ).properties(
        title="Records per Session",
        width=700,
    )
    return


@app.cell
def _(dataset):
    df_files = dataset(
        """
    SELECT
    source_file,
    COUNT(*) AS records
    FROM log_records
    GROUP BY source_file
    ORDER BY records DESC
    LIMIT 10
    """
    ).df()
    return (df_files,)


@app.cell
def _(alt, df_files):
    alt.Chart(df_files).mark_bar().encode(
        x=alt.X("records:Q"),
        y=alt.Y("source_file:N", sort="-x"),
        tooltip=["source_file", "records"],
    ).properties(
        title="Top Source Files",
        width=700,
        height=300,
    )
    return


@app.cell
def _(dataset):
    dataset(
        """
    SELECT
    timestamp,
    project,
    session_id,
    type
    FROM log_records
    ORDER BY timestamp DESC
    LIMIT 100
    """
    ).df()
    return


if __name__ == "__main__":
    app.run()

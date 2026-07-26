import os

import dlt
from dotenv import load_dotenv
from dlt.sources.rest_api import RESTAPIConfig, rest_api_resources

load_dotenv()

READ_TOKEN = os.getenv("LOGFIRE_READ_TOKEN")


@dlt.source(name="logfire")
def logfire_source(read_token=READ_TOKEN):
    config: RESTAPIConfig = {
        "client": {
            "base_url": "https://logfire-eu.pydantic.dev/v1/",
            "auth": {
                "type": "bearer",
                "token": read_token,
            },
        },
        "resource_defaults": {
            "write_disposition": "replace",
        },
        "resources": [
            {
                "name": "spans",
                "endpoint": {
                    "path": "query",
                    "params": {
                        # Fetch recent spans
                        "sql": "SELECT * FROM records LIMIT 1000"
                    },
                },
            },
        ],
    }

    yield from rest_api_resources(config)


def load():
    pipeline = dlt.pipeline(
        pipeline_name="logfire_pipeline",
        destination="duckdb",
        dataset_name="agent_traces",
    )

    info = pipeline.run(logfire_source())

    print(info)
    print(pipeline.last_trace.last_normalize_info)


if __name__ == "__main__":
    load()
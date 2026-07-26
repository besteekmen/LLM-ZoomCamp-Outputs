"""dlt REST API pipeline: Claude Code Agent Logs API -> DuckDB."""

import dlt
from dlt.sources.rest_api import RESTAPIConfig, rest_api_resources

BASE_URL = "https://test-agent-traces-api-xt2e7ottma-ew.a.run.app"


@dlt.source(name="agent_logs_api")
def agent_logs_source(base_url: str = dlt.config.value, page_size: int = 1000):
    config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "paginator": {
                "type": "offset",
                "limit": page_size,
                "offset": 0,
                "limit_param": "limit",
                "offset_param": "offset",
                "total_path": "total",
            },
        },
        "resource_defaults": {
            "write_disposition": "replace",
        },
        "resources": [
            {
                "name": "logs",
                "endpoint": {
                    "path": "/logs",
                    "data_selector": "logs",
                },
                "primary_key": "index",
            },
        ],
    }

    yield from rest_api_resources(config)


def load(full=False):
    pipeline = dlt.pipeline(
        pipeline_name="agent_traces",
        destination="duckdb", # set to playground to persist data
        dataset_name="traces",
    )

    source = agent_logs_source(base_url=BASE_URL)

    if not full:
        source.add_limit(1)

    info = pipeline.run(source)

    print(info)
    print(pipeline.last_trace.last_normalize_info)


if __name__ == "__main__":
    import sys

    load(full="--full" in sys.argv)
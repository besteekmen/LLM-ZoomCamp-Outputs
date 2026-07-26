"""Deployment manifest — import the pipelines and notebooks you want to deploy and list them in __all__."""

# from pipeline import my_pipeline
# from notebook import my_notebook

#__all__: list[str] = []

from dlt._workspace.deployment import pipeline_run
from rest_api_pipeline import load


@pipeline_run("agent_traces")
def rest_api_pipeline():
    load(full=False)


__all__ = ["rest_api_pipeline"]
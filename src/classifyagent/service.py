"""Service layer for payload classification."""

from __future__ import annotations
from classifyagent.classifier import classify_payload_with_agent
from classifyagent.models import PayloadItem, RunResult


class ClassificationService:
    """Coordinates classification requests and response construction."""

    def run(self, payload: list[PayloadItem]) -> RunResult:
        """Classify the provided payload items.

        Args:
            payload: Items to classify.

        Returns:
            RunResult: Structured classification response.
        """
        classifications = classify_payload_with_agent(payload)
        return RunResult(classifications=classifications)

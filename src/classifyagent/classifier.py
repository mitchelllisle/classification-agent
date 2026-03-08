from __future__ import annotations

"""BAML-backed classification helpers."""

from baml_client.sync_client import b  # type: ignore
from classifyagent.models import ClassificationEntry, PayloadItem


def classify_payload_with_agent(payload: list[PayloadItem]) -> list[ClassificationEntry]:
    """Classify payload items by calling the generated BAML sync client.

    Args:
        payload: Items containing name, description, and sample values.

    Returns:
        list[ClassificationEntry]: Classification output for each payload item.
    """
    if not payload:
        return []


    response = b.ClassifyPayloadItems(
        payload=[item.model_dump() for item in payload],
        policy_context=(
            "Classify each item by combining field semantics (name/description) and sample values. "
            "Use public, private, confidential, or highly-confidential."
        ),
    )

    return [
        ClassificationEntry(
            name=item.name,
            classification=item.classification,
            rationale=item.rationale,
            confidence=item.confidence,
        )
        for item in response.classifications
    ]

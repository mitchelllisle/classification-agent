"""Pydantic models for request and response contracts."""

from typing import Literal

from pydantic import BaseModel, Field

ClassificationLevel = Literal[
    "public",
    "private",
    "confidential",
    "highly-confidential",
]


class PayloadItem(BaseModel):
    """Single payload item to classify."""

    name: str = Field(min_length=1)
    description: str = ""
    samples: list[str] = Field(default_factory=list)


class RunRequest(BaseModel):
    """Top-level API request body for classification."""

    payload: list[PayloadItem] = Field(default_factory=list)


class ClassificationEntry(BaseModel):
    """Classification output for a named payload item."""

    name: str
    classification: ClassificationLevel
    rationale: str = ""
    confidence: float | None = Field(default=None, ge=0.0, le=1.0)


class RunResult(BaseModel):
    """Top-level API response body for classification results."""

    classifications: list[ClassificationEntry]

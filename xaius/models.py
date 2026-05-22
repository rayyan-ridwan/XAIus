"""Data models for XAIus."""

from dataclasses import dataclass, field
from typing import Iterable


@dataclass(frozen=True)
class ModelProfile:
    """Describe a candidate model for explainable AI selection."""

    name: str
    family: str
    transparency: float
    interpretability: float
    salience: float
    tags: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        for field_name in ("transparency", "interpretability", "salience"):
            value = getattr(self, field_name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{field_name} must be between 0 and 1")

    def matches(self, keywords: Iterable[str]) -> int:
        """Return how many keywords overlap with the model tags."""

        normalized_tags = {tag.lower() for tag in self.tags}
        return sum(1 for keyword in keywords if keyword.lower() in normalized_tags)

    def explainability_score(self) -> float:
        """Return the base explainability score."""

        return (self.transparency + self.interpretability + self.salience) / 3.0

"""Model ranking logic for XAIus."""

from dataclasses import dataclass
from typing import Iterable, Sequence

from .models import ModelProfile

TAG_BONUS_PER_MATCH = 0.05
FAMILY_BONUS = 0.02


@dataclass(frozen=True)
class RankedModel:
    """A model profile plus its computed ranking score."""

    profile: ModelProfile
    score: float


class XAISelector:
    """Rank models by explainability and use-case fit."""

    def rank(
        self,
        profiles: Sequence[ModelProfile],
        preferred_tags: Iterable[str] = (),
    ) -> list[RankedModel]:
        ranked = [
            RankedModel(
                profile=profile,
                score=self._score(profile, preferred_tags),
            )
            for profile in profiles
        ]
        return sorted(
            ranked,
            key=lambda item: (-item.score, item.profile.name.lower()),
        )

    def recommend(
        self,
        profiles: Sequence[ModelProfile],
        preferred_tags: Iterable[str] = (),
        top_k: int = 3,
    ) -> list[ModelProfile]:
        """Return the highest-ranked model profiles."""

        return [
            item.profile
            for item in self.rank(profiles, preferred_tags=preferred_tags)[:top_k]
        ]

    def _score(self, profile: ModelProfile, preferred_tags: Iterable[str]) -> float:
        base_score = profile.explainability_score()
        tag_matches = profile.matches(preferred_tags)
        tag_bonus = TAG_BONUS_PER_MATCH * tag_matches
        family_bonus = FAMILY_BONUS if profile.family.lower() in {"rule-based", "tree"} else 0.0
        return round(base_score + tag_bonus + family_bonus, 4)

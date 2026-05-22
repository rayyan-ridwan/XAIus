"""Example usage for the XAIus selector."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from xaius import ModelProfile, XAISelector


def main() -> None:
    selector = XAISelector()
    profiles = [
        ModelProfile(
            name="Interpretable Tree",
            family="tree",
            transparency=0.92,
            interpretability=0.88,
            salience=0.76,
            tags=("healthcare", "finance"),
        ),
        ModelProfile(
            name="Black Box Ensemble",
            family="ensemble",
            transparency=0.42,
            interpretability=0.31,
            salience=0.52,
            tags=("general",),
        ),
    ]

    for ranked in selector.rank(profiles, preferred_tags=("healthcare",)):
        print(f"{ranked.profile.name}: {ranked.score:.2f}")


if __name__ == "__main__":
    main()

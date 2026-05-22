"""Tests for the XAIus selector."""

import unittest

from xaius import ModelProfile, XAISelector


class SelectorTests(unittest.TestCase):
    def test_rank_prefers_more_explainable_models(self) -> None:
        selector = XAISelector()
        profiles = [
            ModelProfile(
                name="Complex Model",
                family="ensemble",
                transparency=0.3,
                interpretability=0.2,
                salience=0.4,
            ),
            ModelProfile(
                name="Simple Model",
                family="tree",
                transparency=0.9,
                interpretability=0.8,
                salience=0.85,
            ),
        ]

        ranked = selector.rank(profiles)

        self.assertEqual(ranked[0].profile.name, "Simple Model")
        self.assertGreater(ranked[0].score, ranked[1].score)

    def test_recommend_limits_results(self) -> None:
        selector = XAISelector()
        profiles = [
            ModelProfile(
                name="A",
                family="tree",
                transparency=0.8,
                interpretability=0.7,
                salience=0.9,
            ),
            ModelProfile(
                name="B",
                family="rule-based",
                transparency=0.7,
                interpretability=0.7,
                salience=0.7,
            ),
            ModelProfile(
                name="C",
                family="ensemble",
                transparency=0.6,
                interpretability=0.6,
                salience=0.6,
            ),
        ]

        recommendations = selector.recommend(profiles, top_k=2)

        self.assertEqual(len(recommendations), 2)
        self.assertEqual([profile.name for profile in recommendations], ["A", "B"])

    def test_preferred_tags_increase_score(self) -> None:
        selector = XAISelector()
        matching = ModelProfile(
            name="Matching",
            family="ensemble",
            transparency=0.6,
            interpretability=0.6,
            salience=0.6,
            tags=("healthcare",),
        )
        non_matching = ModelProfile(
            name="NonMatching",
            family="ensemble",
            transparency=0.6,
            interpretability=0.6,
            salience=0.6,
            tags=("finance",),
        )

        ranked = selector.rank([non_matching, matching], preferred_tags=("healthcare",))

        self.assertEqual(ranked[0].profile.name, "Matching")
        self.assertGreater(ranked[0].score, ranked[1].score)


if __name__ == "__main__":
    unittest.main()

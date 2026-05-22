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
        self.assertTrue(all(isinstance(profile, ModelProfile) for profile in recommendations))


if __name__ == "__main__":
    unittest.main()

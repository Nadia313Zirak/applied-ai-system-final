from src.profile_builder import build_profile
from src.recommender import recommend_songs


def test_build_profile_valid_input():
    profile, warnings = build_profile("chill", "lofi", "low", "studying")

    assert profile["preferred_mood"] == "chill"
    assert profile["preferred_genre"] == "lofi"
    assert len(warnings) == 0


def test_build_profile_invalid_input_uses_guardrails():
    profile, warnings = build_profile("unknown", "fakegenre", "super", "sleeping")

    assert profile["preferred_mood"] == "relaxed"
    assert profile["preferred_genre"] == "lofi"
    assert len(warnings) == 4


def test_recommender_returns_results():
    profile, _ = build_profile("chill", "lofi", "low", "studying")
    result = recommend_songs(profile)

    assert "recommendations" in result
    assert len(result["recommendations"]) > 0
    assert result["recommendations"][0]["confidence"] >= 0
    assert result["recommendations"][0]["explanation"] != ""
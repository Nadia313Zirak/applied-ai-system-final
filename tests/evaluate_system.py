from src.profile_builder import build_profile
from src.recommender import recommend_songs


TEST_CASES = [
    {
        "name": "Chill studying profile",
        "mood": "chill",
        "genre": "lofi",
        "energy": "low",
        "activity": "studying",
    },
    {
        "name": "High energy gym profile",
        "mood": "intense",
        "genre": "rock",
        "energy": "high",
        "activity": "gym",
    },
    {
        "name": "Invalid input guardrail test",
        "mood": "unknown",
        "genre": "fakegenre",
        "energy": "super",
        "activity": "sleeping",
    },
]


def run_evaluation():
    passed = 0

    print("AI Music Taste Assistant Evaluation")
    print("-----------------------------------")

    for case in TEST_CASES:
        profile, warnings = build_profile(
            case["mood"],
            case["genre"],
            case["energy"],
            case["activity"],
        )

        result = recommend_songs(profile)
        recommendations = result["recommendations"]

        has_recommendations = len(recommendations) > 0
        has_explanations = all(item["explanation"] for item in recommendations)
        has_confidence = all(item["confidence"] >= 0 for item in recommendations)

        test_passed = has_recommendations and has_explanations and has_confidence

        if test_passed:
            passed += 1

        print(f"\nTest: {case['name']}")
        print(f"Status: {'PASS' if test_passed else 'FAIL'}")
        print(f"Warnings: {warnings if warnings else 'None'}")
        print(f"Top Recommendation: {recommendations[0]['song']['title']}")
        print(f"Confidence: {recommendations[0]['confidence']}%")
        print(f"Reliability: {recommendations[0]['reliability_label']}")

    print("\nEvaluation Summary")
    print("------------------")
    print(f"Passed {passed}/{len(TEST_CASES)} test cases.")


if __name__ == "__main__":
    run_evaluation()
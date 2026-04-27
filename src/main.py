from src.profile_builder import build_profile
from src.recommender import recommend_songs

print("\n🔍 AI Decision Process:")
print("Step 1: Validating user input...")
print("Step 2: Building taste profile...")
print("Step 3: Retrieving songs from dataset...")
print("Step 4: Scoring songs based on similarity...")
print("Step 5: Ranking and selecting top matches...")
print("Step 6: Generating explanations...\n")


def print_recommendations(result):
    if result["guardrail_message"]:
        print("\n⚠️ Guardrail Notice:")
        print(result["guardrail_message"])

    print("\n🎵 Top Music Recommendations:\n")

    for index, item in enumerate(result["recommendations"], start=1):
        song = item["song"]

        print(f"{index}. {song['title']} by {song['artist']}")
        print(f"   Score: {item['score']}")
        print(f"   Confidence: {item['confidence']}%")
        print(f"   Reliability: {item['reliability_label']}")
        print(f"   Explanation: {item['explanation']}")
        print()


def main():
    print("🎧 AI Music Taste Assistant")
    print("This system recommends songs based on your mood, genre, energy, and activity.")
    print()

    mood = input("Enter mood (happy, chill, intense, relaxed): ")
    genre = input("Enter genre (pop, lofi, rock, ambient, jazz): ")
    energy = input("Enter energy level (low, medium, high): ")
    activity = input("Enter activity (studying, gym, relaxing, driving): ")

    profile, warnings = build_profile(mood, genre, energy, activity)

    if warnings:
        print("\n⚠️ Input Validation Warnings:")
        for warning in warnings:
            print(f"- {warning}")

    result = recommend_songs(profile)
    print_recommendations(result)


if __name__ == "__main__":
    main()
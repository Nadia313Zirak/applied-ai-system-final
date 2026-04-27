import csv


def load_songs(csv_path="data/songs.csv"):
    songs = []

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            song = {
                "id": row["id"],
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"].lower(),
                "mood": row["mood"].lower(),
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    return songs


def closeness_score(song_value, preferred_value):
    return max(0, 1 - abs(song_value - preferred_value))


def tempo_score(song_tempo, preferred_tempo=100):
    difference = abs(song_tempo - preferred_tempo)
    return max(0, 1 - difference / 100)


def score_song(song, profile):
    score = 0
    reasons = []

    if song["genre"] == profile["preferred_genre"]:
        score += 2.0
        reasons.append(f"matches your preferred genre: {profile['preferred_genre']}")

    if song["mood"] == profile["preferred_mood"]:
        score += 1.5
        reasons.append(f"matches your mood: {profile['preferred_mood']}")

    energy_match = closeness_score(song["energy"], profile["preferred_energy"])
    valence_match = closeness_score(song["valence"], profile["preferred_valence"])
    dance_match = closeness_score(song["danceability"], profile["preferred_danceability"])
    acoustic_match = closeness_score(song["acousticness"], profile["preferred_acousticness"])

    score += energy_match
    score += valence_match
    score += dance_match
    score += acoustic_match

    if energy_match >= 0.75:
        reasons.append("has a similar energy level")

    if valence_match >= 0.75:
        reasons.append("has a similar emotional tone")

    if dance_match >= 0.75:
        reasons.append("fits your activity vibe")

    if acoustic_match >= 0.75:
        reasons.append("has a similar acoustic feel")

    confidence = min(round((score / 7.5) * 100, 1), 100)

    if confidence >= 75:
        reliability_label = "Strong match"
    elif confidence >= 50:
        reliability_label = "Moderate match"
    else:
        reliability_label = "Weak match"

    if not reasons:
        reasons.append("it was one of the closest available matches in the dataset")

    return {
        "song": song,
        "score": round(score, 2),
        "confidence": confidence,
        "reliability_label": reliability_label,
        "explanation": "Recommended because it " + ", ".join(reasons) + ".",
    }


def recommend_songs(profile, csv_path="data/songs.csv", top_k=3):
    songs = load_songs(csv_path)

    scored_songs = [score_song(song, profile) for song in songs]
    scored_songs.sort(key=lambda item: item["score"], reverse=True)

    top_results = scored_songs[:top_k]

    weak_results = all(result["confidence"] < 50 for result in top_results)

    return {
        "recommendations": top_results,
        "guardrail_message": (
            "No strong matches found. Showing the closest available songs."
            if weak_results
            else None
        ),
    }
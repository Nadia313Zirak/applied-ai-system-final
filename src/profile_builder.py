VALID_MOODS = ["happy", "chill", "intense", "relaxed"]
VALID_GENRES = ["pop", "lofi", "rock", "ambient", "jazz"]
VALID_ENERGY_LEVELS = ["low", "medium", "high"]
VALID_ACTIVITIES = ["studying", "gym", "relaxing", "driving"]


def energy_to_number(level):
    level = level.lower().strip()

    if level == "low":
        return 0.30
    if level == "medium":
        return 0.60
    if level == "high":
        return 0.90

    return 0.60


def activity_defaults(activity):
    activity = activity.lower().strip()

    defaults = {
        "studying": {
            "energy": 0.35,
            "valence": 0.60,
            "danceability": 0.45,
            "acousticness": 0.80,
        },
        "gym": {
            "energy": 0.90,
            "valence": 0.75,
            "danceability": 0.85,
            "acousticness": 0.20,
        },
        "relaxing": {
            "energy": 0.30,
            "valence": 0.65,
            "danceability": 0.45,
            "acousticness": 0.85,
        },
        "driving": {
            "energy": 0.70,
            "valence": 0.75,
            "danceability": 0.70,
            "acousticness": 0.40,
        },
    }

    return defaults.get(activity, defaults["relaxing"])


def validate_choice(value, valid_options, default_value):
    value = value.lower().strip()

    if value in valid_options:
        return value, None

    warning = f"Invalid input '{value}'. Defaulting to '{default_value}'."
    return default_value, warning


def build_profile(mood, genre, energy_level, activity):
    mood, mood_warning = validate_choice(mood, VALID_MOODS, "relaxed")
    genre, genre_warning = validate_choice(genre, VALID_GENRES, "lofi")
    energy_level, energy_warning = validate_choice(
        energy_level, VALID_ENERGY_LEVELS, "medium"
    )
    activity, activity_warning = validate_choice(activity, VALID_ACTIVITIES, "relaxing")

    defaults = activity_defaults(activity)

    profile = {
        "preferred_mood": mood,
        "preferred_genre": genre,
        "preferred_energy": energy_to_number(energy_level),
        "preferred_valence": defaults["valence"],
        "preferred_danceability": defaults["danceability"],
        "preferred_acousticness": defaults["acousticness"],
        "activity": activity,
    }

    warnings = [
        warning
        for warning in [mood_warning, genre_warning, energy_warning, activity_warning]
        if warning
    ]

    return profile, warnings
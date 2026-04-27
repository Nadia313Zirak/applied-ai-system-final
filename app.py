import streamlit as st
from src.profile_builder import build_profile
from src.recommender import recommend_songs

st.set_page_config(page_title="AI Music Taste Assistant", page_icon="🎧")

st.title("🎧 AI Music Taste Assistant")
st.write(
    "An explainable music recommendation system that suggests songs based on "
    "your mood, genre, energy level, and activity."
)

mood = st.selectbox("Choose your mood", ["happy", "chill", "intense", "relaxed"])
genre = st.selectbox("Choose your genre", ["pop", "lofi", "rock", "ambient", "jazz"])
energy = st.selectbox("Choose your energy level", ["low", "medium", "high"])
activity = st.selectbox("Choose your activity", ["studying", "gym", "relaxing", "driving"])

if st.button("Get Recommendations"):
    profile, warnings = build_profile(mood, genre, energy, activity)
    result = recommend_songs(profile)

    if warnings:
        st.warning("\n".join(warnings))

    if result["guardrail_message"]:
        st.warning(result["guardrail_message"])

    st.subheader("Top Recommendations")

    for item in result["recommendations"]:
        song = item["song"]

        st.markdown(f"### {song['title']} by {song['artist']}")
        st.write(f"**Score:** {item['score']}")
        st.write(f"**Confidence:** {item['confidence']}%")
        st.write(f"**Reliability:** {item['reliability_label']}")
        st.write(f"**Explanation:** {item['explanation']}")
        st.divider()
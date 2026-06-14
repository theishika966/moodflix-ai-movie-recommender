import pandas as pd
import streamlit as st

movies = pd.read_csv("movies.csv")

st.set_page_config(
    page_title="MoodFlix",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
<style>
.movie-card {
    background-color: #1f1f2e;
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #444;
    margin-bottom: 25px;
}
.movie-title {
    color: white;
    font-size: 32px;
    font-weight: bold;
}
.movie-text {
    color: #cccccc;
    font-size: 18px;
}
.badge {
    background-color: #ffcc70;
    color: black;
    padding: 6px 12px;
    border-radius: 20px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title("🎬 MoodFlix")
st.subheader("Find a movie based on your mood")

selected_mood = st.selectbox(
    "How are you feeling today?",
    ["Happy", "Sad", "Romantic", "Motivated"]
)

recommended_movies = movies[movies["mood"] == selected_mood]

st.write(f"## Movies for your mood: {selected_mood}")

for index, movie in recommended_movies.iterrows():
    with st.container():
        st.markdown('<div class="movie-card">', unsafe_allow_html=True)

        col1, col2 = st.columns([1, 4])

        with col1:
            st.image(movie["poster"], width=180)

        with col2:
            st.markdown(f'<div class="movie-title">🎥 {movie["title"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<p class="movie-text">Genre: {movie["genre"]}</p>', unsafe_allow_html=True)
            st.markdown(f'<span class="badge">Mood: {movie["mood"]}</span>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
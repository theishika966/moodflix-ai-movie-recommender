import pandas as pd
import streamlit as st

movies = pd.read_csv("movies.csv")

st.set_page_config(
    page_title="MoodFlix",
    page_icon="🎬",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0f0f0f;
        color: white;
    }

    h1 {
        color: #e50914;
        font-size: 52px;
    }

    h2, h3, p, label {
        color: white !important;
    }

    .movie-card {
        background-color: #1f1f2e;
        padding: 20px;
        border-radius: 18px;
        border: 1px solid #333;
        margin-top: 10px;
        margin-bottom: 25px;
    }

    .genre {
        color: #cccccc !important;
        font-size: 18px;
    }

    .mood {
        color: #ffcc70 !important;
        font-size: 18px;
        font-weight: bold;
    }

    .rating {
        color: #ffd700 !important;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎬 MoodFlix")
st.subheader("Find a movie based on your mood")

selected_mood = st.selectbox(
    "How are you feeling today?",
    ["Happy", "Sad", "Romantic", "Motivated"]
)

recommended_movies = movies[movies["mood"] == selected_mood]

st.write(f"## Movies for your mood: {selected_mood}")

for index, movie in recommended_movies.iterrows():

    col1, col2 = st.columns([1, 3])

    with col1:
        st.image(movie["poster"], width=190)

    with col2:
        st.markdown(
            f"""
            <div class="movie-card">
                <h2>🎥 {movie['title']}</h2>
                <p class="genre">Genre: {movie['genre']}</p>
                <p class="mood">Mood: {movie['mood']}</p>
                <p class="rating">⭐ Rating: {movie['rating']}/10</p>
            </div>
            """,
            unsafe_allow_html=True
        )
import pandas as pd
import streamlit as st

movies = pd.read_csv("movies.csv")

st.set_page_config(page_title="MoodFlix", page_icon="🎬")

st.title("🎬 MoodFlix")
st.subheader("Find a movie based on your mood")

selected_mood = st.selectbox(
    "How are you feeling today?",
    ["Happy", "Sad", "Romantic", "Motivated"]
)

recommended_movies = movies[movies["mood"] == selected_mood]

st.write(f"### Movies for your mood: {selected_mood}")

for index, movie in recommended_movies.iterrows():
    st.markdown(
        f"""
        <div style="
            background-color:#1f1f2e;
            padding:20px;
            border-radius:15px;
            margin-bottom:15px;
            border:1px solid #444;
        ">
            <h3 style="color:white;">🎥 {movie['title']}</h3>
            <p style="color:#cccccc;">Genre: {movie['genre']}</p>
            <p style="color:#ffcc70;">Mood: {movie['mood']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
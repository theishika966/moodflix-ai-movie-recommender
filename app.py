import pandas as pd
import streamlit as st

# Load movie dataset
movies = pd.read_csv("movies.csv")

# Page settings
st.set_page_config(
    page_title="MoodFlix",
    page_icon="🎬",
    layout="wide"
)

# Header
st.title("🎬 MoodFlix")
st.subheader("Find a movie based on your mood")

# Mood selector
selected_mood = st.selectbox(
    "How are you feeling today?",
    ["Happy", "Sad", "Romantic", "Motivated"]
)

# Filter movies
recommended_movies = movies[movies["mood"] == selected_mood]

st.write(f"## Movies for your mood: {selected_mood}")

# Display movie cards
for index, movie in recommended_movies.iterrows():

    with st.container():

        col1, col2 = st.columns([1, 3])

        with col1:
            st.image(movie["poster"], width=180)

        with col2:
            st.markdown(
                f"""
                <div style="
                    background-color:#1f1f2e;
                    padding:20px;
                    border-radius:15px;
                    border:1px solid #444;
                    margin-top:10px;
                ">
                    <h2 style="color:white;">🎥 {movie['title']}</h2>
                    <p style="color:#cccccc;font-size:18px;">
                        Genre: {movie['genre']}
                    </p>
                    <p style="color:#ffcc70;font-size:18px;">
                        Mood: {movie['mood']}
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.write("")
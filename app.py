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
        font-size: 56px;
        font-weight: 800;
    }

    h2, h3, p, label {
        color: white !important;
    }

    .subtitle {
        color: #cccccc;
        font-size: 20px;
        margin-bottom: 30px;
    }

    .movie-card {
        background-color: #1a1a1a;
        padding: 20px;
        border-radius: 18px;
        border: 1px solid #333;
        margin-bottom: 25px;
    }

    .movie-title {
        font-size: 30px;
        font-weight: 700;
        color: white;
    }

    .genre {
        color: #bbbbbb !important;
        font-size: 18px;
    }

    .rating {
        color: #ffd700 !important;
        font-size: 18px;
        font-weight: bold;
    }

    .mood-badge {
        background-color: #e50914;
        color: white;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 15px;
        font-weight: bold;
        display: inline-block;
        margin-top: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if "favorites" not in st.session_state:
    st.session_state.favorites = []

with st.sidebar:
    st.title("🎬 MoodFlix")
    st.write("Your mood-based movie space")

    selected_mood = st.selectbox(
        "Choose your mood",
        ["Happy", "Sad", "Romantic", "Motivated"]
    )

    st.write("---")
    st.subheader("❤️ Favorites")

    if st.session_state.favorites:
        for fav in st.session_state.favorites:
            st.write(f"❤️ {fav}")
    else:
        st.write("No favorites yet.")

st.title("MoodFlix")
st.markdown(
    '<p class="subtitle">Discover movies based on how you feel today.</p>',
    unsafe_allow_html=True
)

recommended_movies = movies[movies["mood"] == selected_mood]

st.write(f"## {selected_mood} Recommendations")

for index, movie in recommended_movies.iterrows():

    with st.container():
        col1, col2 = st.columns([1, 3])

        with col1:
            st.image(movie["poster"], width=190)

        with col2:
            st.markdown(
                f"""
                <div class="movie-card">
                    <div class="movie-title">🎥 {movie['title']}</div>
                    <p class="genre">Genre: {movie['genre']}</p>
                    <p class="rating">⭐ Rating: {movie['rating']}/10</p>
                    <span class="mood-badge">{movie['mood']}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button("❤️ Add to Favorites", key=f"fav_{movie['title']}"):
                if movie["title"] not in st.session_state.favorites:
                    st.session_state.favorites.append(movie["title"])
                    st.success(f"{movie['title']} added to favorites!")
                else:
                    st.info(f"{movie['title']} is already in favorites.")

st.write("---")
st.caption("Built with Python, Streamlit, and Pandas")
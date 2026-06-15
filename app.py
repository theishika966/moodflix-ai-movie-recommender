import pandas as pd
import streamlit as st

movies = pd.read_csv("movies.csv")

st.set_page_config(
    page_title="MoodFlix",
    page_icon="🎬",
    layout="wide"
)

if "favorites" not in st.session_state:
    st.session_state.favorites = []

st.markdown("""
<style>

.stApp{
    background:#0b0b0b;
}

h1{
    color:#E50914;
    font-size:56px;
    font-weight:800;
}

.movie-card{
    background:#181818;
    border:1px solid #333;
    border-radius:18px;
    padding:25px;
    margin-top:20px;
    margin-bottom:20px;
}

.movie-title{
    color:white;
    font-size:30px;
    font-weight:bold;
}

.movie-detail{
    color:#d0d0d0;
    font-size:18px;
}

.rating{
    color:gold;
    font-size:20px;
    font-weight:bold;
}

.mood-pill{
    background:#E50914;
    color:white;
    padding:6px 14px;
    border-radius:20px;
    font-size:14px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------

with st.sidebar:

    st.title("🎬 MoodFlix")

    selected_mood = st.selectbox(
        "Choose Mood",
        ["Happy","Sad","Romantic","Motivated"]
    )

    genre_options = ["All"] + sorted(
        movies["genre"].unique().tolist()
    )

    selected_genre = st.selectbox(
        "Choose Genre",
        genre_options
    )

    sort_by_rating = st.checkbox(
        "Highest Rated First"
    )

    st.divider()

    st.subheader("❤️ Favorites")

    if st.session_state.favorites:

        for movie in st.session_state.favorites:

            st.write(f"❤️ {movie}")

    else:

        st.write("No favorites yet")

# ---------- HEADER ----------

st.title("🎬 MoodFlix")

st.write(
    "Discover movies based on how you feel today."
)

# ---------- FILTER ----------

recommended_movies = movies[
    movies["mood"] == selected_mood
]

if selected_genre != "All":

    recommended_movies = recommended_movies[
        recommended_movies["genre"] == selected_genre
    ]

if sort_by_rating:

    recommended_movies = recommended_movies.sort_values(
        by="rating",
        ascending=False
    )

st.write(
    f"## {selected_mood} Recommendations"
)

# ---------- MOVIES ----------

for _, movie in recommended_movies.iterrows():

    poster_col, card_col = st.columns([1,2])

    with poster_col:

        st.image(
            movie["poster"],
            width=180
        )

    with card_col:

        st.markdown(
            f"""
            <div class="movie-card">

            <div class="movie-title">
            🎥 {movie['title']}
            </div>

            <br>

            <div class="movie-detail">
            🎭 Genre: {movie['genre']}
            </div>

            <br>

            <div class="rating">
            ⭐ {movie['rating']}/10
            </div>

            <br>

            <span class="mood-pill">
            {movie['mood']}
            </span>

            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "❤️ Favorite",
            key=f"fav_{movie['title']}"
        ):

            if movie["title"] not in st.session_state.favorites:

                st.session_state.favorites.append(
                    movie["title"]
                )

                st.success(
                    f"{movie['title']} added!"
                )

            else:

                st.info(
                    "Already in favorites"
                )

    st.divider()

st.caption(
    "Built with Python • Streamlit • Pandas"
)
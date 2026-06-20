import pandas as pd
import streamlit as st

movies = pd.read_csv("backend/movies.csv")

st.set_page_config(
    page_title="MoodFlix",
    page_icon="🎬",
    layout="wide"
)

if "watchlist" not in st.session_state:
    st.session_state.watchlist = []

if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

if "hero_movie" not in st.session_state:
    st.session_state.hero_movie = movies.sample(1).iloc[0]["title"]


def open_details(title):
    st.session_state.selected_movie = title
    st.rerun()


def show_details(title):
    movie = movies[movies["title"] == title].iloc[0]

    if st.button("⬅ Back to Home"):
        st.session_state.selected_movie = None
        st.rerun()

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(movie["poster"], width=320)

    with col2:
        st.title(movie["title"])
        st.write(f"⭐ **{movie['rating']}/10**")
        st.write(f"**Genre:** {movie['genre']}")
        st.write(f"**Mood:** {movie['mood']}")
        st.write(f"**Year:** {movie['release_year']}")
        st.write(f"**Runtime:** {movie['runtime']}")
        st.write(movie["description"])

    st.write("---")
    st.write("## More Like This")

    similar = movies[
        (movies["title"] != movie["title"]) &
        (
            (movies["genre"] == movie["genre"]) |
            (movies["mood"] == movie["mood"])
        )
    ].head(4)

    show_movie_row(similar, "similar")


def show_movie_row(data, key_prefix):
    cols = st.columns(4)

    for index, (_, movie) in enumerate(data.head(4).iterrows()):
        with cols[index]:
            st.image(movie["poster"], width=160)
            st.write(f"**{movie['title']}**")
            st.write(f"⭐ {movie['rating']}/10")

            if st.button("View Details", key=f"{key_prefix}_{movie['title']}"):
                open_details(movie["title"])


st.markdown("""
<style>
.stApp {
    background-color: #0b0b0b;
    color: white;
}

h1 {
    color: #e50914;
    font-size: 60px;
    font-weight: 900;
}

h2, h3, p {
    color: white;
}

.hero-box {
    background: linear-gradient(90deg, #111111, #1f1f1f);
    padding: 35px;
    border-radius: 24px;
    border: 1px solid #333;
}

.hero-title {
    color: white;
    font-size: 46px;
    font-weight: 900;
}

.hero-text {
    color: #cccccc;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)


if st.session_state.selected_movie:
    show_details(st.session_state.selected_movie)

else:
    st.title("🎬 MoodFlix")

    hero = movies[movies["title"] == st.session_state.hero_movie].iloc[0]

    poster_col, info_col = st.columns([1, 2])

    with poster_col:
        st.image(hero["poster"], width=300)

    with info_col:
        st.markdown(
            f"""
            <div class="hero-box">
                <div class="hero-title">{hero['title']}</div>
                <br>
                <div class="hero-text">⭐ {hero['rating']}/10</div>
                <div class="hero-text">{hero['release_year']} • {hero['runtime']} • {hero['genre']}</div>
                <br>
                <div class="hero-text">{hero['description']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:
            if st.button("▶ View Details"):
                open_details(hero["title"])

        with col2:
            if st.button("🔄 New Hero"):
                st.session_state.hero_movie = movies.sample(1).iloc[0]["title"]
                st.rerun()

    st.write("---")

    st.write("## 🔥 Trending Now")
    show_movie_row(movies.sort_values(by="rating", ascending=False), "trending")

    st.write("## 😊 Happy Picks")
    show_movie_row(movies[movies["mood"] == "Happy"], "happy")

    st.write("## 💕 Romantic Picks")
    show_movie_row(movies[movies["mood"] == "Romantic"], "romantic")

    st.write("## 🚀 Motivated Picks")
    show_movie_row(movies[movies["mood"] == "Motivated"], "motivated")

    st.write("## 😢 Emotional Picks")
    show_movie_row(movies[movies["mood"] == "Sad"], "sad")

    st.caption("Built with Python • Streamlit • Pandas")
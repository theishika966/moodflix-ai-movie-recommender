# 🎬 MoodFlix

MoodFlix is a mood-based movie recommendation web app built with Python and Streamlit.

Users can select or describe their mood, and the app recommends movies based on mood, genre, rating, and keywords.

## Features

- Mood-based movie recommendations
- AI-style mood detector
- Movie search
- Genre filter
- Sort by highest rating
- Official movie posters
- Favorites list
- Watchlist
- Dark Netflix-style UI

## Tech Stack

- Python
- Streamlit
- Pandas
- CSV Dataset
- GitHub
- Jira

## How It Works

1. User selects a mood or types how they feel.
2. The app detects or uses the selected mood.
3. Movie data is filtered from `movies.csv`.
4. Matching movies are displayed with posters, genre, rating, and mood.

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py

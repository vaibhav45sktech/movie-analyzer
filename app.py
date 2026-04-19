import streamlit as st
import pandas as pd
from analysis import load_data, get_summary, top_movies, filter_by_rating, movies_by_year

st.set_page_config(page_title="Movie Analyzer", layout="wide")
st.title("🎬 TMDB Movie Analyzer")

# Load data
df = load_data()

# --- Summary Cards ---
st.subheader("📊 Dataset Summary")
summary = get_summary(df)
cols = st.columns(5)
for col, (key, val) in zip(cols, summary.items()):
    col.metric(key, val)

st.divider()

# --- Top Rated Movies ---
st.subheader("⭐ Top 10 Rated Movies")
st.dataframe(top_movies(df), use_container_width=True)

st.divider()

# --- Filter by Rating ---
st.subheader("🔍 Filter Movies by Rating")
min_r, max_r = st.slider("Select Rating Range", 0.0, 10.0, (7.0, 10.0), 0.1)
filtered = filter_by_rating(df, min_r, max_r)
st.write(f"Found **{len(filtered)}** movies")
st.dataframe(filtered[["title", "vote_average", "popularity",
                        "budget", "revenue", "release_year"]],
             use_container_width=True)

st.divider()

# --- Movies per Year Chart ---
st.subheader("📅 Movies Released Per Year")
year_data = movies_by_year(df)
st.bar_chart(year_data.set_index("release_year"))

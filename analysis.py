import pandas as pd
import numpy as np

def load_data():
    df = pd.read_csv("tmdb_5000_movies.csv")
    df = df[["title", "genres", "budget", "revenue",
             "vote_average", "popularity", "release_date", "runtime"]]
    df = df.dropna()
    df = df[df["budget"] > 0]
    df = df[df["revenue"] > 0]
    df["release_year"] = pd.to_datetime(df["release_date"]).dt.year
    return df

def get_summary(df):
    return {
        "Total Movies"    : len(df),
        "Avg Rating"      : round(np.mean(df["vote_average"]), 2),
        "Avg Budget ($M)" : round(np.mean(df["budget"]) / 1e6, 2),
        "Avg Revenue ($M)": round(np.mean(df["revenue"]) / 1e6, 2),
        "Avg Runtime (min)": round(np.mean(df["runtime"]), 2),
    }

def top_movies(df, n=10):
    return df.sort_values("vote_average", ascending=False)[
        ["title", "vote_average", "popularity", "release_year"]
    ].head(n)

def filter_by_rating(df, min_rating, max_rating):
    return df[(df["vote_average"] >= min_rating) &
              (df["vote_average"] <= max_rating)]

def movies_by_year(df):
    return df.groupby("release_year").size().reset_index(name="count")
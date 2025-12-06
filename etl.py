import pandas as pd
import requests
import sqlite3
import time

API_KEY = "772937f9"

conn = sqlite3.connect("movies.db")
cur = conn.cursor()

movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

def fetch(title):
    try:
        r=requests.get(f"http://www.omdbapi.com/?apikey={API_KEY}&t={title}").json()
        if r.get("Response")=="True":
            return r.get("Director"), r.get("Plot"), r.get("BoxOffice")
    except:
        pass
    return None, None, None

movies["year"]=movies["title"].str.extract(r"(\d{4})").astype(float)
movies["clean_title"]=movies["title"].str.replace(r"\(\d{4}\)","",regex=True).str.strip()

directors=[]; plots=[]; boxes=[]
for t in movies["clean_title"]:
    d,p,b = fetch(t)
    directors.append(d); plots.append(p); boxes.append(b)
    time.sleep(0.2)

movies["director"]=directors; movies["plot"]=plots; movies["box_office"]=boxes

conn.execute("PRAGMA foreign_keys = OFF;")
conn.execute("DELETE FROM movies")
conn.execute("DELETE FROM ratings")

movies_to_insert = movies[["movieId","clean_title","year","genres","director","plot","box_office"]].rename(
    columns={"clean_title": "title"}
)

movies_to_insert.to_sql("movies", conn, if_exists="append", index=False)
ratings.to_sql("ratings", conn, if_exists="append", index=False)

print("Done")
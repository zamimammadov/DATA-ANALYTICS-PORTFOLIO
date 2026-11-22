"""Local movie recommendations with optional TMDB enrichment."""
import csv
from functools import lru_cache
import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, render_template, request
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from sentiment import fit_model, labelled_reviews

BASE = Path(__file__).resolve().parent
load_dotenv(BASE / ".env")
app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 64 * 1024


def title_key(title):
    return " ".join(title.split()).casefold()


with (BASE / "main_data.csv").open(encoding="utf-8", newline="") as source:
    films = list(csv.DictReader(source))
title_index = {}
for index, film in enumerate(films):
    title_index.setdefault(title_key(film["movie_title"]), index)
features = CountVectorizer().fit_transform(film["comb"] for film in films)
titles = sorted(films[i]["movie_title"].title() for i in title_index.values())


def recommendations(title, top_n=10):
    key = title_key(title)
    if key not in title_index:
        return []
    scores = cosine_similarity(features[title_index[key]], features).ravel()
    result = []
    seen = {key}
    for candidate in (-scores).argsort(kind="stable"):
        name = films[candidate]["movie_title"]
        other = title_key(name)
        if other not in seen:
            result.append(name)
            seen.add(other)
        if len(result) >= top_n:
            break
    return result


@lru_cache(maxsize=1)
def review_model():
    return fit_model(*labelled_reviews())


def tmdb_get(endpoint, **params):
    key = os.getenv("TMDB_KEY")
    if not key:
        return {}
    try:
        response = requests.get(
            "https://api.themoviedb.org/3/" + endpoint,
            params={"api_key": key, "language": "en-US", **params}, timeout=(2, 3),
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return {}


def movie_details(title):
    key = title_key(title)
    for match in tmdb_get("search/movie", query=title).get("results", []):
        if any(title_key(match.get(field) or "") == key for field in ("title", "original_title")):
            return tmdb_get(f"movie/{match['id']}", append_to_response="credits,reviews")
    return {}


@app.get("/")
@app.get("/home")
def home():
    return render_template("home.html", suggestions=titles)


@app.post("/similarity")
def similarity_route():
    names = recommendations(request.form.get("name", ""))
    return "---".join(names) if names else "Sorry! The movie you requested is not in our database."


@app.route("/recommend", methods=["GET", "POST"])
def recommend():
    supplied = request.values.get("title", "")
    index = title_index.get(title_key(supplied))
    if index is None:
        return render_template("home.html", suggestions=titles, missing=True, searched=supplied), 404
    film = films[index]
    title = film["movie_title"].title()
    details = movie_details(title)
    snippets = [r["content"] for r in details.get("reviews", {}).get("results", []) if r.get("content")][:5]
    user_review = request.form.get("review", "").strip()[:3000]
    if user_review:
        snippets.insert(0, user_review)
    predictions = zip(snippets, review_model().predict(snippets)) if snippets else []
    return render_template(
        "recommend.html", film=film, title=title, related=recommendations(title, 5),
        details=details, suggestions=titles, predictions=predictions, user_review=user_review,
        tmdb_enabled=bool(os.getenv("TMDB_KEY")),
    )


@app.get("/cast/<int:person_id>")
def cast_member(person_id):
    person = tmdb_get(f"person/{person_id}")
    return render_template("cast.html", person=person, suggestions=titles), 200 if person else 404


if __name__ == "__main__":
    app.run()

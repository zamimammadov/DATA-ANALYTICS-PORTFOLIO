# NextOnNetflix

A Flask coursework project for exploring two questions about films: which titles have similar genres and people, and how does a classifier label a short English review? Search a title from the catalogue to get five recommendations. The local catalogue and sentiment model work offline after installation.

## Run the app

From this project folder, use Python 3.11 or 3.12 in a virtual environment.

```console
python -m pip install -r requirements.txt
python main.py
```

Open <http://127.0.0.1:5000> and search for **The Matrix**. The first three suggestions in the supplied catalogue are *The Matrix Revolutions*, *The Matrix Reloaded* and *Jupiter Ascending*. The app builds a sparse count matrix from cast, director and genre text, then scores the selected film against the catalogue using cosine similarity. Suggestions exclude duplicate titles and the title that was searched.

The catalogue has 6,010 rows and 5,975 distinct titles after normalising case and whitespace. Remakes with identical titles share one search entry. The source reflects historical film metadata and does not indicate Netflix streaming availability.

## Review sentiment

On the film page, enter a short English review to obtain the classifier's positive or negative label. The training file contains 6,918 labelled rows. Removing repeated review texts leaves 1,238 examples, of which 696 are positive. The app fits a TF-IDF and logistic regression pipeline on these examples the first time a review is classified.

```console
python sentiment.py
python -m unittest discover -s tests -v
```

The evaluation holds out 248 distinct reviews using a reproducible, stratified split and fits the vocabulary only on the other 990. Accuracy was 95.6% on that holdout. The dataset is small and carries no verified source or sampling documentation; the score measures performance on this particular collection. The app tests cover offline search, classification and the optional service with mocked responses.

## Optional TMDB details

To display posters, plot summaries, cast pages and available TMDB reviews, copy the **.env.example** file to **.env** in this folder and set `TMDB_KEY` to your own TMDB v3 API key. Restart the app after changing the file. Requests for information about the searched title are made by the Flask server. If the service is unavailable, local recommendations and review classification remain available. [TMDB API documentation](https://developer.themoviedb.org/docs/getting-started)

## Data and coursework

- [main_data.csv](main_data.csv) contains the catalogue used by the application. [reviews.csv](reviews.csv) contains the sentiment labels.
- The [preparation notebooks](notebooks) record the original catalogue-building work. Stages 1–4 cover the IMDb 5000 Movie Dataset, The Movies Dataset, Wikipedia film lists and TMDB lookups. The intermediate catalogue snapshots are included. Rebuilding these stages requires external source files or services; the app reads the supplied final snapshot. [IMDb 5000 Movie Dataset](https://www.kaggle.com/datasets/carolzhangdc/imdb-5000-movie-dataset) · [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)
- The final notebook compares the coursework Naive Bayes model with the app's logistic regression on the same split.

# Falcon 9 first-stage landing outcomes

IBM Applied Data Science Capstone coursework on historical launches. The analysis asks whether a classifier trained on earlier flights can predict the recorded landing outcome on later flights. The [original course presentation](Winning%20Space%20Race%20with%20Data%20Science.pdf) documents the earlier analysis. The executable evaluation below uses a chronological split.

## Result

Of 90 labelled launches from June 2010 through November 2020, the first 72 are used for training and the last 18 for evaluation. Three expanding training splits select among logistic regression, a support vector machine, a decision tree and nearest neighbours using balanced accuracy. Scaling and categorical encoding are fitted within each training fold.

| Final 18 launches | Correct predictions | Class 0 correctly identified | Balanced accuracy |
|---|---:|---:|---:|
| Decision tree | 16 of 18 | 1 of 3 | 66.7% |
| Training-set majority baseline | 15 of 18 | 0 of 3 | 50.0% |

One flight accounts for the accuracy difference. Class 0 includes failed landings, missing outcomes and launches with no recorded attempt. The comparison therefore cannot establish the probability of failure on an attempted landing. The model excludes the recorded landing outcome, target column, and the booster’s later cumulative reuse count from its predictors.

## Run

From this folder, use Python 3.11 or 3.12 and install the project dependencies.

```console
python -m pip install -r requirements.txt
python evaluate.py
python dashboard.py
```

Open the address printed by Dash. The dashboard uses a separate 56-launch geographical extract from the course. Filter by site and payload to see how many observations support each comparison.

## Notebooks and source data

```console
python -m pip install -r requirements-notebooks.txt
python -m jupyter lab
```

Open the numbered notebooks from this folder. They cover API collection, historical HTML tables, label construction, SQL exploration, plots, geography and model evaluation. The collection notebooks read the bundled snapshots by default. Optional remote refreshes depend on the upstream sites; map tiles also use the network.

The [course extracts](data/) have different populations. The model uses the 90-row labelled file, SQL exploration uses the 101-row launch history, and the map and dashboard use the 56-row geographical extract. The web-scraping worksheet retains its separate 106-row table. The stored feature matrix is retained as a coursework output; the evaluation builds its own features from the labelled launches.

[IBM Applied Data Science Capstone](https://www.coursera.org/learn/applied-data-science-capstone) · [SpaceX API](https://github.com/r-spacex/SpaceX-API) · [Wikipedia revision used in the collection exercise](https://en.wikipedia.org/w/index.php?title=List_of_Falcon_9_and_Falcon_Heavy_launches&oldid=1027686922)

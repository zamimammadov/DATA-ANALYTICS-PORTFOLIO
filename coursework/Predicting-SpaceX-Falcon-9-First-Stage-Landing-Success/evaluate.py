"""Retrospective, chronological evaluation of the capstone's four classifiers."""
from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, balanced_accuracy_score, confusion_matrix
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

DATA = Path(__file__).parent / "data" / "dataset_part_2.csv"
NUMERIC = ["Flights", "GridFins", "Reused", "Legs"]
CATEGORICAL = ["Orbit", "LaunchSite"]


def evaluate(data):
    ordered = data.sort_values(["Date", "FlightNumber"])
    X, y = ordered[NUMERIC + CATEGORICAL], ordered["Class"]
    cutoff = int(0.8 * len(ordered))
    X_train, X_test = X.iloc[:cutoff], X.iloc[cutoff:]
    y_train, y_test = y.iloc[:cutoff], y.iloc[cutoff:]
    features = ColumnTransformer([
        ("numeric", StandardScaler(), NUMERIC),
        ("category", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL),
    ])
    models = [
        ("Logistic regression", LogisticRegression(max_iter=1000), {"model__C": [0.1, 1, 10]}),
        ("SVM", SVC(), {"model__C": [0.1, 1, 10], "model__kernel": ["linear", "rbf"]}),
        ("Decision tree", DecisionTreeClassifier(random_state=42), {"model__max_depth": [2, 4, None]}),
        ("KNN", KNeighborsClassifier(), {"model__n_neighbors": [3, 5, 7]}),
    ]
    searches = {}
    for name, estimator, grid in models:
        pipeline = Pipeline([("prepare", features), ("model", estimator)])
        search = GridSearchCV(pipeline, grid, cv=TimeSeriesSplit(n_splits=3), scoring="balanced_accuracy")
        searches[name] = search.fit(X_train, y_train)
    selected = max(searches, key=lambda name: searches[name].best_score_)
    baseline = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)
    results = []
    for name, classifier in [(selected, searches[selected]), ("Majority baseline", baseline)]:
        prediction = classifier.predict(X_test)
        tn, fp, fn, tp = confusion_matrix(y_test, prediction, labels=[0, 1]).ravel()
        results.append({"model": name, "accuracy": accuracy_score(y_test, prediction),
                        "balanced_accuracy": balanced_accuracy_score(y_test, prediction),
                        "tn": tn, "fp": fp, "fn": fn, "tp": tp})
    scores = pd.Series({name: s.best_score_ for name, s in searches.items()},
                       name="training_cv_balanced_accuracy").sort_values(ascending=False)
    return scores, pd.DataFrame(results).set_index("model")


if __name__ == "__main__":
    scores, results = evaluate(pd.read_csv(DATA))
    print(scores.round(3).to_string())
    print(results.round(3).to_string())

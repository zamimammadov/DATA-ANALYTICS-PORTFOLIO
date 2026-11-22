"""Train and evaluate review sentiment on distinct labelled texts."""
import csv
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline


def labelled_reviews():
    examples = {}
    with Path(__file__).with_name("reviews.csv").open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            text = " ".join(row["review"].split()).casefold()
            label = row["sentiment"]
            if not text or label not in {"positive", "negative"}:
                raise ValueError("Empty text or invalid sentiment label in reviews.csv")
            if text in examples and examples[text] != label:
                raise ValueError("Identical review text has conflicting labels")
            examples[text] = label
    return list(examples), list(examples.values())


def fit_model(texts, labels):
    model = make_pipeline(TfidfVectorizer(stop_words="english"), LogisticRegression(max_iter=1000))
    return model.fit(texts, labels)


if __name__ == "__main__":
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import classification_report

    texts, labels = labelled_reviews()
    train, test, y_train, y_test = train_test_split(
        texts, labels, test_size=0.2, stratify=labels, random_state=42
    )
    model = fit_model(train, y_train)
    print(f"{len(texts)} distinct reviews; {len(train)} training, {len(test)} held out")
    print(classification_report(y_test, model.predict(test), digits=3))

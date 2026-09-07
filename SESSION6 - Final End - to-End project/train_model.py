# Q - 1

"""
1.  Train a machine learning model to predict whether a Flipkart product review is positive or
    negative using a sample dataset, and save the trained model as review_sentiment_model.pkl.
"""


import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Sample Flipkart-style review dataset
data = {
    "review": [
        "The product is excellent and very good quality",
        "Amazing product, I really love it",
        "Very good product and fast delivery",
        "Excellent quality, totally worth the money",
        "I am very happy with this product",
        "The product is awesome",
        "Good quality and nice packaging",
        "Very useful product, highly recommended",
        "Fantastic product, I loved it",
        "Best product at this price",

        "Very bad product",
        "Worst product I have ever purchased",
        "Poor quality and damaged product",
        "I am very disappointed",
        "Product stopped working after one day",
        "Waste of money",
        "Bad quality product",
        "I do not recommend this product",
        "Very poor packaging and quality",
        "The product is terrible"
    ],

    "sentiment": [
        "Positive",
        "Positive",
        "Positive",
        "Positive",
        "Positive",
        "Positive",
        "Positive",
        "Positive",
        "Positive",
        "Positive",

        "Negative",
        "Negative",
        "Negative",
        "Negative",
        "Negative",
        "Negative",
        "Negative",
        "Negative",
        "Negative",
        "Negative"
    ]
}


# Create DataFrame
df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nDataset size:", len(df))


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    df["review"],
    df["sentiment"],
    test_size=0.2,
    random_state=42
)


# Create ML pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression())
])


# Train model
model.fit(X_train, y_train)


# Test model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", accuracy)


# Save trained model
with open("review_sentiment_model.pkl", "wb") as file:
    pickle.dump(model, file)


print("\nModel saved successfully!")
print("File: review_sentiment_model.pkl")
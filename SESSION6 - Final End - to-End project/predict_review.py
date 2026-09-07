
# Q - 2

"""
2.  Build a Flask-based prediction API (predict_review.py) that loads your saved 
    review_sentiment_model.pkl and returns 'Positive' or 'Negative' for a given review text 
    sent via POST request.<br><br><em><strong>Hint:</strong> Use Flask's request.get_json() 
    to read the input review from the API call.</em>
"""


from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Load trained ML model
with open("review_sentiment_model.pkl", "rb") as file:
    model = pickle.load(file)


# Home API
@app.route("/")
def home():
    return send_from_directory(".", "review_predictor.html")


# Prediction API
@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    review = data.get("review", "")

    if not review:
        return jsonify({
            "error": "Please enter a review"
        }), 400

    prediction = model.predict([review])[0]

    return jsonify({
        "review": review,
        "prediction": prediction
    })


if __name__ == "__main__":
    app.run(debug=True)
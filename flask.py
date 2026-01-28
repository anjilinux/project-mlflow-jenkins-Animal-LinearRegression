from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("models/model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["features"]
    prediction = model.predict([data])
    return jsonify({"prediction": prediction.tolist()})

app.run(host="0.0.0.0", port=5001)

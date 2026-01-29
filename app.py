from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "UP"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    payload = request.get_json()
    features = np.array(payload["features"]).reshape(1, -1)
    prediction = model.predict(features)

    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

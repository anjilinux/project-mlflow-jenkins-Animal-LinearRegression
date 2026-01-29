from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model (make sure path is correct)
model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    payload = request.get_json()

    features = payload["features"]
    features = np.array(features).reshape(1, -1)

    prediction = model.predict(features)

    return jsonify({
        "prediction": prediction.tolist()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

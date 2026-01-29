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











# from flask import Flask, request, jsonify
# import joblib
# import numpy as np

# app = Flask(__name__)

# # Load model (make sure path is correct)
# model = joblib.load("model.pkl")

# @app.route("/predict", methods=["POST"])
# def predict():
#     payload = request.get_json()

#     features = payload["features"]
#     features = np.array(features).reshape(1, -1)

#     prediction = model.predict(features)

#     return jsonify({
#         "prediction": prediction.tolist()
#     })

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5001)




#################  output===
# (base) bny@bny:~/git-flow/project-3$ curl -X POST http://localhost:5001/predict \
#      -H "Content-Type: application/json" \
#      -d '{"features":[120,22.5,1100,0.78]}'


#        {"prediction":[340.2775138756957]}
    


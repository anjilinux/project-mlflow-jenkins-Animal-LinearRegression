import joblib
import numpy as np

def test_model_prediction():
    model = joblib.load("models/model.pkl")
    sample = np.array([[100, 25, 300, 0.8]])
    pred = model.predict(sample)

    assert pred is not None

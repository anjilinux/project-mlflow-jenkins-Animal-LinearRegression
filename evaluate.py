import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score

model = joblib.load("models/model.pkl")
data = pd.read_csv("data/processed/clean_data.csv")

X = data.drop("target", axis=1)
y = data["target"]

predictions = model.predict(X)

mse = mean_squared_error(y, predictions)
r2 = r2_score(y, predictions)

print("MSE:", mse)
print("R2 Score:", r2)

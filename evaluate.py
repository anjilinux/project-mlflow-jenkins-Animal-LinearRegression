import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score

# Load model
model = joblib.load("models/model.pkl")

# Load data
data = pd.read_csv("clean_data.csv")
data.columns = data.columns.str.strip()

TARGET_COL = "animal_population"

# Validate
if TARGET_COL not in data.columns:
    raise ValueError(f"❌ '{TARGET_COL}' column not found in clean_data.csv")

X = data.drop(TARGET_COL, axis=1)
y = data[TARGET_COL]

# Predict
predictions = model.predict(X)

# Metrics
mse = mean_squared_error(y, predictions)
r2 = r2_score(y, predictions)

print("MSE:", mse)
print("R2 Score:", r2)

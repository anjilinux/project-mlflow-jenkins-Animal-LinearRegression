import os
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Load data
data = pd.read_csv("clean_data.csv")
data.columns = data.columns.str.strip()

print("Columns:", list(data.columns))

TARGET_COL = "animal_population"

# Validate target
if TARGET_COL not in data.columns:
    raise ValueError(f"❌ '{TARGET_COL}' column not found in clean_data.csv")

X = data.drop(TARGET_COL, axis=1)
y = data[TARGET_COL]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Ensure model directory exists
os.makedirs("models", exist_ok=True)

mlflow.set_experiment("animal_population_linear_regression_22")
mlflow.set_tracking_uri("http://localhost:5555")
# Train + MLflow tracking
with mlflow.start_run():
    model = LinearRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, "models/model.pkl")

    mlflow.log_param("model_type", "LinearRegression")
    mlflow.log_param("target_column", TARGET_COL)
    mlflow.log_param("num_features", X.shape[1])

    mlflow.sklearn.log_model(model, "model")
    mlflow.log_artifact("models/model.pkl")



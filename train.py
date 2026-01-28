import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

data = pd.read_csv("clean_data.csv")

X = data.drop("target", axis=1)
y = data["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

with mlflow.start_run():
    model = LinearRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, "models/model.pkl")

    mlflow.log_param("model_type", "LinearRegression")
    mlflow.sklearn.log_model(model, "model")
    mlflow.log_artifact("models/model.pkl")

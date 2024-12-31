import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def prepare_data(file_path):
    data = pd.read_csv(file_path)
    data = pd.get_dummies(data, drop_first=True)
    X = data.drop("Target", axis=1)
    y = data["Target"]
    return train_test_split(X, y, test_size=0.2, random_state=42)

def build_models(X_train, X_test, y_train, y_test):
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor()
    }
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        results[name] = mse
    return results

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = prepare_data("data/processed/processed_data.csv")
    results = build_models(X_train, X_test, y_train, y_test)
    print("Model Evaluation Results:")
    for model, mse in results.items():
        print(f"{model}: MSE = {mse}")

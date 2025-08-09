# evaluate_model.py

import numpy as np
import sys

from utils.load_csv import load_csv
from utils.load_model import load_model


def evaluate_model(
    x: np.ndarray,
    y: np.ndarray,
    theta0: float,
    theta1: float,
):
    """Evaluate regression model."""

    print("\n===== MODEL EVALUATION =====")
    y_pred = theta0 + (theta1 * x)

    # Lower is better
    mse = np.mean((y - y_pred) ** 2)
    print(f"Mean Squared Error (MSE): {mse:.4f}")

    # Lower is better
    rmse = np.sqrt(mse)
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")

    # Lower is better
    mae = np.mean(np.abs(y - y_pred))
    print(f"Mean Absolute Error (MAE): {mae:.4f}")

    # R-squared (coefficient of determination)
    # Higher is better
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    print(f"R-squared (R²): {r2:.4f}")


def main():
    """Evaluate linear model using the params."""
    if len(sys.argv) != 2:
        print("Usage: python evaluate_model.py <model_file>")
        sys.exit(1)

    model_file = sys.argv[1]

    # Load data
    FILE = "data/data.csv"
    data = load_csv(FILE)
    if data is None:
        return

    # Get data
    mileage = data["km"].values.astype(float)
    price = data["price"].values.astype(float)

    # Load model parameters
    theta0, theta1 = load_model(model_file)
    print("Loaded model parameters:")
    print(f"theta0 = {theta0:.4f}, theta1 = {theta1:.4f}")

    # Evaluate model
    evaluate_model(mileage, price, theta0, theta1)


if __name__ == "__main__":
    main()

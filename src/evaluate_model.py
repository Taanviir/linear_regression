# evaluate_model.py

import numpy as np

from load_csv import load


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


def load_model() -> tuple[float, float]:
    """
    Load theta0 and theta1 from 'model.npy' file.
    Return default values (0,0) if file is missing or invalid.
    """
    try:
        params = np.load("model.npy")
        if len(params) != 2:
            raise ValueError("Model parameter array length is not 2.")
        return float(params[0]), float(params[1])

    except (FileNotFoundError, ValueError) as e:
        print(f"Error: Failed to load model. {e}")
        print("Setting theta0 and theta1 to defaults.\n")
        return 0.0, 0.0


def main():
    """Evaluate linear model."""

    # Load model parameters
    theta0, theta1 = load_model()
    print("Loaded model parameters:")
    print(f"theta0 = {theta0:.4f}, theta1 = {theta1:.4f}")

    # Load data
    file = "data/data.csv"
    data = load(file)
    if data is None:
        return

    # Get data
    mileage = data["km"].values.astype(float)
    price = data["price"].values.astype(float)

    # Evaluate model
    evaluate_model(mileage, price, theta0, theta1)


if __name__ == "__main__":
    main()

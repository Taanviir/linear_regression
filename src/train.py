# train.py

import numpy as np

from utils.load_csv import load_csv
from utils.plot import plot_graph


MODEL_FILE = "model.npy"


def compute_gradients(
    x: np.ndarray, y: np.ndarray, theta0: float, theta1: float
) -> tuple[float, float]:
    """
    Compute partial derivatives of the cost function with respect
    to theta1 and theta0.
    """

    m = len(x)
    predictions = theta0 + (theta1 * x)
    errors = predictions - y

    grad_theta1 = np.dot(errors, x) / m
    grad_theta0 = np.mean(errors)

    return grad_theta1, grad_theta0


def gradient_descent(
    x: np.ndarray,
    y: np.ndarray,
    learning_rate: float = 0.001,
    iterations: int = 10_000,
) -> tuple[float | float]:
    """
    Perform gradient descent to find optimal theta0 and theta1.
    """

    theta0 = 0.0
    theta1 = 0.0

    for _ in range(iterations):
        grad_theta1, grad_theta0 = compute_gradients(x, y, theta0, theta1)
        theta1 -= learning_rate * grad_theta1
        theta0 -= learning_rate * grad_theta0

    return theta0, theta1


def train_model(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Train linear regression model."""

    tmp_th0, tmp_th1 = gradient_descent(normalize(x), normalize(y))

    y_std = y.std()
    y_mean = y.mean()
    x_std = x.std()
    x_mean = x.mean()

    theta0 = y_mean + y_std * tmp_th0 - (y_std * tmp_th1 * x_mean) / x_std
    theta1 = (y_std * tmp_th1) / x_std

    print("Trained model with parameters:")
    print(f"theta0 = {theta0}")
    print(f"theta1 = {theta1}")

    return np.array([theta0, theta1])


def normalize(data: np.ndarray) -> np.ndarray:
    """Return normalized data (mean = 0, std = 1)."""
    return (data - data.mean()) / data.std()


def main():
    """Train linear model and save params to MODEL_FILE."""

    FILE = "data/data.csv"
    data = load_csv(FILE)
    if data is None:
        return

    mileage = data["km"].values.astype(float)
    price = data["price"].values.astype(float)

    params = train_model(mileage, price)
    np.save(MODEL_FILE, params)

    plot_graph(mileage, price, *params)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("KeyboardInterrupt received, closing program...")

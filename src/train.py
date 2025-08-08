# train.py

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from load_csv import load


def plot_graph(mileage, price, theta0, theta1):
    """Plot scatter points and regression line."""

    plt.scatter(mileage, price, marker="x", label="Data Points")

    regression_line = theta0 + (theta1 * mileage)
    plt.plot(mileage, regression_line, c="red", label="Regression Line")

    plt.xlabel("Mileage (normalized)")
    plt.ylabel("Price (normalized)")
    plt.legend()
    plt.tight_layout()

    if mpl.get_backend().lower() == "agg":  # Headless mode
        out_png = "figure.png"
        plt.savefig(out_png)
        print(f"Headless mode detected. Plot saved to '{out_png}'.")
    else:
        plt.show()


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
):
    """
    Perform gradient descent to find optimal theta0 and theta1.
    """

    theta0 = 0.0
    theta1 = 0.0

    for _ in range(iterations):
        grad_theta1, grad_theta0 = compute_gradients(x, y, theta0, theta1)
        theta1 -= learning_rate * grad_theta1
        theta0 -= learning_rate * grad_theta0

    return np.array([theta0, theta1])


def train_model(mileage: np.ndarray, price: np.ndarray) -> np.ndarray:
    """
    Train linear regression model:
    estimatePrice(mileage) = theta0 + (theta1 * mileage)
    """

    params = gradient_descent(mileage, price)
    theta0, theta1 = params

    print("Trained model with parameters:")
    print(f"theta0 = {theta0}")
    print(f"theta1 = {theta1}")

    return params


def normalize(data: np.ndarray) -> np.ndarray:
    """Return normalized data (mean = 0, std = 1)."""
    return (data - data.mean()) / data.std()


def main() -> None:
    """Train linear model."""

    file = "data/data.csv"
    data = load(file)
    if data is None:
        return

    mileage = normalize(data["km"].values.astype(float))
    price = normalize(data["price"].values.astype(float))

    params = train_model(mileage, price)
    np.save("model.npy", params)

    plot_graph(mileage, price, *params)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("KeyboardInterrupt received, closing program...")

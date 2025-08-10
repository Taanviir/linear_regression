# plot.py

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def plot_regression_line(
    x: np.ndarray, plt_module: plt, theta0: float, theta1: float
) -> None:
    """Plot the linear regression model."""

    regression_line = theta0 + (theta1 * x)
    plt_module.plot(x, regression_line, c="red", label="Regression Line")


def plot_graph(
    x: np.ndarray,
    y: np.ndarray,
    theta0: float,
    theta1: float,
    save_path: str | None = None,
) -> None:
    """Plot scatter points and regression line."""

    plt.scatter(x, y, marker="x", label="Data Points")

    plot_regression_line(x, plt, theta0, theta1)

    plt.xlabel("Mileage (in kms)")
    plt.ylabel("Price (in $)")
    plt.legend()
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
        print(f"Plot saved to '{save_path}'.")

    if mpl.get_backend().lower() != "agg":
        plt.show()

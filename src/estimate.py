# estimate.py

import numpy as np


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


def estimate_price(mileage: float, theta0: float, theta1: float) -> float:
    """Estimate the price using formula: price = theta0 + theta1 * mileage"""

    print("price = theta0 + theta1 * mileage")
    print(f"\033[94mprice = {theta0} + {theta1} * {mileage}\033[0m")

    return theta0 + theta1 * mileage


def main():
    """Estimate the price of a car based on mileage using a linear model."""

    theta0, theta1 = load_model()

    try:
        mileage = float(input("Enter the mileage of the car (in km): "))
    except ValueError:
        print("Error: Invalid input for mileage.")
        return

    print()
    price = estimate_price(mileage, theta0, theta1)
    print(f"Estimated price for a car with {mileage} km: ", end="")
    print(f"\033[92m${price:.2f}\033[0m")


if __name__ == "__main__":
    main()

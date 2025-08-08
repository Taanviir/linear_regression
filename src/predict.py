# predict.py

import json
from json import JSONDecodeError


def load_model() -> tuple[int | float, int | float]:
    """
    Load theta0 and theta1 from model.json file.
    Return default values if file is missing or invalid.
    """

    try:
        with open("model.json", "r") as file:
            params = json.load(file)
            return params.get("theta0", 0), params.get("theta1", 0)

    except (FileNotFoundError, JSONDecodeError):
        print("Error: Failed to load model.")
        print("Setting theta0 and theta1 to defaults.\n")
        return 0, 0


def estimate_price(mileage: float, theta0: float, theta1: float) -> float:
    """Estimate the price using formula: price = theta0 + theta1 * mileage"""

    print("price = theta0 + theta1 * mileage")
    print(f"\033[94mprice = {theta0} + {theta1} * {mileage}\033[0m")

    return theta0 + theta1 * mileage


def main():
    """Estimate the price of a car based on mileage using a linear model."""

    theta0, theta1 = load_model()

    try:
        mileage = int(input("Enter the mileage of the car (in km): "))

    except ValueError:
        print("Error: Invalid type entered.")
        return

    print()
    price = estimate_price(mileage, theta0, theta1)
    print(f"Estimated price for a car with {mileage} km: ", end="")
    print(f"\033[92m${price:.2f}\033[0m")


if __name__ == "__main__":
    main()

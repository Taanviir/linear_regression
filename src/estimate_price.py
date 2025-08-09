# estimate.py

from utils.load_model import load_model


MODEL_FILE = "model.npy"


def estimate_price(mileage: float, theta0: float, theta1: float) -> float:
    """Estimate the price using formula: price = theta0 + theta1 * mileage"""

    print("price = theta0 + theta1 * mileage")
    print(f"\033[94mprice = {theta0} + {theta1} * {mileage}\033[0m")

    return theta0 + theta1 * mileage


def main():
    """Estimate the price of a car based on mileage using a linear model."""

    theta0, theta1 = load_model(MODEL_FILE)

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

# train.py

from utils import estimate_price
from json import load, JSONDecodeError


def main():
    """Estimate the price of a car based on mileage using a trained linear model."""

    try:
        with open("model.json") as file:
            params = load(file)
            theta0 = params.get("theta0", 0)
            theta1 = params.get("theta1", 0)
    except JSONDecodeError:
        print("Error: invalid json file.")
        return
    except FileNotFoundError:
        print("No `model.json` file found. Setting theta0 & theta1 to 0 and 0.")

    try:
        mileage = int(input("Enter the mileage of the car (in km): "))
    except ValueError:
        print("Error: Invalid type entered.")
        return

    price = estimate_price(mileage, theta0, theta1)
    print(f"Estimated price for a car with {mileage} km: ${price:.2f}")


if __name__ == "__main__":
    main()

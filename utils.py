# utils.py


def estimate_price(mileage: int | float) -> float:
    theta0 = 0
    theta1 = 0

    price = theta0 + (theta1 * mileage)
    return price

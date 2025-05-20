# utils.py


def estimate_price(
    mileage: int | float, theta0: int | float, theta1: int | float
) -> float:
    return theta0 + (theta1 * mileage)

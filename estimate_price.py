# estimate_price.py


def estimate_price(mileage: int | float) -> float:
    theta0 = 0
    theta1 = 0

    price = theta0 + (theta1 * mileage)
    return price


def main():
    try:
        mileage = int(input("Enter the mileage to estimate price for: "))
    except ValueError:
        print("Error: Invalid Type entered.")
        return

    estimate_price(mileage)


if __name__ == "__main__":
    main()

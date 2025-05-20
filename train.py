# train.py

from utils import estimate_price


def main():
    try:
        mileage = int(input("Enter the mileage to estimate price for: "))
    except ValueError:
        print("Error: Invalid Type entered.")
        return

    price = estimate_price(mileage)


if __name__ == "__main__":
    main()

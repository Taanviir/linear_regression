# predict.py

import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def ft_linear_regression() -> dict:
    """ """

    theta0 = 0
    theta1 = 0

    # get data
    data = pd.read_csv("data.csv")
    print(data)

    # perform linear regression on data
    mileage = data["km"]
    price = data["price"]

    m = len(mileage)

    f = np.zeros(m)
    for i in range(m):
        f[i] = theta0 + theta1 * mileage[i]

    # plt.plot(mileage, f, c="red")
    plt.scatter(mileage, price, marker="x")
    plt.xlabel("Mileage (in km)")
    plt.ylabel("Price (in $)")
    plt.tight_layout()
    plt.savefig("figure.jpg")

    return {"theta0": theta0, "theta1": theta1}


def main():
    params = ft_linear_regression()

    # with open("model.json", "w") as file:
    #     json.dump(params, file, indent=4)


if __name__ == "__main__":
    main()

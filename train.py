# predict.py

import pandas as pd
import json


def ft_linear_regression() -> dict:
    """ """

    theta0 = 0
    theta1 = 0

    # get data
    data = pd.read_csv("data.csv")
    print(data)

    # perform linear regression

    # save theta0 and theta1 to model.json

    return {"theta0": theta0, "theta1": theta1}


def main():
    params = ft_linear_regression()

    with open("model.json", "w") as file:
        json.dump(params, file, indent=4)


if __name__ == "__main__":
    main()

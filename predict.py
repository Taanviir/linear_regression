# predict.py

import pandas as pd


def ft_linear_regression():

    data = pd.read_csv("data.csv")
    print(data)


def main():
    ft_linear_regression()


if __name__ == "__main__":
    main()

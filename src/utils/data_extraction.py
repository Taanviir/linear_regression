# utils/data_extraction.py

import numpy as np

from .load_csv import load_csv


def extract_mileage_and_price(
    file_path: str,
) -> tuple[np.ndarray, np.ndarray] | None:
    """Extract mileage and price data from CSV file."""

    data = load_csv(file_path)
    if data is None:
        return None

    try:
        # Remove rows with missing values
        data = data.dropna()
        mileage = data["km"].values.astype(float)
        price = data["price"].values.astype(float)
        return mileage, price
    except ValueError:
        print(f"Error: invalid data found in '{file_path}'.")
        return None

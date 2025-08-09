# utils/data_extraction.py

import numpy as np
from .load_csv import load_csv

MILEAGE_COLUMN = "km"
PRICE_COLUMN = "price"


def filter_negative_pairs(
    mileage: np.ndarray, price: np.ndarray, file_path: str
) -> tuple[np.ndarray, np.ndarray] | None:
    """Filter out rows where values are negative, preserving alignment."""

    mask = (mileage >= 0) & (price >= 0)

    if not np.all(mask):
        print(
            f"Warning: Negative values found in '{file_path}'. "
            "These will be filtered out."
        )

    mileage = mileage[mask]
    price = price[mask]

    if len(mileage) == 0 or len(price) == 0:
        print(f"Error: No valid data found in '{file_path}' after filtering.")
        return None

    return mileage, price


def extract_mileage_and_price(
    file_path: str,
) -> tuple[np.ndarray, np.ndarray] | None:
    """Extract mileage and price data from CSV file."""

    df = load_csv(file_path)
    if df is None or df.empty:
        print(f"Error: No data found in '{file_path}'.")
        return None

    # Remove rows with missing values
    df = df.dropna()
    if df.empty:
        print(f"Error: No valid data found in '{file_path}'.")
        return None

    # Check required columns
    for col in (MILEAGE_COLUMN, PRICE_COLUMN):
        if col not in df.columns:
            print(f"Error: Column '{col}' not found in '{file_path}'.")
            return None
        if df[col].empty:
            print(f"Error: No data found in '{col}' column of '{file_path}'.")
            return None

    # Convert to float arrays
    try:
        mileage = df[MILEAGE_COLUMN].values.astype(float)
        price = df[PRICE_COLUMN].values.astype(float)
    except ValueError as e:
        print(f"Error: Invalid data found in '{file_path}': {e}")
        return None

    # Filter negative values, keeping mileage-price pairs aligned
    result = filter_negative_pairs(mileage, price, file_path)
    if result is None:
        return None
    mileage, price = result

    # Final length check (should be safe now)
    if len(mileage) != len(price):
        print(f"Error: Mismatch in data lengths in '{file_path}'.")
        return None

    return mileage, price

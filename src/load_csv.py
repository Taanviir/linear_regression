# ex00: load_csv.py

import pandas as pd
from pandas import DataFrame


def load(path: str) -> DataFrame | None:
    """
    Loads the given CSV file path as a pandas DataFrame.

    Parameters:
        path (str): The path to the CSV file.

    Returns:
        DataFrame: The resulting DataFrame from the file,
                   or None in case of error.
    """

    if not path.lower().endswith(".csv"):
        print(f"Error: Invalid file entered: '{path}'.")
        return None

    if path.strip().split("/")[-1].startswith("."):
        print(f"Error: File '{path}' appears to be a hidden or system file.")
        return None

    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at path '{path}'.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file at '{path}' is empty.")
    except pd.errors.ParserError as e:
        print(f"Error: Failed to parse the CSV file at '{path}': {e}")
    except PermissionError:
        print(f"Error: Permission denied while accessing '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred while loading the CSV: {e}")

    return None

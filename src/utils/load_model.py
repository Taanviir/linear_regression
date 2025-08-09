# load_model.py

import numpy as np


def load_model(model_file) -> tuple[float, float]:
    """
    Load theta0 and theta1 from 'model.npy' file.
    Return default values (0,0) if file is missing or invalid.
    """
    try:
        params = np.load(model_file)
        if len(params) != 2:
            raise ValueError("Model parameter array length is not 2.")
        return float(params[0]), float(params[1])

    except (FileNotFoundError, ValueError) as e:
        print(f"Error: Failed to load model. {e}")
        print("Setting theta0 and theta1 to defaults.\n")
        return 0.0, 0.0

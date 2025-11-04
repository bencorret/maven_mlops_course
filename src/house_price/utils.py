"""Utility class."""

import numpy as np
import os


def adjust_predictions(predictions: np.ndarray, scale_factor: float = 1.3) -> np.ndarray:
    """Adjust predictions by multiplying them with a scale factor.

    :param predictions: Array of predictions to be adjusted
    :param scale_factor: Factor to scale the predictions by
    :return: Adjusted predictions array
    """
    return [round(pred * scale_factor, 2) for pred in predictions]

def is_databricks() -> bool:
    """
    Check whether the code is running in Databricks runtime.
    
    Returns:
        bool: True if running in Databricks runtime, False otherwise.
    """
    # Primary check: Databricks runtime version
    if "DATABRICKS_RUNTIME_VERSION" in os.environ:
        return True
import os


def is_databricks() -> bool:
    """
    Check whether the code is running in Databricks runtime.
    
    Returns:
        bool: True if running in Databricks runtime, False otherwise.
    """
    # Primary check: Databricks runtime version
    if "DATABRICKS_RUNTIME_VERSION" in os.environ:
        return True
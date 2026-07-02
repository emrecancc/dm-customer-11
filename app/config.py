import json


def load_config(path):
    """Load a JSON configuration file.

    Parameters
    ----------
    path : str
        Path to the configuration file.

    Returns
    -------
    dict
        Parsed configuration data.
    """
    with open(path, 'r') as f:
        return json.load(f)

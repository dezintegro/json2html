import json


def load_data(data_source):
    """Loads JSON data from the specified file.

    Args:
        data_source: File from which data should to be loaded.

    Returns:
        list: If data in source file wrapped in list.
        dict: In other cases.

    """

    with open(data_source) as data_source:
        return json.load(data_source)

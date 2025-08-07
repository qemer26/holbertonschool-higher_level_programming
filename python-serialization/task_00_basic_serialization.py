import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Parameters:
    data (dict): The dictionary to serialize.
    filename (str): The filename of the output JSON file.
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file into a Python dictionary.

    Parameters:
    filename (str): The filename of the input JSON file.

    Returns:
    dict: The deserialized dictionary from the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)


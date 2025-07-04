#!/usr/bin/python3
"""
This module contains the function save_to_json_file that writes an object
to a text file using its JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)

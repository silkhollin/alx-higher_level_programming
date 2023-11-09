#!/usr/bin/python3
""" an object from json"""

def load_from_json_file(filename):
    """ function for creating an object from json """

    with open(filename) as f:
        return json.load(f)

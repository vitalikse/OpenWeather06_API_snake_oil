import json
import os


def read_from_json_file(path):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'jsons', path)
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"No such JSON file: {file_path}")
    else:
        return data

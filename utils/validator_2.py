import requests
import json
from os.path import join, dirname
import jsonschema
from jsonschema import Draft202012Validator

# End points
BASE_PAGE = 'https://reqres.in'
SINGLE_USER = '/api/users/2'
LIST_USERS = '/api/users?page=2'


def validator(data, schema_file):
    """ Checks whether the given data matches the schema """
    if _load_json_schema(schema_file):
        schema = _load_json_schema(schema_file)
        try:
            Draft202012Validator.check_schema(schema)
            return Draft202012Validator(schema).is_valid(data)
        except jsonschema.exceptions.SchemaError as e:
            print("JSON Schema is incorrect:", e)


def _load_json_schema(filename):
    """ Loads the given schema file """

    relative_path = join('schemas', filename)
    absolute_path = join(dirname(__file__), relative_path)
    try:
        with open(absolute_path) as schema_file:
            try:
                return json.loads(schema_file.read())
            except json.decoder.JSONDecodeError:
                print(f"JSON file has incorrect data: {relative_path}")
    except FileNotFoundError:
        print(f"No such JSON schema file: {relative_path}")
        return False


response = requests.get(f'{BASE_PAGE}{SINGLE_USER}')
print(response.json())
json_data = response.json()
print(validator(json_data, 'st.json'))

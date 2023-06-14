import requests
import json
import jsonschema
from jsonschema import Draft202012Validator
from utils.schemas.schemas import SINGLE_USER_SCHEMA, SCHEMA, SCHEMA_LIST

BASE_PAGE = 'https://reqres.in'
SINGLE_USER = '/api/users/2'
LIST_USERS = '/api/users?page=2'


def validator(data, schema):
    try:
        jsonschema.validate(instance=data, schema=schema)
        print('Validation successful.')
    except jsonschema.exceptions.ValidationError as e:
        print('Validation failed.')
        print(e)


Draft202012Validator.check_schema(SINGLE_USER_SCHEMA)

new_validator = Draft202012Validator(SINGLE_USER_SCHEMA)
# new_validator.is_valid()

response = requests.get(f'{BASE_PAGE}{SINGLE_USER}')
print(response.json())
json_data = response.json()
# validator(json_data, SINGLE_USER_SCHEMA)

# response = requests.get(f'{BASE_PAGE}{LIST_USERS}')
# print(response.json())
# json_data = response.json()
# validator(json_data, SCHEMA_LIST)

# validator(requests.get(f'{BASE_PAGE}{SINGLE_USER}').json(), SINGLE_USER_SCHEMA)
# validator(requests.get(f'{BASE_PAGE}{LIST_USERS}').json(), SCHEMA_LIST)
# validator(requests.get(f'{BASE_PAGE}{LIST_USERS}').json(), SCHEMA)
print(new_validator.is_valid(json_data))

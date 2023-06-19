import pytest
import requests
from data.endpoints import EndPoints as ep
from utils.file_handler import read_from_json_file
from utils.validator_jsonschema import validator_jsonschema


@pytest.mark.positive
class TestsSchemaPositive:
    """Positive tests with correct JSON data from endpoint and correct schema"""

    def test_single_user(self):
        response = requests.get(f'{ep.BASE_PAGE}{ep.SINGLE_USER}')
        json_data = response.json()
        assert validator_jsonschema(json_data, 'single_user.json'), 'API response is incorrect'

    def test_list_users(self):
        response = requests.get(f'{ep.BASE_PAGE}{ep.LIST_USERS}')
        json_data = response.json()
        assert validator_jsonschema(json_data, 'list_users.json'), 'API response is incorrect'


@pytest.mark.positive_json
class TestsSchemaPositiveJSON:
    """Positive tests with correct JSON data from file and correct schema"""

    def test_single_user(self):
        json_data = read_from_json_file('single_user.json')
        assert validator_jsonschema(json_data, 'single_user.json'), 'API response is incorrect'

    def test_list_users(self):
        json_data = read_from_json_file('list_users.json')
        assert validator_jsonschema(json_data, 'list_users.json'), 'API response is incorrect'


@pytest.mark.negative_schema
class TestsSchemaNegativeSchema:
    """Negative tests with correct JSON data from endpoint and incorrect schema"""

    def test_single_user(self):
        response = requests.get(f'{ep.BASE_PAGE}{ep.SINGLE_USER}')
        json_data = response.json()
        assert validator_jsonschema(json_data, 'single_user_broken.json'), 'API response is incorrect'

    def test_list_users(self):
        response = requests.get(f'{ep.BASE_PAGE}{ep.LIST_USERS}')
        json_data = response.json()
        assert validator_jsonschema(json_data, 'list_users_broken.json'), 'API response is incorrect'


@pytest.mark.negative_json
class TestsSchemaNegativeJSON:
    """Negative tests with incorrect JSON data from file and correct schema"""

    def test_single_user(self):
        json_data = read_from_json_file('single_user_broken.json')  # line 3, email is a number instead a string
        assert validator_jsonschema(json_data, 'single_user.json'), 'API response is incorrect'

    def test_list_users(self):
        json_data = read_from_json_file('list_users_broken.json')  # line 16, email is a number instead a string
        assert validator_jsonschema(json_data, 'list_users.json'), 'API response is incorrect'

import pytest
import requests

from utils.file_handler import read_from_json_file
from utils.validator_pydantic import validator_pydantic
from utils.models.models import Models as m
from data.endpoints import EndPoints as ep


@pytest.mark.positive
class TestsPydanticPositive:
    """Positive tests with correct JSON data from endpoint and correct model"""

    def test_single_user(self):
        response = requests.get(f'{ep.BASE_PAGE}{ep.SINGLE_USER}')
        assert validator_pydantic(response.json(), m.SingleUser.Model), 'API response is incorrect'

    def test_list_users(self):
        response = requests.get(f'{ep.BASE_PAGE}{ep.LIST_USERS}')
        assert validator_pydantic(response.json(), m.ListUsers.Model), 'API response is incorrect'


@pytest.mark.positive_json
class TestsPydanticPositiveJSON:
    """Positive tests with correct JSON data from file and correct model"""

    def test_single_user(self):
        json_data = read_from_json_file('single_user.json')
        assert validator_pydantic(json_data, m.SingleUser.Model), 'API response is incorrect'

    def test_list_users(self):
        json_data = read_from_json_file('list_users.json')
        assert validator_pydantic(json_data, m.ListUsers.Model), 'API response is incorrect'


@pytest.mark.negative_model
class TestsPydanticNegativeModel:
    """Negative tests with correct JSON data from endpoint and incorrect model"""

    def test_single_user(self):
        response = requests.get(f'{ep.BASE_PAGE}{ep.SINGLE_USER}')
        assert validator_pydantic(response.json(), m.SingleUserBroken.Model), 'API response is incorrect'

    def test_list_users(self):
        response = requests.get(f'{ep.BASE_PAGE}{ep.LIST_USERS}')
        assert validator_pydantic(response.json(), m.ListUsersBroken.Model), 'API response is incorrect'


@pytest.mark.negative_json
class TestsPydanticNegativeJSON:
    """Negative tests with incorrect JSON data from file and correct model"""

    def test_single_user(self):
        json_data = read_from_json_file('single_user_broken.json')
        assert validator_pydantic(json_data, m.SingleUser.Model), 'API response is incorrect'

    def test_list_users(self):
        json_data = read_from_json_file('list_users_broken.json')
        assert validator_pydantic(json_data, m.ListUsers.Model), 'API response is incorrect'

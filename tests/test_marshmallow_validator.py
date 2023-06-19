import pytest
import requests
from utils.models.marshmallow_models import ModelSingleUser
from utils.validator_marshmallow import validator_marshmallow
from data.endpoints import EndPoints as ep


@pytest.mark.positive
class TestsMarshmallowPositive:
    """Positive tests with correct JSON data from endpoint and correct model"""

    def test_single_user(self):
        response = requests.get(f'{ep.BASE_PAGE}{ep.SINGLE_USER}')
        json_data = response.json()
        assert validator_marshmallow(json_data, ModelSingleUser), 'API response is incorrect'

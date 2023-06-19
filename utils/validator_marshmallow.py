import json


def validator_marshmallow(data, model):
    schema = model()
    validated_data = schema.load(json.loads(json.dumps(data)))
    return validated_data

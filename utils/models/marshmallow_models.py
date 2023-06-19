"""This file contains models for JSON marshmallow validation"""
from marshmallow import Schema, fields, validate


class DataSingleUser(Schema):
    id = fields.Int(required=True, allow_none=False)
    email = fields.Email(required=True, allow_none=False)
    first_name = fields.Str(required=True, allow_none=False)
    last_name = fields.Str(required=True, allow_none=False)
    avatar = fields.URL(required=True, allow_none=False)


class SupportSingleUser(Schema):
    url = fields.URL(required=True, allow_none=False)
    text = fields.Str(required=True, allow_none=False)


class ModelSingleUser(Schema):
    data_schema = DataSingleUser()
    data = fields.Nested(data_schema)
    support_schema = SupportSingleUser()
    support = fields.Nested(support_schema)

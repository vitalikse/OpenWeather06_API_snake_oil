SINGLE_USER_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "title": "Single user Schema",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "email": {
                    "type": "string"
                },
                "first_name": {
                    "type": "string"
                },
                "last_name": {
                    "type": "string"
                },
                "avatar": {
                    "type": "string"
                }
            },
            "required": [
                "id",
                "email",
                "first_name",
                "last_name",
                "avatar"
            ],
            "additionalProperties": False
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string"
                },
                "text": {
                    "type": "string"
                }
            },
            "required": [
                "url",
                "text"
            ],
            "additionalProperties": False
        }
    },
    "required": [
        "data",
        "support"
    ],
    "additionalProperties": False
}

SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "page": {
            "type": "integer"
        },
        "per_page": {
            "type": "integer"
        },
        "total": {
            "type": "integer"
        },
        "total_pages": {
            "type": "integer"
        },
        "data": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "email": {
                            "type": "string"
                        },
                        "first_name": {
                            "type": "string"
                        },
                        "last_name": {
                            "type": "string"
                        },
                        "avatar": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "email",
                        "first_name",
                        "last_name",
                        "avatar"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "email": {
                            "type": "string"
                        },
                        "first_name": {
                            "type": "string"
                        },
                        "last_name": {
                            "type": "string"
                        },
                        "avatar": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "email",
                        "first_name",
                        "last_name",
                        "avatar"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "email": {
                            "type": "string"
                        },
                        "first_name": {
                            "type": "string"
                        },
                        "last_name": {
                            "type": "string"
                        },
                        "avatar": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "email",
                        "first_name",
                        "last_name",
                        "avatar"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "email": {
                            "type": "string"
                        },
                        "first_name": {
                            "type": "string"
                        },
                        "last_name": {
                            "type": "string"
                        },
                        "avatar": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "email",
                        "first_name",
                        "last_name",
                        "avatar"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "email": {
                            "type": "string"
                        },
                        "first_name": {
                            "type": "string"
                        },
                        "last_name": {
                            "type": "string"
                        },
                        "avatar": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "email",
                        "first_name",
                        "last_name",
                        "avatar"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "email": {
                            "type": "string"
                        },
                        "first_name": {
                            "type": "string"
                        },
                        "last_name": {
                            "type": "string"
                        },
                        "avatar": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "email",
                        "first_name",
                        "last_name",
                        "avatar"
                    ]
                }
            ]
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string"
                },
                "text": {
                    "type": "string"
                }
            },
            "required": [
                "url",
                "text"
            ]
        }
    },
    "required": [
        "page",
        "per_page",
        "total",
        "total_pages",
        "data",
        "support"
    ]
}

SCHEMA_LIST = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "page": {
            "type": "integer"
        },
        "per_page": {
            "type": "integer"
        },
        "total": {
            "type": "integer"
        },
        "total_pages": {
            "type": "integer"
        },
        "data": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "email": {
                            "type": "string"
                        },
                        "first_name": {
                            "type": "string"
                        },
                        "last_name": {
                            "type": "string"
                        },
                        "avatar": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "email",
                        "first_name",
                        "last_name",
                        "avatar"
                    ],
                    "additionalProperties": False
                }
            ]
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string"
                },
                "text": {
                    "type": "string"
                }
            },
            "required": [
                "url",
                "text"
            ],
            "additionalProperties": False
        }
    },
    "required": [
        "page",
        "per_page",
        "total",
        "total_pages",
        "data",
        "support"
    ],
    "additionalProperties": False
}

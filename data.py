class Token :

    token1 = {"Authorization" : "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczNDc2NjE4NywianRpIjoiMGI2ODczNTItMGU3MC00NTJlLWEwMTEtYjdhMmU0NWJkZWI5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluIiwibmJmIjoxNzM0NzY2MTg3LCJleHAiOjE3MzQ3Njk3ODd9.2yoCO1IOb9DsrAsxqEXuOzHuQc253ZAw-5S7dKe1kho"
    }

class Schema :
    schema_get_item = {
  "type": "object",
  "properties": {
    "description": {
      "type": "string"
    },
    "id": {
      "type": "integer"
    },
    "name": {
      "type": "string"
    },
    "quantity": {
      "type": "integer"
    }
  },
  "additionalProperties": False,
  "required": [
    "description",
    "id",
    "name",
    "quantity"
  ]
}

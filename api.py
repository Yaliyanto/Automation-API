import requests
from data import Token, Schema
import json
from jsonschema import validate, ValidationError

base_url = "https://testapi.kelasotomesyen.com"




def get_token():
    body = {"username": "admin", "password": "uHuY12#$"}

    resp = requests.post(base_url + "/login", json=body)
    json_response = json.loads(resp.text)

    return json_response['token']

def test_get_items_by_id():

    getToken = get_token()
    token = {"Authorization":f"Bearer {getToken}"}
    resp = requests.get(base_url+'/items/70',headers= token)

    status_code = resp.status_code
    json_response= json.loads(resp.text)
    id = json_response ['id']
    name = json_response ['name']
    

    assert status_code == 200
    assert id  == 70
    assert name == "Dodol"
    print(json_response)

    try :
        validate(resp.json(),schema=Schema.schema_get_item)

    except ValidationError as e:
        assert False, f'JSON SCHEMA ERROR: {e}'

def test_post_items():


    getToken = get_token()
    token = {"Authorization":f"Bearer {getToken}"}

    body_request = {"name": "yal wick", "description": "Sate Madura", "quantity": 14}

    resp = requests.post(base_url+'/items',headers= token,json=body_request)

    
    status_code = resp.status_code
    json_response = json.loads(resp.text)

    name = json_response ['name']

    assert status_code == 201
    assert name == 'yal wick'

    try :
        validate(resp.json(),schema=Schema.schema_get_item)

    except ValidationError as e:
        assert False, f'JSON SCHEMA ERROR: {e}'

def test_get_items():

    getToken = get_token()
    token = {"Authorization":f"Bearer {getToken}"}
    response = requests.get(base_url+'/items',headers= token)
    status_code = response.status_code
    json_response = json.loads(response.text)

    return json_response

    assert status_code == 201

def test_put_item():


    getToken = get_token()
    token = {"Authorization":f"Bearer {getToken}"}
    body_request = {"name": "Ballerina", "description": "Nasi Goreng", "quantity": 12}
    response = requests.put(base_url + f"/items/{89}", headers= token, json=body_request)
    json_response = json.loads(response.text)
    quantity = json_response ["quantity"]
    status_code = response.status_code

    return json_response
    assert status_code == 201
    assert quantity == '12'


def test_delete_item():

    getToken = get_token()
    token = {"Authorization":f"Bearer {getToken}"}
    response = requests.delete(base_url + f"/items/{61}", headers= token)
    status_code = response.status_code

    return response.status_code
    assert status_code == 200

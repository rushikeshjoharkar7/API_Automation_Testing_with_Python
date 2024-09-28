import pytest
import requests


def test_get_request_validation():
    header = {
        'Content-Type': 'application/json'
    }

    base_url = 'https://reqres.in/'

    response = requests.get(url=base_url+ '/api/users/2', headers=header)
    assert 200 == response.status_code
    print(response.text)
    print(response.json())

test_get_request_validation()
import requests
import pytest
import json

endpoint = "https://reqres.in/api/users/2"


def test_Delete_request():
    response = requests.delete(endpoint)

    assert response.status_code == 204



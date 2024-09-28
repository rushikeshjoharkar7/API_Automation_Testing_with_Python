# requests is a python library which helps to automate the REST API automation.

# The POST method is one of the most commonly used HTTP methods in REST APIs and
# __is used to create a new resource on the server. Unlike the GET method, which is used to
# __retrieve resources, the POST method is used to submit data to the server for processing.

# POST is idempotent which means which does same work again nd again newly.

import requests

header = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json'
}

post_payload = {
    "id": 20,
    "title": "automate_with_rushi",
    "dueDate": "2024-09-23T10:31:02.569Z",
    "completed": True
}

endpoint = "https://fakerestapi.azurewebsites.net/api/v1/Activities"


def test_Post_request():
    response = requests.post(endpoint,
                             json=post_payload,
                             headers=header)
    print(response.status_code, '\n', response.json())
    assert response.status_code == 200

    data = response.json()
    assert data['id'] == 20


test_Post_request()


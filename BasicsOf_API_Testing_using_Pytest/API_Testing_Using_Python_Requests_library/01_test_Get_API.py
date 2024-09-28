import requests

endpoint = "https://fakerestapi.azurewebsites.net/api/v1/Activities"


def test_get_API_endpoint():
    response = requests.get(endpoint)
    assert response.status_code == 200
    print(response.text)
    print(response.status_code)
    print(response.json())


test_get_API_endpoint()

head = {
    'Accept': 'text/plain'
}

endpoint2 = "https://fakerestapi.azurewebsites.net/api/v1/Activities/5"


def test_get_API_endpoint2():
    response2 = requests.get(endpoint2, headers=head)
    assert response2.status_code == 200
    print(response2.text)
    print(response2.status_code)
    print(response2.json())


test_get_API_endpoint2()



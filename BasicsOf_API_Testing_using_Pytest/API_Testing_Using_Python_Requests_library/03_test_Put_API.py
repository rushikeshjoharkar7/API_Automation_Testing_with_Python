# The PUT method is used to update a resource on the server. The resource is
# __identified by a URI and the updated data is sent in the body of the request. PUT requests are
# __typically used to update an existing resource, such as an existing user account or a blog post.

# If any resource on the server is not present in database to update then PUT can create it also. So, PUT is not a
# __ idempotent (idempotent means which does same work again nd again newly)

import requests

header = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json'
}

endpoint = "https://fakerestapi.azurewebsites.net/api/v1/Activities/12"

put_payload = {
  "id": 14,
  "title": "rushi",
  "dueDate": "2024-09-23T11:16:26.327Z",
  "completed": True
}


def test_Put_request():
    responseGet = requests.get(endpoint, headers=header)
    print("before update: ", responseGet.status_code, "\n", responseGet.json())

    responsePut = requests.put(endpoint, headers=header, json=put_payload)
    print("after update: ", responsePut.status_code, "\n", responsePut.json())


test_Put_request()
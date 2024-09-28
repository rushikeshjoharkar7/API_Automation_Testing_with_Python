# API authentication is the process of verifying the identity of the user or application making the
# __request, while API authorization is the process of verifying that the authenticated user or application
# __has permission to access the requested resources.

# A Bearer token is a type of token used for authentication and authorization and is used in web applications
# __and APIs to hold user credentials and indicate authorization for requests and access.

# Bearer Authorization is an HTTP authentication scheme commonly used with OAuth 2.0. In this approach,
# __the client includes an access token in the "Authorization" header using the "Bearer" scheme, granting
# __permission to access protected resources. The server validates the token for authorization.


import requests

url = 'https://gorest.co.in/public/v2/users/'

head = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer a4b521926fe4d9af2af8f77ea1abeceb9c3f75ca79bc87b6a6c8db67c0e09ed6'
}

body = {
    "id": 7416843,
    "name": "raghavan",
    "email": "raghavn_asan@swift.example",
    "gender": "male",
    "status": "inactive"
}


def auth_POST_request():
    response_auth_post = requests.post(url, headers=head, json=body)
    print(response_auth_post.json())
    assert response_auth_post.status_code == 201  # 201 code shows created status

    response_get_req = requests.get(url + '/' + str(response_auth_post.json()['id']), headers=head)
    print(response_get_req.json())


auth_POST_request()

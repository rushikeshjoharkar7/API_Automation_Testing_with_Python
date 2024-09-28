import json

import requests


base_url = 'https://reqres.in/'

header_test = {'Content-type': 'application/json'}

json_file = open('./users.json')
json_payload = json.load(json_file)

# response = requests.post(url=base_url + '/api/users', headers=header_test, json=json_payload) is also one way
# and we can use data replacing json param as shown below.
response = requests.post(url=base_url + '/api/users', headers=header_test, data=json.dumps(json_payload))
print(response.json())
print(response.status_code)
assert response.status_code == 201
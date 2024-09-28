import requests
import uuid

endpoint = "https://todo.pixegami.io"

# user url : "https://todo.pixegami.io/docs#/" for knowing APIs info

def test_can_create_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    data = create_task_response.json()
    assert create_task_response.status_code == 200

    task_id = data['task']['task_id']
    get_created_response = get_task(task_id)
    assert get_created_response.status_code == 200
    assert get_created_response.json()["content"] == payload["content"]
    assert get_created_response.json()["user_id"] == payload["user_id"]

def test_can_update_task():
    # create the task
    # get and validate the changes
    payload = new_task_payload()
    create_task_response = create_task(payload)
    task_id = create_task_response.json()['task']['task_id']

    # update the task
    new_payload = {
        "user_id": payload["user_id"],
        "task_id": task_id,
        "content": "my updated content",
        "is_done": True
    }
    updated_task_response = update_task(new_payload)
    assert updated_task_response.status_code == 200

    # get and validate the changes
    get_updated_task_response = get_task(task_id)
    assert get_updated_task_response.status_code == 200
    get_task_data = get_updated_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["is_done"] == new_payload["is_done"]

def test_can_list_users():
    # create N tasks
    n = 3
    payload = new_task_payload()
    for _ in range(3):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200

    # list tasks and check that there are N items.
    user_id = payload["user_id"]
    list_task_response = list_tasks(user_id)
    assert list_task_response.status_code == 200
    data = list_task_response.json()

    tasks = data["tasks"]
    assert len(tasks) == n

def test_can_delete_task():
    # create the task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()['task']['task_id']

    # delete the task
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200

    # get the task and check that it is not found
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404

def new_task_payload():
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"

    return{
        "content": content,
        "user_id": user_id,
        "task_id": "test_task_id",
        "is_done": False
    }

def create_task(payload):
    return requests.put(endpoint+"/create-task", json=payload)

def update_task(payload):
    return requests.put(endpoint + "/update-task", json=payload)

def get_task(task_id):
    return requests.get(endpoint + f"/get-task/{task_id}")

def list_tasks(user_id):
    return requests.get(endpoint + f"/list-tasks/{user_id}")

def delete_task(task_id):
    return requests.delete(endpoint + f"/delete-task/{task_id}")





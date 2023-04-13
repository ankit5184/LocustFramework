from locust import HttpUser, SequentialTaskSet, task, constant, events
from commonFunctions.readJson import read_json_file
from genricMethods.getRequest import get_request
from genricMethods.postRequest import post_request
from genricMethods.putRequest import put_request
from genricMethods.deleteRequest import delete_request


class post(SequentialTaskSet):

    @task
    def get_user(self):
        status_code, response_body = get_request("/api/users?page=2")
        assert status_code == 200, f"Unexpected status code: {status_code}"
        print(response_body)
        print(status_code)

    @task
    def create_user(self):
        createUserData = read_json_file('testData/jsonFiles/createUser.json')
        # headers = {'Authorization': 'Bearer my_token'}
        status_code, response_body = post_request('/api/users', createUserData)
        assert status_code == 201, f"Unexpected status code: {status_code}"
        print(response_body)
        print(status_code)

    @task
    def user_not_found(self):
        status_code, response_body = get_request('/api/users/23')
        assert status_code == 404, f"Unexpected status code : {status_code}"
        print(response_body)
        print(status_code)

    @task
    def update_user(self):
        updateUserData = read_json_file('testData/jsonFiles/updateUser.json')
        status_code, response_body = put_request('/api/users/2', updateUserData)
        assert status_code == 200, f"Unexpected status code : {status_code}"
        assert response_body["name"] == "Suzuki", f"Unexpected status code : {response_body}"
        print(response_body)
        print(status_code)

    @task
    def delete_user(self):
        status_code, response_body = delete_request('/api/users/2')
        assert status_code == 204, f"Unexpected status code : {status_code}"
        print(response_body)
        print(status_code)


class runtest(HttpUser):
    host = "https://reqres.in"
    wait_time = constant(1)
    tasks = [post]

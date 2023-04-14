from locust import HttpUser, SequentialTaskSet, task, between
from genricMethods.getRequest import get_request
from genricMethods.postRequest import post_request
from commonLib.readJson import read_json_file


class reqres(SequentialTaskSet):

    @task
    def list_resource(self):
        status_code, response_body = get_request("/api/unknown")
        assert status_code == 200, f"Unexpected status code: {status_code}"
        print(response_body)
        print(status_code)

    @task
    def single_resource(self):
        status_code, response_body = get_request("/api/unknown/2")
        assert status_code == 200, f"Unexpected status code: {status_code}"
        print(response_body)
        print(status_code)

    @task
    def resource_not_found(self):
        status_code, response_body = get_request("/api/unknown/23")
        assert status_code == 404, f"Unexpected status code: {status_code}"
        print(response_body)
        print(status_code)

    @task
    def register_succ(self):
        loginData = read_json_file('testData/jsonFiles/loginData.json')
        # headers = {'Authorization': 'Bearer my_token'}
        status_code, response_body = post_request('/api/register', loginData)
        assert status_code == 200, f"Unexpected status code: {status_code}"
        print(response_body)
        print(status_code)


class executeTest(HttpUser):
    host = "https://reqres.in"
    wait_time = between(1, 6)
    tasks = [reqres]

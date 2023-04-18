from locust import HttpUser, constant, task, between
import webbrowser


class MyReqRes(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_users(self):
        res = self.client.get("/api/users?page=2")
        print(res.status_code)

    @task
    def create_user(self):
        res = self.client.post("/api/users", data='''
           {"name": "morpheus","job": "leader"}
           ''')
        print(res.text)
        print(res.status_code)
        print(res.headers)
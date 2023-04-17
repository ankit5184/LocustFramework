from locust import HttpUser, constant, task, between
import webbrowser


class MyReqRes(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_users(self):
        res = self.client.get("/api/users?page=2")
        print(res.status_code)


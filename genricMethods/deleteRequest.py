import requests
import json
from locust import events


def delete_request(url, headers=None):
    if headers is None:
        headers = {}
    full_url = f"https://reqres.in{url}"
    response = requests.delete(full_url, headers=headers)
    try:
        response_body = json.loads(response.text)
    except json.decoder.JSONDecodeError:
        response_body = response.text
    events.request.fire(
        request_type="DELETE",
        name=url,
        response_time=response.elapsed.total_seconds() * 1000,
        response_length=len(response.text),
    )
    return response.status_code, response_body
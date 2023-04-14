import requests
import json
from locust import events


def get_request(url, headers=None, params=None):
    if headers is None:
        headers = {}
    if params is None:
        params = {}
    full_url = f"https://reqres.in{url}"
    response = requests.get(full_url, headers=headers, params=params)
    try:
        response_body = json.loads(response.text)
    except json.decoder.JSONDecodeError:
        response_body = response.text
    events.request.fire(
        request_type="GET",
        name=url,
        response_time=response.elapsed.total_seconds() * 1000,
        response_length=len(response.text),
        response=response,
    )
    return response.status_code, response_body
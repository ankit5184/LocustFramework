import requests
import json
from locust import events

def post_request(url, json_data, headers=None):
    if headers is None:
        headers = {}
    full_url = f"https://reqres.in{url}"
    headers['Content-Type'] = 'application/json'
    response = requests.post(full_url, data=json.dumps(json_data), headers=headers)
    try:
        response_body = json.loads(response.text)
    except json.decoder.JSONDecodeError:
        response_body = response.text
    events.request.fire(
        request_type="POST",
        name=url,
        response_time=response.elapsed.total_seconds() * 1000,
        response_length=len(response.text),
        response=response
    )
    return response.status_code, response_body

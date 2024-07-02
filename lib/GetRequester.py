import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(f"{self.url}")
        return response.content

    def load_json(self):
        json_response = requests.get(f"{self.url}")
        return json_response.json()
import httpx

from config import config


class APIClient:
    def __init__(self):
        self.client = httpx.Client(
            base_url=config.API_BASE_URL,
            timeout=config.API_TIMEOUT
        )

    def set_token(self, token):
        self.client.headers["x-auth-token"] = token

    def get(self, endpoint):
        return self.client.get(endpoint)

    def post(self, endpoint, json):
        return self.client.post(endpoint, json=json)

    def put(self, endpoint, json):
        return self.client.put(endpoint, json=json)

    def patch(self, endpoint, json):
        return self.client.patch(endpoint, json=json)

    def delete(self, endpoint):
        return self.client.delete(endpoint)

    def close(self):
        self.client.close()

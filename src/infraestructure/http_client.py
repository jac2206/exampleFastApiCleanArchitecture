import requests

class HttpClient:
    def __init__(self, base_url: str = None):
        self.base_url = base_url.rstrip("/") if base_url else ""

    def get(self, endpoint: str, params: dict = None, headers: dict = None):
        # url = f"{self.base_url}/{endpoint.lstrip('/')}"
        url = f"{endpoint.lstrip('/')}"
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint: str, data: dict = None, headers: dict = None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()

    def put(self, endpoint: str, data: dict = None, headers: dict = None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.put(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()

    def patch(self, endpoint: str, data: dict = None, headers: dict = None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.patch(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint: str, headers: dict = None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return response.json()

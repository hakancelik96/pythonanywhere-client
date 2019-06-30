# python
import requests

class Client:
    base_uri = "https://www.pythonanywhere.com"

    def __init__(self, username, token):
        self.username = username
        self.headers = dict(
            Authorization=f"Token {token}"
        )

    def _create_api_uri(self, op, name, path, api_version="v0"):
        return f"{self.base_uri}/api/{api_version}/user/{self.username}/{op}/{name}/{path}"

    def _requests(self, method, op, name, path, data=dict()):
        uri = self._create_api_uri(op, name, path)
        return getattr(requests, method)(
            uri,
            timeout=10,
            headers=self.headers,
            data=data
        )

    def _get(self, op, name="", path=""):
        return self._requests("get", op, name, path)

    def _post(self, op, name="", path="", data=dict()):
        return self._requests("post", op, name, path, data)

    def _put(self, op, name="", path="", data=dict()):
        return self._requests("put", op, name, path, data)

    def _patch(self, op, name="", path="", data=dict()):
        return self._requests("patch", op, name, path, data)

    def _delete(self, op, name="", path=""):
        return self._requests("delete", op, name, path)

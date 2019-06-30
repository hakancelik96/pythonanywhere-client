# python
import requests

class Client:

    def __init__(self, username, token):
        self.headers = dict(
            Authorization=f"Token {token}"
        )

    def _get(self):
        return requests.get(
            self.api_uri,
            headers=self.headers
        )

    def _post(self, **kwargs):
        return requests.post(
            self.api_uri,
            headers=self.headers,
            data=kwargs
        )

    def _put(self, **kwargs):
        return requests.put(
            self.api_uri,
            headers=self.headers,
            data=kwargs
        )

    def _patch(self, **kwargs):
        return requests.patch(
            self.api_uri,
            headers=self.headers,
            data=kwargs
        )

    def _delete(self):
        return requests.delete(
            self.api_uri,
            headers=self.headers
        )


if __name__ == "__main__":
    client = Client(
        username="coogger",
        token="cece7010f9ff2c6d0cfd831f25a9c90938ec6698"
    )
    print(client.)

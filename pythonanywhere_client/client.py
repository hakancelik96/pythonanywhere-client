# python
import requests
import re

class Client:
    base_uri = "https://www.pythonanywhere.com"

    def __init__(self, username, token):
        self.username = username
        self.headers = dict(
            Authorization=f"Token {token}"
        )

    def _create_api_uri(self, op, name, path, api_version="v0"):
        return f"{self.base_uri}/api/{api_version}/user/{self.username}/{op}/{name}/{path}"

    def _requests(self, method, op, name, path, data):
        uri = self._create_api_uri(op, name, path)
        return getattr(requests, method)(
            uri,
            timeout=10,
            headers=self.headers,
            data=data
        )

def get_variable(obj, text):
    regex = r"{self\.(.*)}"
    matches = re.finditer(regex, text, re.DOTALL)
    for match in matches:
        return getattr(obj, match.group(1))
    return text

def client_decorator(op, name="", path="", method=None):
    def client_f(func):
        def wraps(*args, **kwargs):
            payload = func(*args, **kwargs)
            obj = args[0]
            name_parameter = get_variable(obj, name)
            return getattr(obj.client, f"_requests")(
                method=method or func.__name__,
                op=op,
                name=name_parameter,
                path=path,
                data=payload or dict()
            )
        return wraps
    return client_f

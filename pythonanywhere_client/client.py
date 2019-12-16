# python
import inspect
import re

import requests


class Client:
    base_uri = "https://www.pythonanywhere.com"

    def __init__(self, username, token):
        self.username = username
        self.headers = dict(Authorization=f"Token {token}")

    def _create_api_uri(self, op, name, path, api_version="v0"):
        return (
            f"{self.base_uri}/api/{api_version}/user/{self.username}/{op}/{name}/{path}"
        )

    def _requests(self, method, op, name, path, data):
        uri = self._create_api_uri(op, name, path)
        return getattr(requests, method)(
            uri, timeout=10, headers=self.headers, data=data
        )


def get_variable(obj, text):
    regex = r"{self\.(.*)}"
    matches = re.finditer(regex, text, re.DOTALL)
    for match in matches:
        match_text = text[match.span()[0] : match.span()[1]]
        remove_match_text = text.replace(match_text, "")
        variable = str(getattr(obj, match.group(1)))
        return remove_match_text + variable
    return text


def client_decorator(op, name="", path="", method=None):
    def client_f(func):
        def wraps(*args, **kwargs):
            get_parameters = inspect.getcallargs(func, *args, **kwargs)
            obj = get_parameters["self"]
            del get_parameters["self"]
            print(get_variable(obj, path))
            return getattr(obj.client, f"_requests")(
                method=method or func.__name__,
                op=op,
                name=name,
                path=get_variable(obj, path),
                data=get_parameters or dict(),
            )

        return wraps

    return client_f

# python
import requests
import inspect

# config
from config import TOKEN

class Common:
    headers = dict(
        Authorization=f"Token {TOKEN}"
    )

    def get_data(self, *args, **kwargs):
        if kwargs.get("data") is not None and isinstance(kwargs.get("data"), dict):
            return kwargs.get("data")
        data = dict()
        # set data
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        for i in args:
            data[i] = values[i]
        return data

    def get(self):
        return requests.get(self.api_uri, headers=self.headers)

    def post(self, *args, **kwargs):
        return requests.post(self.api_uri, headers=self.headers, data=self.get_data(*args, **kwargs))

    def put(self, *args, **kwargs):
        return requests.put(self.api_uri, headers=self.headers, data=self.get_data(*args, **kwargs))

    def patch(self, *args, **kwargs):
        return requests.patch(self.api_uri, headers=self.headers, data=self.get_data(*args, **kwargs))

    def delete(self):
        return requests.delete(self.api_uri, headers=self.headers)

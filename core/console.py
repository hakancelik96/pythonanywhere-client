# python
import requests
import inspect

# settings
from settings import BASE_URL

# config
from config import USERNAME, TOKEN, Common


class Console(Common):
    api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/consoles/"

    def get(self):
        "List all your consoles"

        return requests.get(self.api_uri, headers=self.headers)

    def post(self, executable="bash", arguments="", working_directory=None):
        """
        Create a new console object (NB does not actually start the process.
        Only connecting to the console in a browser will do that).
        """
        data = dict()
        # set data
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        for i in args:
            if i == "self":
                continue
            data[i] = values[i]
        return requests.post(self.api_uri, headers=self.headers, data=data)


class ShareWithYou(Common):
    api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/consoles/shared_with_you/"

    def get(self):
        "View consoles shared with you."

        return requests.get(self.api_uri, headers=self.headers)


class Id(Common):

    def __init__(self, id):
        self.api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/consoles/{id}/"

    def get(self):
        "Return information about a console instance."

        return requests.get(self.api_uri, headers=self.headers)

    def kill(self):
        "Kill a console."

        return requests.delete(self.api_uri, headers=self.headers)


class GetLatestOutput(Common):

    def __init__(self, id):
        self.api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/consoles/{id}/get_latest_output/"

    def get(self):
        "Get the most recent output from the console (approximately 500 characters)."

        return requests.get(self.api_uri, headers=self.headers)


class SendInput(Common):

    def __init__(self, id):
        self.api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/consoles/{id}/send_input/"

    def post(self, input):
        '"type" into the console. Add a "\n" for return.'
        
        return requests.post(self.api_uri, headers=self.headers, data=input)


if __name__ == "__main__":
    console = Console()
    print(console.post(executable="python3.6", name="test").json())

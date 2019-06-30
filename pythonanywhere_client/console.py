# settings
from settings import BASE_URL

# config
from config import USERNAME

# client
from client import Common


class Console(Common):
    api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/consoles/"

    def get(self):
        "List all your consoles"

        return super().get()

    def post(self, executable="bash", arguments="", working_directory=None):
        """
        Create a new console object (NB does not actually start the process.
        Only connecting to the console in a browser will do that).
        """

        p = locals()
        del p["self"]
        return super().post(**p)


class ShareWithYou(Common):
    api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/consoles/shared_with_you/"

    def get(self):
        "View consoles shared with you."

        return super().get()


class Id(Common):

    def __init__(self, id):
        self.api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/consoles/{id}/"

    def get(self):
        "Return information about a console instance."

        return super().get()

    def delete(self):
        "Kill a console."

        return super().delete()


class GetLatestOutput(Common):

    def __init__(self, id):
        self.api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/consoles/{id}/get_latest_output/"

    def get(self):
        "Get the most recent output from the console (approximately 500 characters)."

        return super().get()


class SendInput(Common):

    def __init__(self, id):
        self.api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/consoles/{id}/send_input/"

    def post(self, input):
        '"type" into the console. Add a "\n" for return.'

        return super().post(data=input)


if __name__ == "__main__":
    console = Console()
    print(console.post(executable="python3.6").json())

class Console:

    def __init__(self, client):
        self.client = client

    def get(self):
        "List all your consoles"

        return self.client._get(op="consoles")

    def post(self, executable="bash", arguments="", working_directory=None):
        """
        Create a new console object (NB does not actually start the process.
        Only connecting to the console in a browser will do that).
        """

        payload = locals()
        del payload["self"]
        return self.client._post(op="consoles", data=payload)


class ShareWithYou:

    def __init__(self, client):
        self.client = client

    def get(self):
        "View consoles shared with you."

        return self.client._get(op="consoles", name="shared_with_you")


class ConsoleId:

    def __init__(self, client, id):
        self.client = client
        self.id = id

    def get(self):
        "Return information about a console instance."

        return self.client._get(op="consoles", name=id)

    def delete(self):
        "Kill a console."

        return self.client._delete(op="consoles", name=id)


class GetLatestOutput:

    def __init__(self, client, id):
        self.client = client
        self.id = id

    def get(self):
        "Get the most recent output from the console (approximately 500 characters)."

        return self.client._get(
            op="consoles",
            name=f"{self.id}",
            path="get_latest_output"
        )


class SendInput:

    def __init__(self, client, id):
        self.client = client
        self.id = id

    def post(self, input):
        '"type" into the console. Add a "\n" for return.'

        payload = locals()
        del payload["self"]
        return self.client._post(
            op="consoles",
            name=f"{self.id}",
            path="send_input",
            data=payload
        )



if __name__ == "__main__":
    from client import Client
    client = Client(
        username="username",
        token="token"
    )
    console = Console(client)
    print(console.get().json())

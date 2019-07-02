from client import client_decorator

class Console:

    def __init__(self, client):
        self.client = client

    @client_decorator(op="consoles")
    def get(self):
        "List all your consoles"

    @client_decorator(op="consoles")
    def post(self, executable="bash", arguments="", working_directory=None):
        """
        Create a new console object (NB does not actually start the process.
        Only connecting to the console in a browser will do that).
        """
        return dict(
            executable=executable,
            arguments=arguments,
            working_directory=working_directory
        )


class ShareWithYou:

    def __init__(self, client):
        self.client = client

    @client_decorator(op="consoles", name="shared_with_you")
    def get(self):
        "View consoles shared with you."


class ConsoleId:

    def __init__(self, client, id):
        self.client = client
        self.id = id

    @client_decorator(op="consoles", name="{self.id}")
    def get(self):
        "Return information about a console instance."

    @client_decorator(op="consoles", name="{self.id}")
    def delete(self):
        "Kill a console."


class GetLatestOutput:

    def __init__(self, client, id):
        self.client = client
        self.id = id

    @client_decorator(op="consoles", name="{self.id}", path="get_latest_output")
    def get(self):
        "Get the most recent output from the console (approximately 500 characters)."


class SendInput:

    def __init__(self, client, id):
        self.client = client
        self.id = id

    @client_decorator(op="consoles", name="{self.id}", path="send_input")
    def post(self, input):
        '"type" into the console. Add a "\n" for return.'

        return dict(
            input=input
        )

if __name__ == "__main__":
    from client import Client
    client = Client(
        username="coogger",
        token="1d9d69e4a1a44d04c25dcbb385486e5cf7986361"
    )
    console = ConsoleId(client, 1)
    print(console.get())

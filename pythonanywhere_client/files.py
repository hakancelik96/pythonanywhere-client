from .client import client_decorator


class Path:
    def __init__(self, client, path):
        self.client = client
        self.path = path

    @client_decorator(op="files", name="path{self.path}")
    def get(self):
        "Downloads the file at the specified path."

    @client_decorator(op="files", name="path{self.path}")
    def post(self):
        """
        Uploads a file to the specified file path.
        Contents should be in a multipart-encoded file with the name "content".
        The attached filename is ignored. If the directories in the given path do not exist,
        they will be created. Any file already present at the specified path will be overwritten.
        Returns 201 on success if a file has been created, or 200 if an existing file has been updated.
        """

    @client_decorator(op="files", name="path{self.path}")
    def delete(self):
        """
        Deletes the file at the specified path.
        This method can be used to delete log files that are not longer required.
        Returns 204 on success.
        """


class Sharing:
    def __init__(self, client, path):
        self.client = client
        self.path = path

    @client_decorator(op="files", name="sharing", path="?path={self.path}")
    def get(self):
        "Check sharing status for a path. Returns 404 if path not currently shared."

    @client_decorator(op="files", name="sharing")
    def post(self):
        "Start sharing a file. Returns 201 on success, or 200 if file was already shared."

    @client_decorator(op="files", name="sharing", path="?path={self.path}")
    def delete(self):
        "Stop sharing a path. Returns 204 on successful unshare."

    @client_decorator(op="files", name="tree", path="?path={self.path}", method="get")
    def get_contents(self):
        """
        Returns a list of the contents of a directory, and its subdirectories as a list.
        Paths ending in slash/ represent directories. Limited to 1000 results.
        """


if __name__ == "__main__":
    from client import Client

    client = Client(username="username", token="token")
    path = Path(client=client, path=f"/home/username")
    print(path.get().text)

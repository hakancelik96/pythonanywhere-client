class Path:

    def __init__(self, client, path):
        self.client = client
        self.path

    def get(self):
        "Downloads the file at the specified path."

        return self.client._get(op="files", name=f"path{path}")

    def post(self):
        """
        Uploads a file to the specified file path.
        Contents should be in a multipart-encoded file with the name "content".
        The attached filename is ignored. If the directories in the given path do not exist,
        they will be created. Any file already present at the specified path will be overwritten.
        Returns 201 on success if a file has been created, or 200 if an existing file has been updated.
        """

        return self.client._post(op="files", name=f"path{path}")

    def delete(self):
        """
        Deletes the file at the specified path.
        This method can be used to delete log files that are not longer required.
        Returns 204 on success.
        """

        return self.client._delete(op="files", name=f"path{path}")


class Sharing:


    def __init__(self, client, path):
        self.client = client
        self.path = path

    def post(self):
        "Start sharing a file. Returns 201 on success, or 200 if file was already shared."

        return self.client._post(
            op="files",
            name="sharing",
            data=dict(path=self.path)
        )

    def get(self):
        "Check sharing status for a path. Returns 404 if path not currently shared."

        return self.client._get(
            op="files",
            name="sharing",
            path=f"?path={self.path}"
        )

    def delete(self):
        "Stop sharing a path. Returns 204 on successful unshare."

        return self.client._delete(
            op="files",
            name="sharing",
            path=f"?path={self.path}"
        )

    def get_contents(self):
        """
        Returns a list of the contents of a directory, and its subdirectories as a list.
        Paths ending in slash/ represent directories. Limited to 1000 results.
        """

        return self.client._get(
            op="files",
            name="tree",
            path=f"?path={self.path}"
        )

if __name__ == "__main__":
    from client import Client
    client = Client(
        username="username",
        token="token"
    )
    path = Path(client=client, path=f"/home/username")
    print(path.get().text)

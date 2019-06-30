# settings
from settings import BASE_URL

# config
from config import USERNAME

# client
from client import Client



class Path(Client):

    def __init__(self, path):
        self.api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/files/path{path}"

    def get(self):
        "Downloads the file at the specified path."

        return super().get()

    def post(self):
        """
        Uploads a file to the specified file path.
        Contents should be in a multipart-encoded file with the name "content".
        The attached filename is ignored. If the directories in the given path do not exist,
        they will be created. Any file already present at the specified path will be overwritten.
        Returns 201 on success if a file has been created, or 200 if an existing file has been updated.
        """

        return super().post()

    def delete(self):
        """
        Deletes the file at the specified path.
        This method can be used to delete log files that are not longer required.
        Returns 204 on success.
        """

        return super().delete()


class Sharing(Client):


    def __init__(self, path):
        self.path = path

    def post(self):
        "Start sharing a file. Returns 201 on success, or 200 if file was already shared."

        self.api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/files/sharing/"
        return super().post(path=self.path)

    def get(self):
        "Check sharing status for a path. Returns 404 if path not currently shared."

        self.api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/files/sharing/?path={self.path}"
        return super().get()

    def delete(self):
        "Stop sharing a path. Returns 204 on successful unshare."

        self.api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/files/sharing/?path={self.path}"
        return super().delete()

    def get_contents(self):
        """
        Returns a list of the contents of a directory, and its subdirectories as a list.
        Paths ending in slash/ represent directories. Limited to 1000 results.
        """

        self.api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/files/tree/?path={self.path}"
        return super().get()


if __name__ == "__main__":
    console = Path(path=f"/home/{USERNAME}")
    print(console.get().text)

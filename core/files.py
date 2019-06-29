# python
import requests
import inspect

# settings
from settings import BASE_URL

# config
from config import USERNAME, TOKEN, Common


class Path(Common):

    def __init__(self, path):
        self.api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/files/path{path}"

    def get(self):
        "Downloads the file at the specified path."

        return requests.get(self.api_uri, headers=self.headers)

    def post(self):
        """
        Uploads a file to the specified file path.
        Contents should be in a multipart-encoded file with the name "content".
        The attached filename is ignored. If the directories in the given path do not exist,
        they will be created. Any file already present at the specified path will be overwritten.
        Returns 201 on success if a file has been created, or 200 if an existing file has been updated.
        """

        return requests.post(self.api_uri, headers=self.headers)

    def delete(self):
        """
        Deletes the file at the specified path.
        This method can be used to delete log files that are not longer required.
        Returns 204 on success.
        """

        return requests.delete(self.api_uri, headers=self.headers)


class Sharing(Common):


    def __init__(self, path):
        self.path = path

    def post(self):
        "Start sharing a file. Returns 201 on success, or 200 if file was already shared."

        api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/files/sharing/"
        return requests.post(api_uri, headers=self.headers, data=dict(path=self.path))

    def get(self):
        "Check sharing status for a path. Returns 404 if path not currently shared."

        api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/files/sharing/?path={self.path}"
        return requests.get(api_uri, headers=self.headers)

    def delete(self):
        "Stop sharing a path. Returns 204 on successful unshare."

        api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/files/sharing/?path={self.path}"
        return requests.delete(api_uri, headers=self.headers)

    def get_contents(self):
        """
        Returns a list of the contents of a directory, and its subdirectories as a list.
        Paths ending in slash/ represent directories. Limited to 1000 results.
        """

        api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/files/tree/?path={self.path}"
        return requests.get(api_uri, headers=self.headers)


if __name__ == "__main__":
    console = Sharing(path=f"/home/{USERNAME}")
    print(console.get_contents().json())

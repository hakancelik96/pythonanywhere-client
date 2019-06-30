# settings
from settings import BASE_URL

# config
from config import USERNAME

# client
from client import Client


class Webapps(Client):
    api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/webapps/"

    def get(self):
        "List all webapps"

        return super().get()

    def post(self, domain_name, python_version):
        """
        Create a new webapp with manual configuration.
        Use (for example) "python36" to specify Python 3.6.
        """

        p = locals()
        del p["self"]
        return super().post(**p)


class DomaiName(Client):

    def __init__(self, domain_name):
        self.api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/webapps/{domain_name}/"

    def get(self):
        "Return information about a web app's configuration"

        return super().get()

    def put(self, python_version, source_directory, virtualenv_path, force_https):
        "Modify configuration of a web app. (NB a reload is usually required to apply changes)."

        p = locals()
        del p["self"]
        return super().put(**p)

    def patch(self, python_version, source_directory, virtualenv_path, force_https):
        "Modify configuration of a web app. (NB a reload is usually required to apply changes)."

        p = locals()
        del p["self"]
        return super().patch(**p)

    def delete(self):
        """
        Delete the webapp. This will take the site offline.
        Config is backed up in /var/www, and your code is not touched.
        """

        return super().delete()


class Reload(Client):

    def __init__(self, domain_name):
        self.api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/webapps/{domain_name}/reload/"

    def post(self):
        "Reload the webapp to reflect changes to configuration and/or source code on disk."

        return super().post()


class Ssl(Client):

    def __init__(self, domain_name):
        self.api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/webapps/{domain_name}/ssl/"

    def get(self):
        """
        Get and set TLS/HTTPS info. POST parameters to the right are incorrect,
        use `cert` and `private_key` when posting.
        """

        return super().get()

    def post(self, python_version, source_directory, virtualenv_path, force_https):
        """
        Get and set TLS/HTTPS info. POST parameters to the right are incorrect,
        use `cert` and `private_key` when posting.
        """

        p = locals()
        del p["self"]
        return super().post(**p)

    def delete(self):
        """
        Get and set TLS/HTTPS info. POST parameters to the right are incorrect,
        use `cert` and `private_key` when posting.
        """

        return super().delete(**p)


class StaticFiles(Client):

    def __init__(self, domain_name):
        self.api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/webapps/{domain_name}/static_files/"

    def get(self):
        "List all the static files mappings for a domain."

        return super().get()

    def post(self, url, path):
        "Create a new static files mapping. (webapp restart required)"

        p = locals()
        del p["self"]
        return super().post(**p)

class StaticFilesId(Client):

    def __init__(self, domain_name, id):
        self.api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/webapps/{domain_name}/static_files/{id}/"

    def get(self):
        "Get URL and path of a particular mapping."

        return super().get()

    def put(self, url, path):
        "Modify a static files mapping. (webapp restart required)"

        p = locals()
        del p["self"]
        return super().put(**p)

    def patch(self, url, path):
        "Modify a static files mapping. (webapp restart required)"

        p = locals()
        del p["self"]
        return super().patch(**p)

    def delete(self):
        "Remove a static files mapping. (webapp restart required)"

        return super().delete()

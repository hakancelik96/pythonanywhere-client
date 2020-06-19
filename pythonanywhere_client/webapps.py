from .client import client_decorator


class Webapps:
    def __init__(self, client):
        self.client = client

    @client_decorator(op="webapps")
    def get(self):
        "List all webapps"

    @client_decorator(op="webapps")
    def post(self, domain_name, python_version):
        """
        Create a new webapp with manual configuration.
        Use (for example) "python36" to specify Python 3.6.
        """


class DomaiName:
    def __init__(self, client, domain_name):
        self.client = client
        self.domain_name = domain_name

    @client_decorator(op="webapps", name="{self.domain_name}")
    def get(self):
        "Return information about a web app's configuration"

    @client_decorator(op="webapps", name="{self.domain_name}")
    def put(
        self, python_version, source_directory, virtualenv_path, force_https
    ):
        "Modify configuration of a web app. (NB a reload is usually required to apply changes)."

    @client_decorator(op="webapps", name="{self.domain_name}")
    def patch(
        self, python_version, source_directory, virtualenv_path, force_https
    ):
        "Modify configuration of a web app. (NB a reload is usually required to apply changes)."

    @client_decorator(op="webapps", name="{self.domain_name}")
    def delete(self):
        """
        Delete the webapp. This will take the site offline.
        Config is backed up in /var/www, and your code is not touched.
        """


class Reload:
    def __init__(self, client, domain_name):
        self.client = client
        self.domain_name = domain_name

    @client_decorator(op="webapps", name="{self.domain_name}", path="reload")
    def post(self):
        "Reload the webapp to reflect changes to configuration and/or source code on disk."


class Ssl:
    def __init__(self, client, domain_name):
        self.client = client
        self.domain_name = domain_name

    @client_decorator(op="webapps", name="{self.domain_name}", path="ssl")
    def get(self):
        """
        Get and set TLS/HTTPS info. POST parameters to the right are incorrect,
        use `cert` and `private_key` when posting.
        """

    @client_decorator(op="webapps", name="{self.domain_name}", path="ssl")
    def post(
        self, python_version, source_directory, virtualenv_path, force_https
    ):
        """
        Get and set TLS/HTTPS info. POST parameters to the right are incorrect,
        use `cert` and `private_key` when posting.
        """

    @client_decorator(op="webapps", name="{self.domain_name}", path="ssl")
    def delete(self):
        """
        Get and set TLS/HTTPS info. POST parameters to the right are incorrect,
        use `cert` and `private_key` when posting.
        """


class StaticFiles:
    def __init__(self, client, domain_name):
        self.client = client
        self.domain_name = domain_name

    @client_decorator(
        op="webapps", name="{self.domain_name}", path="static_files"
    )
    def get(self):
        "List all the static files mappings for a domain."

    @client_decorator(
        op="webapps", name="{self.domain_name}", path="static_files"
    )
    def post(self, url, path):
        "Create a new static files mapping. (webapp restart required)"


class StaticFilesId:
    def __init__(self, client, domain_name, id):
        self.client = client
        self.domain_name = domain_name
        self.id = id

    @client_decorator(
        op="webapps", name="{self.domain_name}", path="static_files/{self.id}"
    )
    def get(self):
        "Get URL and path of a particular mapping."

    @client_decorator(
        op="webapps", name="{self.domain_name}", path="static_files/{self.id}"
    )
    def put(self, url, path):
        "Modify a static files mapping. (webapp restart required)"

    @client_decorator(
        op="webapps", name="{self.domain_name}", path="static_files/{self.id}"
    )
    def patch(self, url, path):
        "Modify a static files mapping. (webapp restart required)"

    @client_decorator(
        op="webapps", name="{self.domain_name}", path="static_files/{self.id}"
    )
    def delete(self):
        "Remove a static files mapping. (webapp restart required)"

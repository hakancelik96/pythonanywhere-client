class Webapps:

    def __init__(self, client):
        self.client = client

    def get(self):
        "List all webapps"

        return self.client._get(op="webapps")

    def post(self, domain_name, python_version):
        """
        Create a new webapp with manual configuration.
        Use (for example) "python36" to specify Python 3.6.
        """

        payload= locals()
        del payload["self"]
        return self.client._post(op="webapps", data=payload)


class DomaiName:

    def __init__(self, client, domain_name):
        self.client = client
        self.domain_name = domain_name

    def get(self):
        "Return information about a web app's configuration"

        return self.client._get(op="webapps", name=self.domain_name)

    def put(self, python_version, source_directory, virtualenv_path, force_https):
        "Modify configuration of a web app. (NB a reload is usually required to apply changes)."

        payload = locals()
        del payload["self"]
        return self.client._put(op="webapps", name=self.domain_name, data=payload)

    def patch(self, python_version, source_directory, virtualenv_path, force_https):
        "Modify configuration of a web app. (NB a reload is usually required to apply changes)."

        payload = locals()
        del payload["self"]
        return self.client._patch(op="webapps", name=self.domain_name, data=payload)

    def delete(self):
        """
        Delete the webapp. This will take the site offline.
        Config is backed up in /var/www, and your code is not touched.
        """

        return self.client._delete(op="webapps", name=self.domain_name)


class Reload:

    def __init__(self, client, domain_name):
        self.client = client
        self.domain_name = domain_name

    def post(self):
        "Reload the webapp to reflect changes to configuration and/or source code on disk."

        return self.client._post(op="webapps", name=self.domain_name, path="reload")


class Ssl:

    def __init__(self, client, domain_name):
        self.client = client
        self.domain_name = domain_name

    def get(self):
        """
        Get and set TLS/HTTPS info. POST parameters to the right are incorrect,
        use `cert` and `private_key` when posting.
        """

        return self.client._get(op="webapps", name=self.domain_name, path="ssl")

    def post(self, python_version, source_directory, virtualenv_path, force_https):
        """
        Get and set TLS/HTTPS info. POST parameters to the right are incorrect,
        use `cert` and `private_key` when posting.
        """

        payload = locals()
        del payload["self"]
        return self.client._post(
            op="webapps",
            name=self.domain_name,
            path="ssl",
            data=payload
        )

    def delete(self):
        """
        Get and set TLS/HTTPS info. POST parameters to the right are incorrect,
        use `cert` and `private_key` when posting.
        """

        return self.client._delete(op="webapps", name=self.domain_name, path="ssl")


class StaticFiles:

    def __init__(self, client, domain_name):
        self.client = client
        self.domain_name = domain_name

    def get(self):
        "List all the static files mappings for a domain."

        return self.client._get(op="webapps", name=self.domain_name, path="static_files")

    def post(self, url, path):
        "Create a new static files mapping. (webapp restart required)"

        payload = locals()
        del payload["self"]
        return self.client._post(
            op="webapps",
            name=self.domain_name,
            path="static_files",
            data=payload
        )


class StaticFilesId:

    def __init__(self, client, domain_name, id):
        self.client = client
        self.domain_name = domain_name
        self.id = id

    def get(self):
        "Get URL and path of a particular mapping."

        return self.client._get(
            op="webapps",
            name=self.domain_name,
            path=f"static_files/{id}"
        )

    def put(self, url, path):
        "Modify a static files mapping. (webapp restart required)"

        payload = locals()
        del payload["self"]
        return self.client._put(
            op="webapps",
            name=self.domain_name,
            path=f"static_files/{id}",
            data=payload
        )

    def patch(self, url, path):
        "Modify a static files mapping. (webapp restart required)"

        payload = locals()
        del payload["self"]
        return self.client._patch(
            op="webapps",
            name=self.domain_name,
            path=f"static_files/{id}",
            data=payload
        )

    def delete(self):
        "Remove a static files mapping. (webapp restart required)"

        return self.client._delete(
            op="webapps",
            name=self.domain_name, 
            path=f"static_files/{id}"
        )

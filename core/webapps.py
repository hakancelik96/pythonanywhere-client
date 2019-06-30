# settings
from settings import BASE_URL

# config
from config import USERNAME

# client
from client import Common


class Webapps(Common):
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


class DomaiName(Common):

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

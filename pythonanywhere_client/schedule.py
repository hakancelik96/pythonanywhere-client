# settings
from settings import BASE_URL

# config
from config import USERNAME

# client
from client import Common



class Schedule(Common):
    api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/schedule/"

    def get(self):
        "List all of your scheduled tasks"

        return super().get()

    def post(self, command, enabled=True, interval="daily", hour=20, minute=0):
        """
        Create a new scheduled task
        command: 'python3.6 { path }'
        """

        p = locals()
        del p["self"]
        return super().post(**p)


class Id(Common):

    def __init__(self, id):
        self.api_uri = f"{BASE_URL}/api/v0/user/{USERNAME}/schedule/{id}/"

    def get(self):
        "Return information about a scheduled task."

        return super().get()

    def put(self, command, enabled=True, interval="daily", hour=20, minute=0):
        "Endpoints for scheduled tasks"

        p = locals()
        del p["self"]
        return super().put(**p)

    def patch(self, command, enabled=True, interval="daily", hour=20, minute=0):
        "Endpoints for scheduled tasks"

        p = locals()
        del p["self"]
        return super().patch(**p)

    def delete(self):
        "Delete an scheduled task"

        return super().delete()



if __name__ == "__main__":
    s = Schedule()
    print(s.post(command="python3.6 /home/coogger/trade_follow/trade_follow/trade_follow.py").json())

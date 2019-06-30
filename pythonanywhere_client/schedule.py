class Schedule:

    def __init__(self, client):
        self.client = client

    def get(self):
        "List all of your scheduled tasks"

        return self.client._get(op="schedule")

    def post(self, command, enabled=True, interval="daily", hour=20, minute=0):
        """
        Create a new scheduled task
        command: 'python3.6 { path }'
        """

        payload = locals()
        del payload["self"]
        return self.client._post(op="schedule", data=payload)


class Id:

    def __init__(self, id):
        self.id = id

    def get(self):
        "Return information about a scheduled task."

        return self.client._get(op="schedule", name=self.id)

    def put(self, command, enabled=True, interval="daily", hour=20, minute=0):
        "Endpoints for scheduled tasks"

        payload = locals()
        del payload["self"]
        return self.client._put(op="schedule", name=self.id, data=payload)

    def patch(self, command, enabled=True, interval="daily", hour=20, minute=0):
        "Endpoints for scheduled tasks"

        p = locals()
        del p["self"]
        return self.client._patch(op="schedule", name=self.id, data=payload)

    def delete(self):
        "Delete an scheduled task"

        return self.client._delete(op="schedule", name=self.id)


if __name__ == "__main__":
    from client import Client
    client = Client(
        username="username",
        token="token"
    )
    schedule = Schedule(client=client)
    print(schedule.post(command="python3.6 /home/{username}/{file_path}").json())

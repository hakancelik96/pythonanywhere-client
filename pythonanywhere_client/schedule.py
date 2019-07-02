from client import client_decorator

class Schedule:

    def __init__(self, client):
        self.client = client

    @client_decorator(op="schedule")
    def get(self):
        "List all of your scheduled tasks"

    @client_decorator(op="schedule")
    def post(self, command, enabled=True, interval="daily", hour=20, minute=0):
        """
        Create a new scheduled task
        command: 'python3.6 { path }'
        """

        return dict(
            command=command,
            enabled=enabled,
            interval=interval,
            hour=hour,
            minute=minute
        )


class ScheduleId:

    def __init__(self, id):
        self.id = id

    @client_decorator(op="schedule", name="{self.id}")
    def get(self):
        "Return information about a scheduled task."

    @client_decorator(op="schedule", name="{self.id}")
    def put(self, command, enabled=True, interval="daily", hour=20, minute=0):
        "Endpoints for scheduled tasks"

        return dict(
            command=command,
            enabled=enabled,
            interval=interval,
            hour=hour,
            minute=minute
        )

    @client_decorator(op="schedule", name="{self.id}")
    def patch(self, command, enabled=True, interval="daily", hour=20, minute=0):
        "Endpoints for scheduled tasks"

        return dict(
            command=command,
            enabled=enabled,
            interval=interval,
            hour=hour,
            minute=minute
        )

    @client_decorator(op="schedule", name="{self.id}")
    def delete(self):
        "Delete an scheduled task"


if __name__ == "__main__":
    from client import Client
    client = Client(
        username="username",
        token="token"
    )
    schedule = Schedule(client=client)
    print(schedule.post(command="python3.6 /home/{username}/{file_path}").json())

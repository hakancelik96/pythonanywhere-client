import os

from pythonanywhere_client.client import Client
from pythonanywhere_client.files import Path, Sharing

username = "coogger"
token = "1d9d69e4a1a44d04c25dcbb385486e5cf7986361"
project_name = "coogger"

client = Client(username=username, token=token)

path = f"/home/{username}/{project_name}/"

valid_folder = [
    # f"{path}/media/images/",
    f"{path}/db/"
]


def create_folder(direction):
    if not os.path.exists(direction):
        os.makedirs(direction)


for folder in valid_folder:
    folder_name = folder.split("/")[-2]
    create_folder(os.getcwd() + "/" + folder_name)
    sharing = Sharing(client=client, path=folder)
    for path in sharing.get_contents().json():
        download_file = Path(client=client, path=path).get().content
        with open(
            os.getcwd() + "/" + folder_name + "/" + path.split("/")[-1], "wb"
        ) as file:
            file.write(download_file)

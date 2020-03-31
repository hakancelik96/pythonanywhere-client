# An Example To Backup Specific Files From Pythonanywhere Server

This example only backup files in `invalid_folder` list, The items in the invalid\_folder list are the folder names where the databases and image files are located, so the following example was written to back up databases and image files.

```python
from pythonanywhere_client.client import Client
from pythonanywhere_client.files import Path, Sharing

import os

username = "username"
token = "token"
project_name = "project_name"

client = Client(
    username=username,
    token=token
)
path = f"/home/{username}/{project_name}/"

valid_folder = [
    f"{path}/media/images/",
    f"{path}/db/",
]

def create_folder(direction):
    if not os.path.exists(direction):
        os.makedirs(direction)

for folder in valid_folder:
    folder_name = folder.split("/")[-2]
    create_folder(os.getcwd()+"/"+folder_name)
    sharing = Sharing(client=client, path=folder)
    for path in sharing.get_contents().json():
        download_file = Path(client=client, path=path).get().content
        with open(os.getcwd()+"/"+folder_name+"/"+path.split("/")[-1], "wb") as file:
            file.write(download_file)
```

## Line 28

Allows us to get files under the given folder path.

## Line 30

line and we took the data as a binary.

## Line 31

We opened the file in the binary format.


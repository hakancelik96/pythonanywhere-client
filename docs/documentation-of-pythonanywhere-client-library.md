# Documentation of Pythonanywhere Client Library

## How to Install
`pip install pythonanywhere-client`

## How to Use

### Client
Client class purpose is to get your project username and token then send any requests to pythonanywhere API service.

```python
from pythonanywhere_client.client import Client

client = Client(
  usernama="your_pythonanywhere_username",
  token="your_pythonanywhere_app_token"
)
```

### Where is My API Token ?
Here, `https://www.pythonanywhere.com/user/{{ your_username }}/account/#api_token`

Follow the [API documentation](https://help.pythonanywhere.com/pages/API/) to submit your requests with this library, its to easy.

### Console
```python
from pythonanywhere_client.console import Console, ShareWithYou, ConsoleId, GetLatestOutput, SendInput
```

#### Console Class
```python
>>> console = Console(client=client)
```

##### get function
List all your consoles
```pyhton
>>> console.get()
```

##### post function
Create a new console object (NB does not actually start the process. Only connecting to the console in a browser will do that).

**Parameters**
- executable
	- str
	- default= 'bash'
- arguments
	- str
	- default= ""
- working_directory
	- str
	- default = None

```pyhton
>>> console.post()
```

#### ShareWithYou Class
```python
>>> share_with_you = ShareWithYou(client=client)
```

##### get function
View consoles shared with you.
```python
>>> share_with_you.get()
```

#### ConsoleId Class
**Parameters**
- id
	- str
	- your_any_console_id

```python
>>> console_id = ConsoleId(client=client, id: str)
```

##### get function
Return information about a console instance.
```python
>>> console_id.get()
```

#### delete function
Kill a console
```python
>>> console_id.delete()
```

#### GetLatestOutput Class
**Parameters**
- id
	- str
	- your_any_console_id

```python
>>> get_lates_output = GetLatestOutput(client=client, id: str)
```

##### get function
Get the most recent output from the console (approximately 500 characters).
```python
>>> get_lates_output.get()
```

#### SendInput Class
**Parameters**
- id
	- str
	- your_any_console_id

```python
>>> send_input = SendInput(client=client, id: str)
```

##### post function
"type" into the console. Add a "\n" for return.

**Parameters**
- input
	- str
	- example: 'source myvenv/bin/activate\n'

```python
>>> send_input.post(input: str)
```

### Files
```python
from pythonanywhere_client.files import Path, Sharing
```

#### Path Class
**parameters**
- client
- path
	- your_any_file_or_folder_path

```python
>>> path = Path(client=client, path: str)
```

##### get function
Downloads the file at the specified path
```python
>>> path.get()
```

##### post function
Uploads a file to the specified file path. Contents should be in a multipart-encoded file with the name "content". The attached filename is ignored. If the directories in the given path do not exist, they will be created. Any file already present at the specified path will be overwritten. Returns 201 on success if a file has been created, or 200 if an existing file has been updated.
```python
>>> path.post()
```

##### delete function
Deletes the file at the specified path. This method can be used to delete log files that are not longer required. Returns 204 on success.
```python
>>> path.delete()
```

#### Sharing Class
```python
>>> sharing = Sharing(client=client, path: str = "your_any_file_or_folder_path")
```

##### get function
Check sharing status for a path. Returns 404 if path not currently shared.
```python
>>> path.get()
```

##### post function
Start sharing a file. Returns 201 on success, or 200 if file was already shared.
```python
>>> path.post()
```

##### delete function
Stop sharing a path. Returns 204 on successful unshare.
```python
>>> path.delete()
```

##### get_contents function
Returns a list of the contents of a directory, and its subdirectories as a list. Paths ending in slash/ represent directories. Limited to 1000 results.
```python
>>> path.get_contents()
```

### Schedule
```python
from pythonanywhere_client.schedule import Schedule, ScheduleId
```

#### Schedule Class
```python
>>> schedule = Schedule(client=client)
```

##### get function
List all of your scheduled tasks
```python
>>> schedule.get()
```

##### post function
Create a new scheduled task

**parameters**
- command
	- str
	- example: 'python3.6 { write_your_file_path }'
- enabled
	- bool or str
	- default: True
- interval
	- str
	- default: "daily"
- hour
	- number, int, str, float
	- defult: 20
- minute
	- number, int, str, float
	- default: 0

```python
>>> schedule.post(command: str)
```

#### ScheduleId Class
**parameters**
- client
- id
	- your_task_id

```python
>>> schedule_id = ScheduleId(client=client, id: str)
```

##### get function
Return information about a scheduled task
```python
>>> schedule_id.get()
```

##### put function
Endpoints for scheduled tasks

**parameters**
- command
	- str
	- example: 'python3.6 { write_your_file_path }'
- enabled
	- bool or str
	- default: True
- interval
	- str
	- default: "daily"
- hour
	- number, int, str, float
	- defult: 20
- minute
	- number, int, str, float
	- default: 0

```python
>>> schedule_id.put(command: str)
```

##### patch function
Endpoints for scheduled tasks

**parameters**
- command
	- str
	- example: 'python3.6 { write_your_file_path }'
- enabled
	- bool or str
	- default: True
- interval
	- str
	- default: "daily"
- hour
	- number, int, str, float
	- defult: 20
- minute
	- number, int, str, float
	- default: 0

```python
>>> schedule_id.patch(command: str)
```

##### delete function
Delete an scheduled task
```python
>>> schedule_id.delete()
```

### Webapps
```python
from pythonanywhere_client.webapps import Webapps, DomaiName, Reload, Ssl, StaticFiles, StaticFilesId
```

#### Webapps Class
```python
>>> web_apps = Webapps(client=client)
```

##### get function
List all webapps
```python
>>> web_apps.get()
```

##### post function
Create a new webapp with manual configuration. Use (for example) "python36" to specify Python 3.6.

**parameters**
- domain_name
	- str
- python_version
	- str

```python
>>> web_apps.post(domain_name: str, python_version: str)
```

#### DomaiName Class
**parameters**
- client
- domain_name
	- str
	- example: 'www.coogger.com'

```python
>>> domain_name = DomaiName(client=client, domain_name: str)
```

##### get function
Return information about a web app's configuration
```python
>>> domain_name.get()
```

##### put function
Modify configuration of a web app. (NB a reload is usually required to apply changes).

```python
>>> domain_name.put(python_version: str, source_directory: str, virtualenv_path: str, force_https: bool)
```

##### patch function
Modify configuration of a web app. (NB a reload is usually required to apply changes).

```python
>>> domain_name.patch(python_version: str, source_directory: str, virtualenv_path: str, force_https: bool)
```

##### delete function
Delete the webapp. This will take the site offline. Config is backed up in /var/www, and your code is not touched.
```python
>>> domain_name.delete()
```

#### Reload Class
**parameters**
- client
- domain_name
	- str
	- example: 'www.coogger.com'

```python
>>> reload = Reload(client=client, domain_name: str)
```

##### post function
Reload the webapp to reflect changes to configuration and/or source code on disk.
```python
>>> reload.post()
```

#### Ssl Class
**parameters**
- client
- domain_name
	- str
	- example: 'www.coogger.com'

```python
>>> ssl = Ssl(client=client, domain_name: str)
```

##### get function
Get and set TLS/HTTPS info. POST parameters to the right are incorrect, use `cert` and `private_key` when posting.
```python
>>> ssl.get()
```

##### post function
Get and set TLS/HTTPS info. POST parameters to the right are incorrect, use `cert` and `private_key` when posting.
```python
>>> ssl.post(python_version: str, source_directory: str, virtualenv_path: str, force_https: bool)
```

##### delete function
 Get and set TLS/HTTPS info. POST parameters to the right are incorrect use `cert` and `private_key` when posting.
```python
>>> ssl.delete()
```


#### StaticFiles Class
**parameters**
- client
- domain_name
	- str
	- example: 'www.coogger.com'

```python
>>> static_files = StaticFiles(client=client, domain_name: str)
```

##### get function
List all the static files mappings for a domain.
```python
>>> static_files.get()
```

##### post function
Create a new static files mapping. (webapp restart required)
```python
>>> static_files.post(url: str, path: str)
```

#### StaticFilesId Class
**parameters**
- client
- domain_name
	- str
	- example: 'www.coogger.com'

```python
>>> static_files_id = StaticFilesId(client=client, domain_name: str)
```

##### get function
Get URL and path of a particular mapping
```python
>>> static_files_id.get()
```

##### put function
Modify a static files mapping. (webapp restart required)
```python
>>> static_files_id.put(url: str, path: str)
```

##### patch function
Modify a static files mapping. (webapp restart required)
```python
>>> static_files_id.patch(url: str, path: str)
```

##### delete function
Remove a static files mapping. (webapp restart required)
```python
>>> static_files_id.delete()
```

## Donate

> If you like this work you can donate to me

- BTC Address '1Hk9M9cSng2pziHtc3ak75Wegx9sx8NPwT'
- LTC Address 'LeJheyL4assPejXTRhQX5LBu59KDW6bK32'
- ETH Address '0x1baf218f8f0366e3e9ef8d2609ecfd51cd136715'
- Steem Account https://steemitwallet.com/@hakancelik

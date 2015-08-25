# [TeamspeakClientQueryAPIpy](https://github.com/BluscreamFanBoy/TeamspeakClientQueryAPIpy)

This is a python module with useful functions for using the Teamspeak Client Query


## Quick Start

Its simple like that you import the `api` module

```python
#Import the api module
import api
```
And then you can use all functions<br>
To start the a connection to the Teamspeak Client Query you simply can run the function [teamspeak_socket_init](#teamspeak_socket_init) and get the return variable
```python
#Import the api module
import api

#Create a connection to the current client query
ts3clientquery = api.teamspeak_socket_init()
```
In the next step you can use this variable to send and receive something from your clientquery data.<br>
In this example we change your nickname for that we need the [teamspeak_socket_send](#teamspeak_socket_send) function
```python
#Import the api module
import api

#Create a connection to the current client query
ts3clientquery = api.teamspeak_socket_init()

'''
Here we use the teamspeak_socket_send function with 
clientupdate command and set with parameter client_nickname
the nickname and escape this nickname
with the teamspeak_escape function
'''
print(api.teamspeak_socket_send(ts3clientquery,"clientupdate client_nickname=".api.teamspeak_escape("I am Stupid")))
```
After you send all what you want the best way to end your program is to use the `close`
function
```python
#Import the api module
import api

#Create a connection to the current client query
ts3clientquery = api.teamspeak_socket_init()

'''
Here we use the teamspeak_socket_send function with 
clientupdate command and set with parameter client_nickname
the nickname and escape this nickname
with the teamspeak_escape function
'''
print(api.teamspeak_socket_send(ts3clientquery,"clientupdate client_nickname=".api.teamspeak_escape("I am Stupid")))

#Close the clientquery
ts3clientquery.close()
```

## Functions

[teamspeak_socket_init](#teamspeak_socket_init)<br>
[teamspeak_socket_send](#teamspeak_socket_send)

### teamspeak_socket_init

#### Description
```python
def teamspeak_socket_init(clientquery_port=25639):
```
This is a Function that initalize a local socket connection to the teamspeak client query and `gets` and `print` the first 3 lines of the response.

#### Parameters
`clientquery_port`<br>
The Client Query must be a Integer. If not set it is using the default port for the clientquery(25639).

#### Return Values
This Function return a simple raw socket for a connection to the teamspeak client query.

#### Examples

```python
#Create a connection to the current client query
ts3query = api.teamspeak_socket_init()
```

```python
#Create a connection to the current client query with a custom port
ts3query = api.teamspeak_socket_init(12058)
```

#### Changelog

No Changes

### teamspeak_socket_send

#### Description
```python
def teamspeak_socket_send(socket,command):
```
This function use the pre initalized socket ([teamspeak_socket_init](#teamspeak_socket_init)) to send some command to the client query.

#### Parameters
`socket`<br>
The Client Query Socket must be a raw tcp socket connection. I recommend to use the [teamspeak_socket_init](#teamspeak_socket_init) function, because you maybe get trouble with getting data from the response stream.

`command`<br>
The Command must be a String without "\n". I recommend to use the [tool.py](https://github.com/BluscreamFanBoy/TeamspeakClientQueryAPIpy/blob/master/tool.py) to find out more about the commands.

#### Return Values
This Function return the next line of the response after sending the command.

#### Examples

```python
#Create a connection to the current client query
ts3query = api.teamspeak_socket_init()

#Send the Command to Change the nickname to "IamStupid"
api.teamspeak_socket_send(ts3query,"clientupdate client_nickname=IamStupid")
```

#### Changelog

No Changes

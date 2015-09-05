#!/usr/bin/python
#.note the api file must be in the same directory as this file 
import api
#Create a Connection and Change Your Nickname To "I am Stupid"
ts3query = api.teamspeak_socket_init()
print(api.teamspeak_socket_send(ts3query,"clientupdate client_nickname="+api.teamspeak_escape("I am Stupid")))
ts3query.close()
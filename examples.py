#!/usr/bin/python
import api

#Create a Connection and Change Your Nickname To "I am Stupid"
ts3query = api.teamspeak_socket_init()
print(api.teamspeak_socket_send(ts3query,"clientupdate client_nickname="+api.teamspeak_escape("I am Stupid")))
ts3query.close()

#Create a Connection and Printout The Help Page
ts3query = api.teamspeak_socket_init()
line = api.teamspeak_socket_send(ts3query,"help")
while api.get_teamspeak_status(line) == None:
	print(line)
	line = api.fgets(ts3query)
ts3query.close()
input()
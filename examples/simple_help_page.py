#!/usr/bin/python
#.note the api file must be in the same directory as this file 
import api
#Create a Connection and Printout The Help Page
ts3query = api.teamspeak_socket_init()
line = api.teamspeak_socket_send(ts3query,"help")
while api.get_teamspeak_status(line) == None:
	print(line)
	line = api.fgets(ts3query)
ts3query.close()
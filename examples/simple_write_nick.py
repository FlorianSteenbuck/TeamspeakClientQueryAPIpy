#!/usr/bin/python
#.note the api file must be in the same directory as this file 
import api
#use the an_write function to create a animation like writing
name = "I am Stupid"
ts3query = api.teamspeak_socket_init()
for i in range(2,len(name)+1):
	print(api.teamspeak_socket_send(ts3query,"clientupdate client_nickname="+api.teamspeak_escape(api.an_write(i,name))))
ts3query.close()
input()
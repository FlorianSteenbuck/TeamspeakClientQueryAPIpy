#!/usr/bin/python
#.note the api file must be in the same directory as this file 
import api
import time
import random

#change every 10 seconds your name to a random name
names = ["I am Stupid","I am not Stupid","Whatever"]
lastname = ""
ts3query = api.teamspeak_socket_init()
while 1:
	name = names[random.randint(0,len(names)-1)]
	while lastname == name:
		name = names[random.randint(0,len(names)-1)]
	print(api.teamspeak_socket_send(ts3query,"clientupdate client_nickname="+api.teamspeak_escape(name)))
	lastname = name
	time.sleep(10)
ts3query.close()
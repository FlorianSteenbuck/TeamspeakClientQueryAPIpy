#!/usr/bin/python
import api
import time
import random

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
#use the an_write function to create a animation like writing
name = "I am Stupid"
ts3query = api.teamspeak_socket_init()
for i in range(2,len(name)+1):
	print(api.teamspeak_socket_send(ts3query,"clientupdate client_nickname="+api.teamspeak_escape(api.an_write(i,name))))
input()
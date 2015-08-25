#!/usr/bin/python
import api

# This is a simple ClientQuery Tool

ts3query = api.teamspeak_socket_init()
while 1:
	cmd = input()
	if cmd == 'close':
		break
	line = api.teamspeak_socket_send(ts3query,cmd)
	while api.get_teamspeak_status(line) == None:
		print(line)
		line = api.fgets(ts3query)
	print(line)
ts3query.close()
#!/usr/bin/python
import socket
import sys
import string

def fgets(socket,recv_bytes=2,deml='\n\r'):
	data = ''
	while 1:
		data += socket.recv(recv_bytes).decode('utf-8')
		if deml in data:
			data = data.split(deml)[0]
			break
	return data

def teamspeak_unescape(str):
	return ((str.replace('↵', '\n')).replace('\\s', ' ')).replace('│', '|')
def teamspeak_escape(str):
	return ((str.replace('\n', '↵')).replace(' ', '\\s')).replace('|', '│')
def get_teamspeak_param(name,teamspeakreturn):
	if isinstance(name,int):
		return teamspeakreturn.split(' ')[name].split('=')[1]
	if name.isalpha():
		value = NULL
		args = teamspeakreturn.split(' ')
		for arg in args:
			keyval = arg.split('=')
			if keyval[0] == name:
				value = keyval[1]
				break
		return value
	else:
		return NULL
def get_teamspeak_status(teamspeakreturn):
	if teamspeakreturn[0:6] == '\rerror':
		return get_teamspeak_param(1,teamspeakreturn)
	else:
		return NULL
def teamspeak_socket_init(client_queryport=25639):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(('localhost', client_queryport))
	print(fgets(sock))
	print(fgets(sock))
	print(fgets(sock))
	return sock
def teamspeak_socket_send(sock,command):
	sock.sendall((command+'\n').encode('utf-8'))
	return fgets(sock)
def teamspeak_getname(sock):
	tmp = teamspeak_socket_send(sock,'whoami')
	print(fgets(sock))
	clid = get_teamspeak_param(0,tmp)
	tmp = teamspeak_socket_send(sock, "clientvariable clid="+clid+" client_nickname")
	print(fgets(sock))
	name = teamspeak_unescape(get_teamspeak_param(1,tmp))
	return name

version='1'
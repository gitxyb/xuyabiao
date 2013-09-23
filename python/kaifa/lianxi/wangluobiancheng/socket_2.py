#coding:utf8
#客户端

import socket
import threading

ke_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ke_obj.connect(('127.0.0.1',9002))

while True:
	print '服务器说：',ke_obj.recv(1024)
	data = raw_input('>')
	return ke_obj.send(data)
		

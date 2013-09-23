#coding:utf8
#客户端

import socket
import threading

ke_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ke_obj.connect(('127.0.0.1',9002))

name = raw_input('filename:')
filedata = open(name,'r').read()
ke_obj.send(name)
print ke_obj.recv(1024)
ke_obj.send(filedata)
print ke_obj.recv(1024)

		

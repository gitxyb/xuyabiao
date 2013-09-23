#/usr/bin/python
#coding:utf8
import socket
import threading

kehu_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

kehu_obj.connect(("127.0.0.1",9003))

def r():
	while True:
		print " 服务器端说：",kehu_obj.recv(1024)

def s():
	while True:
		data = raw_input("客户端说：")
		kehu_obj.send(data)

th1 = threading.Thread(target=r)
th2 = threading.Thread(target=s)

th1.start()
th2.start()
th1.join()
th2.join()


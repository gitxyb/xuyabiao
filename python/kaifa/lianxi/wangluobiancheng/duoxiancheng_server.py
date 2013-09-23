#/usr/bin/python
#coding:utf8
import socket
import threading

IP = "127.0.0.1"
POTH = 9003
sh =1024

server_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_obj.bind((IP,POTH))

server_obj.listen(5)

conn,addr = server_obj.accept()

print "从 %s 获得的连接" % addr[0]
conn.send('welcome to server:')

def r():
	while True:
		print "客户端说：",conn.recv(sh)

def s():
	while True:
		data = raw_input("服务器说：")
		conn.send(data)

th1 = threading.Thread(target = r)
th2 = threading.Thread(target = s)

th1.start()
th2.start()
th1.join()
th2.join()


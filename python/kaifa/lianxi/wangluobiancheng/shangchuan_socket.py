#coding:utf8
import socket
import threading

server_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)	#生成一个socket对象

server_obj.bind(('127.0.0.1',9002))	#绑定地址

server_obj.listen(10)	#监听

conn,addr = server_obj.accept() #等待接受	conn通讯句柄；addr是ip、端口号

print "从 %s 获得链接" % addr[0]
conn.send("welcome to my server:")	#客户端发送


filename = conn.recv(1024) #接收
filepath = './' + filename
conn.send(filepath)


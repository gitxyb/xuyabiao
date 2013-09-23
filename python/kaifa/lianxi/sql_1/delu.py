#coding:utf8

import MySQLdb
from MS import MySQLCtrl

conn = MySQLdb.connect()
conn.select_db('auth')
corsor = conn.cursor()
sqli = "insert into user values (%s,%s)"
sqls = "select * from user"

def regist():
	username = raw_input('请输入用户：')
	passwd1 = raw_input('请输入密码：')
	passwd2 = raw_input('请重新输入密码：')
	return (username,passwd2)

def login():
	username = raw_input('请输入用户：')
	passwd = raw_input('请输入密码：')
	return (username,passwd)

x = raw_input('请选择登陆：y/n:')
if x == 'n':
	t = regist()
	if corsor.execute(sqli,t):
		conn.commit()
		print "ok"
else:
	name,passwd = login()
	n = corsor.execute(sqls)
	for username,userpasswd in corsor.fetchmany(n):
		if name==username and passwd == userpasswd:
			print "welcome %s to login!" % username

corsor.close()
conn.close()

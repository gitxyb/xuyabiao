#coding:utf8

import MySQLdb

class MySQlCtrl(object):


	def __init__(self,user,host):
		self.user = user 
		self.host = host
		self.conn = MySQLdb.connect(user=self.user,host=self.host)
		self.conn.select_db('auth')
		self.cursor = self.conn.cursor()

	def insert(self,name,passwd):
		self.name = name
		self.passwd = passwd
		self.cursor.execute("insert into user values(%s,%s)" ,(self.name,self.passwd))
		return True

	def select(self):
		self.cursor.execute("select * from user")
		self.data = self.cursor.fetchall()
		return self.data,5

	def youbiao(self):
		self.chazhao()
		self.cursor
		
	def __del__(self):
		print "完成"

#coding:utf8
import time

class Hero(object):
	def __init__(self,name="xyb",hp=100,act=10):
		self.name = name
		self.hp = hp
		self.act = act

	def say(self,i):
		print "I am %s" % i
		self.hp += 1000
		print "hp = %s" % self.hp

	def up(self,j):
		print "(捡到铠甲一套穿戴上)"
		print "加载。。。"
		time.sleep(2)
		self.hp += 500
		self.act += 20
		print "称号:%s" % j,"hp:%s" % self.hp,"攻击力:%s" % self.act

	def down(self):
		print "(前方有smail boss,请小心！！！)"

	def gongji(self):
		self.hp -= 200
		self.act += 50
		print "smail boss 被消灭！攻击力：%s" % self.act,"hp:%s" % self.hp,

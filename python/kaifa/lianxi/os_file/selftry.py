#coding:utf8
class MyInputException(Exception):
	def __init__(self,length,least): #继承父类Exception的内置方法
		Exception.__init__(self)
		self.length=length
		self.least=least
try:
	s = raw_input('input something:')
	if len(s)<5:
		raise MyInputException(len(s),5)
except MyInputException,x:
	print "你输入的是 %s,长度是%s,必须至少%s" % (s,x.length,x.least)



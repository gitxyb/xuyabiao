#coding:utf8
class RenLei(object):
	name = 'ren'  #公有属性
	high = 'yirengao'  #公有属性
	__money = '5000'	#私有属性
	__init__ = '+++'	#内置属性

	class Eyes(object):
		color = "block"

	def __init__(self,name,age):		#内置方法(初始化的)
		self.name = name
		self.age = age
		print "初始化完成......"

	def __add__(self,other):	#内置方法（又叫魔术方法）
		print "++++++++++++++++++++"
		return self.age + other.age

	@classmethod	#装饰器
	def say(self,i):	#公有方法	
		print "I am running %s" % i

#	c_run = classmethod(say)	#类方法

	def __say(self):	#私有方法
		print "I have %s money" % self.__money

	@staticmethod	#装饰器
	def run(i):		#静态方法
		print "I am hungrey! %s" % i

#	b_run = staticmethod(run)	#静态方法

	def __del__(self):		#析构函数（释放的）
		print "goodbye"

if __name__ == "__main__":
	#xiao = RenLei('xiaoming',20)
	#qiang = RenLei('xiaoqiang',16)
	
	#RenLei.run('5')		#为了实现类名可调用静态方法和装饰器的作用
	#
	#qiang.run('6')		#为了实现实例化的对象可调用静态方法和装饰器的作用
	#
	#RenLei.say('50')	#为了实现类名可调用类方法和装饰器的作用
	#
	#qiang.say('100')	#为了实现类名可调用类方法和装饰器的作用
	
	#print xiao+qiang	#为了实现魔术方法
	
	yan = RenLei.Eyes()
	
	print yan.color

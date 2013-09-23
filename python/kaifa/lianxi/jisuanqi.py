#coding:utf8
from __future__ import division

#def f1(x,y):
#	return x+y
#
#def f2(x,y):
#	return x-y
#
#def f3(x,y):
#	return x*y
#
#def f4(x,y):
#	return x/y
#
#
#
#def main():
#	while 1:
#		Q = raw_input('输入w停止运算，继续进行按任意键：')
#		
#		if Q == "w":
#			break
#		x = int(raw_input("请输入数字："))
#		b = raw_input("请输入符号：")
#		y = int(raw_input("请输入数字："))
#	
#		result = {'+':f1,'-':f2,'*':f3,'/':f4}
#
#		print result.get(b)(x,y)
		
#		if b == "+":
#			print f1(x,y)
#			
#		elif b == "-":
#			print f2(x,y)
#	
#		elif b == "*":
#			print f3(x,y)
#	
#		else:
#			print f4(x,y)
#main()

#x = 1
#y = 2
#o = raw_input()
#result = {'+':x+y,'-':x-y,'*':x*y,'/':x/y}
#print result.get(o,'+ - * /')

#x = int(raw_input("请输入数字："))
#b = raw_input("请输入符号：")
#y = int(raw_input("请输入数字："))
#	
#if b == "+":
#	print f1(x,y)
#			
#elif b == "-":
#	print f2(x,y)
#	
#elif b == "*":
#	print f3(x,y)
#	
#else:
#	print f4(x,y)
while True:
	Q = raw_input('退出按w键：')

	if Q == 'w':
		break

	x = int(raw_input('请输入数字：'))
	z = raw_input('请输入符号：')
	y = int(raw_input('请输入数字：'))
	
	f1 = lambda x,y:x+y
	f2 = lambda x,y:x-y
	f3 = lambda x,y:x*y
	f4 = lambda x,y:x/y
	f5 = lambda x,y:x**y

	print {'+':f1,'-':f2,'*':f3,'/':f4,'**':f5}.get(z)(x,y)

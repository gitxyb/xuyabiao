#coding:utf8
import random

#def f():
#	a = []
#	for i in range(65,91):
#		a.append(chr(i))
#	for j in range(97,123):
#		a.append(chr(j))
#	for jj in range(10):
#		a.append(jj)
#	print random.sample(a,4)
#
#f()

def fun():
	a = []
	b = []
	for i in range(65,91):
		a.append(chr(i))
	for j in range(97,123):
		a.append(chr(j))
	for jj in range(10):
		a.append(jj)
	for ii in range(4):
		b.append(a[random.randint(0,61)])
		return b

print fun()

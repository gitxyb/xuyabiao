#coding:utf8
import os

tt = raw_input('import path:')
with open(tt,'r') as f:
	print f.read()

#try:
#	f = open(tt,'r')
#except IOError,msg:
#	print "笨蛋，没有这个文件！！！%s" % msg
	

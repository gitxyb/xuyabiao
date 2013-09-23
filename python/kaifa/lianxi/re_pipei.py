#coding:utf8
import re
#name_re = r"^[a-zA-Z0-9_][a-zA-Z0-9_][a-zA-Z0-9_]$"	#只能为3位
#name_re = r"^\w\w\w$"	#只能为3位
#name_re = r"^\w{3}$"	#只能为3位
#name_re = r"^\w{1,3}$"	#只能为1~3位
#name_re = r"^\w{0,3}$"	#为1~3位,也可以不匹配
#name_re = r"^\w{0,}$"	#为0位以上,也可以不匹配
#name_re = r"ab\w{1,100}"	#为最大匹配
#name_re = r"ab\w{1,100}?"	#为最小匹配
#name_re = r"ab\w+"	#为重复无穷多次（不包括0）
#name_re = r"ab\w*"	#为重复无穷多次（包括0）
#name_re = r"abc?"	#为"c"可有可无

#while True:
#	name = raw_input('input your name:')
#	if re.findall(name_re,name):
#		print "welcome %s" % name

name_re = re.compile(r"^\w{3}$")
while True:
	name = raw_input('input your name:')
	if name_re.findall(name):
		print "welcome %s" % name

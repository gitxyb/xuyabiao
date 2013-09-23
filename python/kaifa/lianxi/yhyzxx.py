#coding:utf8
import re

name_re = r"\w{6,15}"

a = raw_input("请输入用户名：")
if re.findall(name_re,a):
	print a
else:
	print "格式错误！！！（6~15位的字母、数字、下划线）"

b = raw_input("请输入密码：")
passwd_re = r"\w+"
password = re.compile(passwd_re)
if password.findall(b):
	print b

c = raw_input("请重新输入密码：")
passwd_re = r"\w+"
password = re.compile(passwd_re)
if password.findall(c):
	print c

d = raw_input("请输入您的邮箱：")
email_re = r"^\w+@\w+\.co?[mn]$"
email = re.compile(email_re)
if email.findall(d):
	print d


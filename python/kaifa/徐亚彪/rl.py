#coding:utf8
def regist():
	username = raw_input('请输入用户：')
	passwd1 = raw_input('请输入密码：')
	passwd2 = raw_input('请重新输入密码：')
	return (username,passwd2)

def login():
	username = raw_input('请输入用户：')
	passwd = raw_input('请输入密码：')
	return (username,passwd)

#coding:utf8

x = raw_input('login:y/n:')
if x == 'n':
	name = raw_input('please input your name:')
	passwd1 = raw_input('please input your passwd:')
	passwd2 = raw_input('please input your passwd agin:')

	print "your name is %s \nyour passwd is %s" % (name,passwd2)

	open('userinfo.txt','a').write(name+":"+passwd2+"\n")



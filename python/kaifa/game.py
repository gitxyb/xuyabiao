from MS import MySQlCtrl
import rl

mysqlobj = MySQlCtrl(user='root',host='127.0.0.1')

x = raw_input('login:y/n')
if x == 'n':
    name,passwd = rl.regist()
    if mysqlobj.insert(name,passwd):
        print "ok"
else:
    name,passwd = rl.login()
    data,n = mysqlobj.select()
    for username,userpasswd in data:
        if name==username and passwd==userpasswd:
            print "welcome %s  you have logined" % name


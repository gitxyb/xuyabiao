#coding:utf8
from herostore import Hero

print "**************"
print "*欢迎来到魔兽*"
print "**************"

user = raw_input('输入你的称号：')

player1 = Hero(name = user)

print "*|退出：exit|向前走：W|向后走：S|向右走：A|向左走：D|呐喊：say|攻击：x|*"

while 1:
	user_select = raw_input("执行你的动作:")

	if user_select == "say":
		player1.say(user)
	elif user_select == "w":
		player1.up(user)
	elif user_select == "s":
		player1.down()
	elif user_select == "x":
		player1.gongji()
	elif user_select == "exit":
		print "Good Bye"
		break

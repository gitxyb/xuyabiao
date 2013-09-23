#coding=utf8
def f(x=0,y = "tree"):
	print "树上有 %s 猴子 %s" % (x,y)
f(123)
f(5,"river")
f()
f('fire')
f(y="fire")


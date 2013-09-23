a = 100
def f():
	global a
	a = 9
	return a
f()
print a


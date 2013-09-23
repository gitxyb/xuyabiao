
def deco(func):
	def _deco(x,y):
		print "before a()"
		func(x,y)
		print "after a()"
		return func(x,y)
	return _deco

#@deco
def a(x,y):
	print "I am function"
	return x+y
print a(1,2)
a = deco(a)
print a(1,2)

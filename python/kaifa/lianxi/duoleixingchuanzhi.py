
t = (1,2)

d = {'x':1,'y':2}

def f(x,y):
	print x,y

f(*t)

f(**d)

def f(x,y,*args,**kw):
	print x,y,args,kw

f(1,2,3,4,5,6,z=8)

#coding:utf8
s = 0
for i in range(1000):
	if i%3 == 0 or i%5 == 0:
		s = s+i
print s

print sum ([ i for i in range(1000) if i%3 == 0 or i%5 == 0])


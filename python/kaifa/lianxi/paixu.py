
l = [1,3,2,4,5,6,67,8]

for i in xrange(len(l)):
	for j in xrange(i):
		if l[j] > l[j+1]:
			l[j],l[j+1] = l[j+1],l[j]
			print l


#def paixu(x):
#	s = True
#	while s:
#		print l
#		s =False
#		for i in range(len(x)-1):
#			if x[i] > x[i+1]:
#				tmp = x[i+1]
#				x[i+1] = x[i]
#				x[i] = tmp
#				s = True
#		return x
#print paixu(l)

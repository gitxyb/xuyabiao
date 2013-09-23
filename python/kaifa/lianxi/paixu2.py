s = [3,4,2,52,6,9]

for i in xrange(len(s)):
	for j in xrange(i):
		if s[j] > s[j+1]:
			s[j],s[j+1] = s[j+1],s[j]
			print s

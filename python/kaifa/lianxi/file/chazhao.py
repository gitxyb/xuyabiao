import re
import string

name_re = re.compile(r'hello')

a = open('./123.txt','r+').read()

#b = 0
#for i in name_re.findall(a):
#	b += 1
#	print b
b = (name_re.findall(a))
print b

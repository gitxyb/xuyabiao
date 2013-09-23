#!/usr/bin/python
from __future__ import division
import sys
running = True
while running:
	try:
		t = int(raw_input())
		p = int(raw_input())
	except EOFError:
		break
	print 'operator + result\n',t+p
	print 'operator - result\n',t-p
	print 'operator * result\n',t*p
	print 'operator / result\n',t/p

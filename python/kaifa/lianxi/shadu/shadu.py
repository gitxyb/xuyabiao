#!/usr/bin/python
#!-*- coding:utf-8 -*-

import os
import re

print "欢迎使用xyb杀毒软件!"

def file_names(path,name):
	for path_1,dir,files in os.walk(path):
		for filenames in files:
			if filenames.split('.')[-1] == name:
				a = open(filenames).read()
				b = r'abc'
				if re.search(b,a):
					os.remove(filenames)
			

file_names(raw_input("请输入地址："),raw_input("请输入："))



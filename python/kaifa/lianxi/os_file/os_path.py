import os 

def dirList(path):
	filelist = os.listdir(path)
	for filename in filelist:
		filepath = os.path.join(path.filename)
		if os.path.isdir(filepath):
			print filepath+'/'
			dirList(filepath)
		else:
			print filepath

dirList('/root/kaifa/lianxi/os_file')



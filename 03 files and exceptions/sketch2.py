#sketch version with letting errors occur and handling them
import os

os.chdir('/Users/lukasz/hf-python/03 files and exceptions')
data = open('sketch.txt')
print(data.readline())

data.seek(0)

#Display on screen every line of file
for each_line in data:
	try:
		(role, line_spoken) = each_line.split(':', 1)
		print(role, end='')
		print(' said: ', end='')
		print(line_spoken, end='')
	except:
		pass

data.close()

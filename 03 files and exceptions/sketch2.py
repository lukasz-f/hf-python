#sketch version with letting errors occur and handling them
#OS X version
import os

os.chdir('/Users/lukasz/hf-python/03 files and exceptions')
try:
    data = open('sketch.txt')

    #Display on screen every line of file
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except ValueError:
            pass

    data.close()
except IOError:
    print('The data file is missing!')

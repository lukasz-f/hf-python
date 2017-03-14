# sketch version with extra logic to handle exceptional situations
# Windows version
import os

os.chdir('C:\\repo-git\\hf-python\\03 files and exceptions')
if os.path.exists('sketch.txt'):  # Check if file exists
    data = open('sketch.txt')

    # Display on screen every line of file
    for each_line in data:
        if not each_line.find(':') == -1:  # Check if line contains a colon
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')

    data.close()
else:
    print('The data file is missing!')

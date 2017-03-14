data = open('sketch.txt') #Open file
data = open('sketch.txt', 'r') #Open file for reading

out = open('data.out', 'w') #Open file for writing

data.readline() #Use readline to grab a line from file

print('asdf', file=out) #Use print to write to file

data.seek(0) #Return to the start of the file

data.close() #You are done so close file

#try/except/finally
try:
    file = open('file.txt')
except IOError as err:
    print('File error: ' + str(err))
finally:
    if 'file' in locals(): #Check if file object was created
        file.close()

#try with/except
try:
    with open('file.txt') as file:
        print("It's...", file=file)
except IOError as err:
    print('File error: ' + str(err))

#Open file, readline and close file
with open('sketch.txt') as data:
    data.readline()

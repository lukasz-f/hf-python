'''Athelets module with sanitizing with list comprehension'''


def sanitize(time_sting):
    if '-' in time_sting:
        splitter = '-'
    elif ':' in time_sting:
        splitter = ':'
    else:
        return time_sting

    (mins, secs) = time_sting.split(splitter)
    return mins + '.' + secs


james = []
julie = []
mikey = []
sarah = []

try:
    with open('james.txt') as james_file:
        data = james_file.readline()
    james = data.strip().split(',')

    with open('julie.txt') as julie_file:
        data = julie_file.readline()
    julie = data.strip().split(",")

    with open('mikey.txt') as mikey_file:
        data = mikey_file.readline()
    mikey = data.strip().split(',')

    with open('sarah.txt') as sarah_file:
        data = sarah_file.readline()
    sarah = data.strip().split(',')
except IOError as err:
    print('File error: ' + str(err))

clean_james = [sanitize(each_time) for each_time in james]
clean_julie = [sanitize(each_time) for each_time in julie]
clean_mikey = [sanitize(each_time) for each_time in mikey]
clean_sarah = [sanitize(each_time) for each_time in sarah]

print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))

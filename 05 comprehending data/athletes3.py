'''Athelets module with function chaining'''


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

print(sorted([sanitize(each_time) for each_time in james]))
print(sorted([sanitize(each_time) for each_time in julie]))
print(sorted([sanitize(each_time) for each_time in mikey]))
print(sorted([sanitize(each_time) for each_time in sarah]))

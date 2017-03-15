'''Athelets module with sorted and sanitized lists without lists copies'''


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
        james = james_file.readline().strip().split(',')

    with open('julie.txt') as julie_file:
        julie = julie_file.readline().strip().split(",")

    with open('mikey.txt') as mikey_file:
        mikey = mikey_file.readline().strip().split(',')

    with open('sarah.txt') as sarah_file:
        sarah = sarah_file.readline().strip().split(',')
except IOError as err:
    print('File error: ' + str(err))

for i in range(len(james)):
    james[i] = sanitize(james[i])

for i in range(len(julie)):
    julie[i] = sanitize(julie[i])

for i in range(len(mikey)):
    mikey[i] = sanitize(mikey[i])

for i in range(len(sarah)):
    sarah[i] = sanitize(sarah[i])

print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))

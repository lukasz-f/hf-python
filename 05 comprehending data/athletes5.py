'''Athelets module without duplication in lists'''


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
with open('james.txt') as james_file:
    data = james_file.readline()
james = data.strip().split(',')

julie = []
with open('julie.txt') as julie_file:
    data = julie_file.readline()
julie = data.strip().split(",")

mikey = []
with open('mikey.txt') as mikey_file:
    data = mikey_file.readline()
mikey = data.strip().split(',')

sarah = []
with open('sarah.txt') as sarah_file:
    data = sarah_file.readline()
sarah = data.strip().split(',')

james = sorted([sanitize(each_time) for each_time in james])
julie = sorted([sanitize(each_time) for each_time in julie])
mikey = sorted([sanitize(each_time) for each_time in mikey])
sarah = sorted([sanitize(each_time) for each_time in sarah])

unique_james = []
for each_time in james:
    if each_time not in unique_james:
        unique_james.append(each_time)

unique_julie = []
for each_time in julie:
    if each_time not in unique_julie:
        unique_julie.append(each_time)

unique_mikey = []
for each_time in mikey:
    if each_time not in unique_mikey:
        unique_mikey.append(each_time)

unique_sarah = []
for each_time in sarah:
    if each_time not in unique_sarah:
        unique_sarah.append(each_time)

print(unique_james[0:3])
print(unique_julie[0:3])
print(unique_mikey[0:3])
print(unique_sarah[0:3])

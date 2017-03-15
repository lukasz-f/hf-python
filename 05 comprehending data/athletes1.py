'''Simple Athelets module'''


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

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for each_time in james:
    clean_james.append(sanitize(each_time))

for each_time in julie:
    clean_julie.append(sanitize(each_time))

for each_time in mikey:
    clean_mikey.append(sanitize(each_time))

for each_time in sarah:
    clean_sarah.append(sanitize(each_time))

print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))

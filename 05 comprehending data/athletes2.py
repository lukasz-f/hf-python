'''Athelets module with sorted and sanitized lists with list comprehension'''


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

clean_james = [sanitize(each_time) for each_time in james]
clean_julie = [sanitize(each_time) for each_time in julie]
clean_mikey = [sanitize(each_time) for each_time in mikey]
clean_sarah = [sanitize(each_time) for each_time in sarah]

sorted_james = sorted(clean_james)
sorted_julie = sorted(clean_julie)
sorted_mikey = sorted(clean_mikey)
sorted_sarah = sorted(clean_sarah)

print(sorted_james)
print(sorted_julie)
print(sorted_mikey)
print(sorted_sarah)

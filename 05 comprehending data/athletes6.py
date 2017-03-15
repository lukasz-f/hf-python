'''Athelets module without duplication with set'''


def sanitize(time_sting):
    if '-' in time_sting:
        splitter = '-'
    elif ':' in time_sting:
        splitter = ':'
    else:
        return time_sting

    (mins, secs) = time_sting.split(splitter)
    return mins + '.' + secs


def get_coach_data(file_name):
    try:
        with open(file_name) as file:
            data = file.readline()
        return data.strip().split(',')
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return None


james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

james = sorted(set([sanitize(each_time) for each_time in james]))[0:3]
julie = sorted(set([sanitize(each_time) for each_time in julie]))[0:3]
mikey = sorted(set([sanitize(each_time) for each_time in mikey]))[0:3]
sarah = sorted(set([sanitize(each_time) for each_time in sarah]))[0:3]

print(james)
print(julie)
print(mikey)
print(sarah)

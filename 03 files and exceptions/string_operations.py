str = ' asdf:fdsa:asdf '

# s = '!!!!!''
s = "!" * 5

# s = 'hellothere'
s = 'hello' + 'There'

# s = 'helloThere!'
s += '!'

# Get s length
len(s)

# Sliceing
str[2]    # Return third letter from str
str[2:4]  # Return third and fourth letter from str
str[1:]   # Return string without first letter
str[-1]   # Return last letter
str[-4]   # Return 4th from the end
str[:-3]  # Substring not including last 3 chars
str[-3:]  # Return last 3 chars
'Hello world'[::-1]  # Reverse string

# Remove whitespace from the leading and trailing
str.strip()
':asdf:'.strip(':')  # Remove ':'
':asdf.'.strip('.:')  # Remove ':' and '.'
'radar'.strip('ra')  # Remove 'ra' and 'ar'

str.lstrip()  # Remove from the leading
str.rstrip()  # Remove from the trailing

# Finding with 'in' operator
print('asdf' in str)
print('asdf' not in str)

# Returns the lowercase or uppercase version of the string
s.lower()  # 'hellothere!'
s.upper()  # 'HELLOTHERE!''
s.swapcase()  # 'HELLOtHERE!'
s.capitalize()  # 'Hellothere!'

# Tests if all the string chars are in the various character classes
s.isalpha()
s.isdigit()
s.isspace()

str.count('a')  # Number of 'a' occurrences: 3

# Tests if the string starts or ends with the given other string
s.startswith('other')  # s.startswith(prefix[, start[, end]])
s.endswith('other')  # s.endswith(prefix[, start[, end]])

# Searches for the given other string (not a regular expression) within s,
# and returns the first index where it begins or -1 if not found
s.find('other')
str.find(':')  # 4
str.find('!')  # -1

# Returns a string where all occurrences of 'old' have been replaced by 'new'
s.replace('old', 'new')

# Returns a list of substrings separated by the given delimiter.
# The delimiter is not a regular expression, it's just text.
# split() with no arguments splits on all whitespace chars.
s.split('delim')
str.split(':')              # ['asdf', 'fdsa', 'asdf']
(a, b) = str.split(':', 1)  # ['asdf', 'fdsa:asdf']
'aaa,bbb,ccc'.split(',')    # ['aaa', 'bbb', 'ccc']
'aaa bbb  ccc'.split(' ')    # ['aaa', 'bbb', '', 'ccc']
'aaa bbb  ccc'.split()    # ['aaa', 'bbb', 'ccc']

# Opposite of split(), joins the elements in the given list together
# using the string as the delimiter
s.join(list())
'---'.join(['aaa', 'bbb', 'ccc'])  # aaa---bbb---ccc
''.join(reversed('Hello world'))  # Reverse string

# % operator
text = ("%d little pigs come out or I'll %s and %s and %s" %
        (3, 'huff', 'puff', 'blow down'))
txt = '%d int, %s string, %f/%g floating point' % (1, '1', 1.1, 1.1)

hash = {'word': 'garfield', 'count': 42}
s = 'I want %(count)d copies of %(word)s' % hash

# {} operator
t = '{}={}'.format('a', 1)  # 'a=1'

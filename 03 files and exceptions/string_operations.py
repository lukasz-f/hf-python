str = ' asdf:fdsa:asdf '

# s = '!!!!!''
s = "!" * 5

# s = 'hellothere'
s = 'hello' + 'there'

# s = 'hellothere!'
s += '!'

# Get s length
len(s)

# Return third letter from str
str[2]

# Return third and fourth letter from str
str[2:4]

# Remove whitespace from the leading and trailing
str.strip()

# Finding with 'in' operator
print('asdf' in str)
print('asdf' not in str)

# Returns the lowercase or uppercase version of the string
s.lower()
s.upper()

# Tests if all the string chars are in the various character classes
s.isalpha()
s.isdigit()
s.isspace()

# Tests if the string starts or ends with the given other string
s.startswith('other')
s.endswith('other')

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
'aaa bbb ccc'.split()    # ['aaa', 'bbb', 'ccc']

# Opposite of split(), joins the elements in the given list together
# using the string as the delimiter
s.join(list)
'---'.join(['aaa', 'bbb', 'ccc'])  # aaa---bbb---ccc

# Create empty dictionary
dict = {}

# Add to dictionary 3 elements
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'

# Create dictionary with 3 elements
dict = {'a': 'alpha', 'g': 'gamma', 'o': 'omega'}

# Get 'a' element
dict['a']
dict.get('a')

# Iterates over keys
for key in dict:
    print(key)
for key in dict.keys():
    print(key)

# Iterates over values
for value in dict.values():
    print(value)

for k, v in dict.items():
    print(k + ' ' + v)

# .items() is the dict expressed as (key, value) tuples
print(dict.items())  # [('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')]

# Check key in dictionary
'a' in dict

d = {'a': 1, 'b': 2, 'c': 3}

# Dictionary comprehension
{v: k for k, v in d.items()}

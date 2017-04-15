# Returns an iterator that generates numbers in a specified range on demand
# and as needed
range(10)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
range(1, 11)  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
range(10, 0, -1)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

# Creates a numbered list of paired-data, starting from 0
enumerate(['a', 'c', 'd'])
for i, element in enumerate([5, 2, 8, 0]):
    print(i, element)

int()  # Factory function that creates a integer with value 0
int('1')  # Converts a strings or another number to an integer (if possible)
int(True)  # 1

str()  # Factory function that creates a new, empty string
str(1)  # Converts values to a string (if possible)
str(True)  # 'True'

id(None)  # Returns the unique identification for a Python data object
str = 'abc'
id(str)  # 4320935640
str += 'd'  # string jest immutable
id(str)  # 4385020480

next()  # Returns the next item form a iterable data structure such as a list

float()  # Converts to floating point
float('2.22')

bool()  # Factory function that creates a boolean with value False
bool(2)  # Coverts int to boolean True
bool(0)  # False
bool('')  # False
bool('a')  # True

complex(1)  # 1+0j
complex(1, 1) # 1+1j

type(1)  # Zwraca typ zmiennej
a = 'a'
type(a)

# Lista
list()  # Factory function that creates a new, empty list
list(range(4))  # [0, 1, 2, 3]
list('asdf')  # ['a', 's', 'd', 'f']

# Zbiór
set()  # Factory function that creates new empty set
set([1, 2, 1])  # Set removes duplications

# Słownik
dict()
d1 = {}  # Utworzenie pustego slownika
d2 = {'a': 1}  # Utworzenie jednoelementowego slownika

# Krotka (immutable list)
tuple()
t1 = ((),)  # Utworzenie pustej krotki
t2 = (1,)  # Utworzenie jednoelementowej krotki
t3 = (1, 2)  # Utworzenie dwuelementowej krotki

max([1, 11, 111])  # 111

round(2.111)  # 2
round(2.111, 1)  # 2.1

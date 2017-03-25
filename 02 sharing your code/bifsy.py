list()      # Factory function that creates a new, empty list

# Returns an iterator that generates numbers in a specified range on demand
# and as needed
range()
range(10)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
range(1, 11)  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
range(10, 0, -1)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
list(range(4))

enumerate()  # Creates a numbered list of paired-data, starting from 0

int()  # Converts a strings or another number to an integer (if possible)

str()  # Converts values to a string (if possible)

id()  # Returns the unique identification for a Python data object

next()  # Returns the next item form a iterable data structure such as a list

float()  # Converts to floating point
float('2.22')

set()  # Factory function that creates new empty set
set([1, 2, 1])  # Set removes duplications

type(1)  # Zwraca typ zmiennej
a = 'a'
type(a)

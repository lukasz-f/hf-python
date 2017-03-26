locals()  # Zwraca słownik z nazwami i wartościami lokalnych zmiennych

# Remove definition of variable.
# Delete part of the list and entries from dictionaries.
del()
var = 6
del(var)  # var no more!

list = ['a', 'b', 'c', 'd']
del(list[0])  # Delete first element

dict = {'a': 1, 'b': 2, 'c': 3}
del(dict['b'])  # Delete 'b' entry

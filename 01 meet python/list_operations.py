# Utworzenie listy imion
cast = ["Cleese", 'Palin', 'Jones', "Idle"]

# Wyświetlenie listy
print(cast)

# Wyświetlenie długości listy
print(len(cast))

# Wyświetlenie pojedynczego elementu listy
print(cast[1])

# Wyświetlenie elementów o indeksach 0, 1, 2
print(cast[0:3])

# Nie tworzy kopii. Obie zmienne wskazują na tą samą listę
a = cast

# Tworzy kopie listy
b = cast[:]
c = list(cast)

# Dodanie elementu na koniec listy
cast += ['Gilliam']
cast.append('Gilliam')
print(cast)

# Dodanie kilku elementów na koniec listy
cast += ["Gilliam", "Chapman"]
cast.extend(["Gilliam", "Chapman"])
print(cast)

# Różnica między 'append' a 'extend'
lista = [0]
lista.append(['a', 'b'])
lista.extend(['c', 'd'])
print(lista)

# Dodanie elementu przed podanym indeksem
cast.insert(0, "Chapman")
print(cast)

# Usunięcie ostatniego elementu
cast.pop()
del(cast[-1])
print(cast)

# Removes and returns the element at the given index. Returns the rightmost
# element if index is omitted (roughly the opposite of append())
cast.pop(0)
print(cast)

# Znalezienie i usunięcie pierwszego odnalezionego elementu
cast.remove("Chapman")
print(cast)

# Usuniecie kilku elementow
del(cast[-2:])
print(cast)

# In-place sorting. Arrange in the order and replace original data
cast.sort()
print(cast)
cast.sort(reverse=True)
print(cast)

# Copied sorting. Returns a sorted copy of original data
sorted([2, 3, 1])
sorted([2, 3, 1], reverse=True)

strs = ['CCC', 'aaaa', 'd', 'bb']
sorted(strs)  # ['CCC', 'aaaa', 'bb', 'd']
sorted(strs, key=len)  # ['d', 'bb', 'CCC', 'aaaa']
sorted(strs, key=str.lower)  # ['aaaa', 'bb', 'CCC', 'd']

# Finding with 'in' operator
print('Cleese' in cast)
print('Cleese' not in cast)

# List comprehension. Create a new list by applying a transformation to each
# data item within existing list
print([each_name.upper() for each_name in cast])
[m * 60 for m in [1, 2, 3]]
[n for n in [2, 8, 1, 6] if n <= 2]  # [2, 1]

# Searches for the given element from the start of the list and returns its
# index. Throws a ValueError if the element does not appear.
cast.index('Palin')

[1, 2, 3, 4, 1, 5, 6, 1].count(1)  # Number of number 1 occurrences: 3

# Reverses the list in place (does not return it)
cast.reverse()

# Slices
letters = ['a', 'b', 'c', 'd']
letters[1:-1]  # ['b', 'c']
letters[::2]  # ['a', 'c']

# Changing list elements
letters[0] = 'A'  # ['A', 'b', 'c', 'd']
letters[2:4] = ['d', 'c']  # ['A', 'b', d', 'c']
letters[2:4] = 'z'  # ['A', 'b', 'z']

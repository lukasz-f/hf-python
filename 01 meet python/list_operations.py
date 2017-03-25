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

# Dodanie elementu na koniec listy
cast.append("Gilliam")
print(cast)

# Usunięcie ostatniego elementu
cast.pop()
print(cast)

# Dodanie kilku elementów na koniec listy
cast.extend(["Gilliam", "Chapman"])
print(cast)

# Różnica między ‚append’ a ‚extend’
cast.append(['a', 'b'])
print(cast)
cast.pop()

cast.extend(['a', 'b'])
print(cast)
cast.pop()
cast.pop()
print(cast)

# Znalezienie i usunięcie elementu
cast.remove("Chapman")
print(cast)

# Dodanie elementu przed podanym indeksem
cast.insert(0, "Chapman")
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

# Slices
list = ['a', 'b', 'c', 'd']
list[1:-1]  # ['b', 'c']
list[::2]  # ['a', 'c']
list[0:2] = 'z'  # replace ['a', 'b'] with ['z']

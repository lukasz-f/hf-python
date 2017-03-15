# Utworzenie listy imion
cast = ["Cleese", 'Palin', 'Jones', "Idle"]

# Wyświetlenie listy
print(cast)

# Wyświetlenie długości listy
print(len(cast))

# Wyświetlenie pojedynczego elementu listy
print(cast[1])

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

# Finding with 'in' operator
print('Cleese' in cast)
print('Cleese' not in cast)

# List comprehension. Create a new list by applying a transformation to each
# data item within existing list
print([each_name.upper() for each_name in cast])
print([m * 60 for m in [1, 2, 3]])

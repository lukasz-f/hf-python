# BIF = built-in function
import sys

# Wszystkie BIFs
dir(__builtins__)  # __builtins__ to namespace

# Informacje o BIF
help(print)

# Wyświetlanie linii tekstu na ekranie
print('asdf')
# Wyświetlanie linii tekstu na ekranie
print('asdf', sep=' ', end='\n', file=sys.stdout)
# Wyświetlenie znaku a (bez przejścia do nowej linii)
print('a', end='')

# Zapis do pliku
out = open('data.out', 'w')
print('a', file=out)

# Obliczenie wielkości listy
cast = ["Cleese", 'Palin', 'Jones', "Idle"]
len(cast)

# Sprawdzenie czy zmienna jest listą
isinstance(cast, list)
num_names = len(cast)
isinstance(num_names, list)

# Copied sorting. Returns a sorted copy of original data
sorted([2, 3, 1])
sorted([2, 3, 1], reverse=True)

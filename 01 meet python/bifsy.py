#BIF = built-in function

#Wszystkie BIFs
dir(__builtins__) #__builtins__ to namespace

#Informacje o BIF
help(print)

print('asdf') 		#Wyświetlanie linii tekstu na ekranie
print('a', end='') 	#Wyświetlenie znaku a (bez przejścia do nowej linii)

#Obliczenie wielkości listy
cast = ["Cleese", 'Palin', 'Jones', "Idle"]
len(cast)

#Sprawdzenie czy zmienna jest listą
isinstance(cast, list)
num_names = len(cast)
isinstance(num_names, list)


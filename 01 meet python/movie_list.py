#Lista filmów
movies = ["the Holy Grail", "The Life of Brian", "The Meaning of Life"]

#Wstawienie daty nakręcenia filmów
movies.insert(1, 1975)
movies.insert(3, 1979)
movies.append(1983)
print(movies)

#Iteracja po liście
for movie in movies:
	print(movie)

#Zagnieżdżone listy
movies=["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
print(movies)
print(movies[4][1][3])

#Iteracja po liście list
for each_item in movies:
	print(each_item)

#Iteracja po liście list 2
for each_item in movies:
	if isinstance(each_item, list):
		for nested_item in each_item:
			if isinstance(nested_item, list):
				for deeper_item in nested_item:
					print(deeper_item)
			else:
				print(nested_item)
	else:
		print(each_item)

movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]

# Pętla for
for movie in movies:
    print(movie)

# Pętla while
count = 0
while count < len(movies):
    print(movies[count])
    count = count + 1

# Pętla for z licznikiem.
for i in range(4):
    print(i)        # Wyświetla 0, 1, 2, 3

# List comprehension. Create a new list by applying a transformation to each
# data item within existing list
movies_upper = [m.upper() for m in movies]
print(movies_upper)

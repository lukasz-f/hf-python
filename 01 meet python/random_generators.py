import random
import string

# Random integers
random.randint(1, 5)  # [1, 5]

# Random real value
random.random()  # [0.0, 1.0)

# Functions for sequences
random.choice('asdf')  # Random letter from 'a' to 'f'
random.choice(string.ascii_letters)  # Random letter from 'a' to 'Z'
random.choices('asdf', k=10)  # 10 random letters from 'a' to 'f'
random.sample(string.ascii_letters, 5)  # Random unique 5 letters
random.sample(range(100), 5)  # Random unique 5 numbers
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(x)  # Shuffled list

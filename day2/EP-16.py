#solution to task given in EP - 9

# Pattern 1
for i in range(1, 6):
    print('*' * i)

print("\n\n")
# Pattern 2
for i in range(1, 6):
    spaces = ' ' * (5 - i) # Calculate leading spaces
    stars = '*' * (2 * i - 1) # Calculate stars
    print(spaces + stars)

print("\n\n")

# Pattern 3
for i in range(5):
    print('*' * 5)

print("\n\n")

# Pattern 4
for i in range(1, 6):
    spaces = ' ' * (5 - i) # Calculate leading spaces
    stars = '*' * (2 * i - 1) # Calculate stars
    print(spaces + stars)

for i in range(4, 0, -1):
    spaces = ' ' * (5 - i) # Calculate leading spaces
    stars = '*' * (2 * i - 1) # Calculate stars
    print(spaces + stars)

print("\n\n")

# Pattern 5
for i in range(5, 0, -1):
    spaces = ' ' * (5 - i) # Calculate leading spaces
    stars = '*' * (2 * i - 1) # Calculate stars
    print(spaces + stars)

for i in range(2, 6):
    spaces = ' ' * (5 - i) # Calculate leading spaces
    stars = '*' * (2 * i - 1) # Calculate stars
    print(spaces + stars)


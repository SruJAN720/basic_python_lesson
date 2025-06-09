

# Demonstrating the break statement
for i in range(1, 3):
    if i == 3:
        print("Breaking the loop at i =", i)
        break
    print("Inside the loop, i =", i)
else:
    print("Loop finished without encountering a break statement.")


# Demonstrating the continue statement
for i in range(1, 6):
    if i == 4:
        print("Skipping iteration at i =", i)
        continue
    print("Inside the loop, i =", i)




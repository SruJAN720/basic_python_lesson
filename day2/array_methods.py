colors = ["red", "orange", "yellow", "green", "blue"]

colors.append("indigo")     # Add new color
colors.append("violet")     # Add new color
colors.remove("blue")       # Remove one color
last_color = colors.pop()   # Remove the last item and store it
colors.pop(2)               # Remove the item located at position 2
position = colors.index("red")  # Find where "red" is

print(colors)
print("Last color was:", last_color)
print("Red is at position:", position)

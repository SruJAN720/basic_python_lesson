colors = ["red", "blue", "green"]

colors.append("yellow")     # Add new color
colors.remove("blue")       # Remove one color
last_color = colors.pop()   # Remove the last item and store it
position = colors.index("red")  # Find where "red" is

print(colors)
print("Last color was:", last_color)
print("Red is at position:", position)

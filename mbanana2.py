import turtle
import time
import math

# Set up screen
screen = turtle.Screen()
screen.title("CodeMonkey-Style Monkey Chasing Banana")
screen.bgcolor("lightgreen")
screen.setup(width=800, height=600)

# Register custom images
screen.addshape("monkey.gif")   # Make sure this image exists
screen.addshape("banana.gif")   # Make sure this image exists

# Create monkey turtle
monkey = turtle.Turtle()
monkey.shape("monkey.gif")
monkey.penup()
monkey.goto(-350, -50)

# Create banana turtle
banana = turtle.Turtle()
banana.shape("banana.gif")
banana.penup()
banana.goto(200, -50)

# Smooth monkey movement function
def move_monkey_to_banana():
    while monkey.xcor() < banana.xcor() - 10:
        # Move in small steps
        new_x = monkey.xcor() + 5

        # Add a bounce effect for legs (simulate walking)
        bounce = 10 * math.sin(new_x / 15)

        monkey.goto(new_x, -50 + bounce)
        time.sleep(0.03)

    # Celebrate reaching the banana
    monkey.write("Yum!", align="left", font=("Arial", 18, "bold"))

# Run the animation
move_monkey_to_banana()

# Keep the window open
screen.mainloop()


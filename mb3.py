import turtle
import time
import math

# --- Setup Screen ---
screen = turtle.Screen()
screen.title("Monkey Eats Banana - CodeMonkey Style")
screen.bgcolor("lightgreen")
screen.setup(width=800, height=600)

# --- Register Images ---
screen.addshape("monkey.gif")   # Ensure this file exists
screen.addshape("banana.gif")   # Ensure this file exists

# --- Create Banana (drawn first, so it's under) ---
banana = turtle.Turtle()
banana.shape("banana.gif")
banana.penup()
banana.goto(200, -50)

# --- Create Monkey (drawn after banana, appears on top) ---
monkey = turtle.Turtle()
monkey.shape("monkey.gif")
monkey.penup()
monkey.goto(-350, -50)

# --- Smooth Movement Function ---
def move_monkey_to_banana():
    while monkey.xcor() < banana.xcor() - 10:
        new_x = monkey.xcor() + 5
        bounce = 10 * math.sin(new_x / 15)
        monkey.goto(new_x, -50 + bounce)
        time.sleep(0.03)

    # Banana disappears
    banana.hideturtle()

    # Monkey reacts
    monkey.write("Yum!", align="left", font=("Arial", 18, "bold"))

# --- Run Animation ---
move_monkey_to_banana()

# --- Keep Window Open ---
screen.mainloop()


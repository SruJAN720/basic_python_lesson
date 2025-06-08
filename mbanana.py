import turtle
import time

# Set up screen
screen = turtle.Screen()
screen.title("Monkey Chasing Banana")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)

# Add image shapes
screen.addshape("monkey.gif")
screen.addshape("banana.gif")

# Create monkey turtle
monkey = turtle.Turtle()
monkey.shape("monkey.gif")
monkey.penup()
monkey.goto(-300, 0)

# Create banana turtle
banana = turtle.Turtle()
banana.shape("banana.gif")
banana.penup()
banana.goto(200, 0)

# Movement function
def move_monkey():
    while monkey.xcor() < banana.xcor() - 10:
        x = monkey.xcor() + 5
        monkey.setx(x)
        time.sleep(0.05)  # delay for animation effect

# Start animation
move_monkey()

# Keep the window open
screen.mainloop()


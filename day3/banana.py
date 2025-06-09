import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("skyblue")
screen.tracer(0)

# Monkey
monkey = turtle.Turtle()
monkey.speed(0)
monkey.penup()
monkey.shape("square")
monkey.color("brown")
monkey.shapesize(stretch_len=2, stretch_wid=2)
monkey.goto(-200, 0)

# Banana
banana = turtle.Turtle()
banana.speed(0)
banana.penup()
banana.shape("circle")
banana.color("yellow")
banana.shapesize(stretch_len=1, stretch_wid=1)
banana.goto(200, 0)

# Animation
def move_monkey():
    if monkey.xcor() < banana.xcor():
        monkey.forward(2)
        screen.update()
        time.sleep(0.01)
        move_monkey()

move_monkey()
turtle.done()

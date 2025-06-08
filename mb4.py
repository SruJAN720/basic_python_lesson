import turtle
import time
import math
import pygame  # For playing music

# --- Initialize Pygame for sound ---
pygame.mixer.init()
pygame.mixer.music.load("mb.mp3")
pygame.mixer.music.play(-1)  # -1 means loop forever

# --- Setup Screen ---
screen = turtle.Screen()
screen.title("Monkey Eats Banana - With Music")
screen.bgcolor("lightgreen")
screen.setup(width=800, height=600)

# --- Register Images ---
screen.addshape("monkey.gif")
screen.addshape("banana.gif")

# --- Create Banana ---
banana = turtle.Turtle()
banana.shape("banana.gif")
banana.penup()
banana.goto(200, -50)

# --- Create Monkey ---
monkey = turtle.Turtle()
monkey.shape("monkey.gif")
monkey.penup()
monkey.goto(-350, -50)

# --- Move Monkey Function ---
def move_monkey_to_banana():
    time.sleep(0.05)
    while monkey.xcor() < banana.xcor() - 10:
        time.sleep(0.03)
        new_x = monkey.xcor() + 5
        bounce = 10 * math.sin(new_x / 15)
        monkey.goto(new_x, -50 + bounce)
        time.sleep(0.03)

    banana.hideturtle()
    monkey.write("Yum!", align="left", font=("Arial", 18, "bold"))

# --- Start Animation ---
move_monkey_to_banana()

# --- Keep Window Open ---
screen.mainloop()

# --- Stop music when window closes (optional) ---
pygame.mixer.music.stop()


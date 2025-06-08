import turtle
import time
import math
import pygame  # For music

# --- Initialize Pygame ---
pygame.mixer.init()
pygame.mixer.music.load("monkey_music.mp3")
pygame.mixer.music.play(-1)

# --- Setup Screen ---
screen = turtle.Screen()
screen.title("Monkey Eats Banana - Y2L Academy Demo")
screen.bgcolor("lightgreen")
screen.setup(width=800, height=600)

# --- Register Shapes ---
screen.addshape("monkey.gif")
screen.addshape("banana.gif")

# --- Caption Turtle (for text at top) ---
caption = turtle.Turtle()
caption.hideturtle()
caption.penup()
caption.goto(0, 250)  # Top of screen
caption.color("darkblue")
caption.write(
    "Want to learn Python coding fundamentals the fun and easy way?\nAttend our demo class!",
    align="center",
    font=("Arial", 18, "bold")
)

# --- Sub-caption ---
details = turtle.Turtle()
details.hideturtle()
details.penup()
details.goto(0, 220)
details.color("black")
details.write(
    "For details, contact: y2lacademy.com",
    align="center",
    font=("Arial", 14, "normal")
)

# --- Banana Turtle ---
banana = turtle.Turtle()
banana.shape("banana.gif")
banana.penup()
banana.goto(200, -50)

# --- Monkey Turtle ---
monkey = turtle.Turtle()
monkey.shape("monkey.gif")
monkey.penup()
monkey.goto(-350, -50)

# --- Move Monkey Function ---
def move_monkey_to_banana():
    time.sleep(5)  # Wait 5 seconds before movement
    while monkey.xcor() < banana.xcor() - 10:
        new_x = monkey.xcor() + 5
        bounce = 10 * math.sin(new_x / 15)
        monkey.goto(new_x, -50 + bounce)
        time.sleep(0.03)

    banana.hideturtle()
    monkey.write("Yum!", align="left", font=("Arial", 18, "bold"))

# --- Run Animation ---
move_monkey_to_banana()

# --- Keep Window Open ---
screen.mainloop()

# --- Stop Music (optional) ---
pygame.mixer.music.stop()


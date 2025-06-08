import turtle
import time
import math
import pygame

# --- Initialize Music ---
pygame.mixer.init()
pygame.mixer.music.load("monkey_music.mp3")
pygame.mixer.music.play(-1)

# --- Setup Fullscreen Screen ---
screen = turtle.Screen()
screen.title("Y2L Academy - Fun Python Learning Demo")
screen.bgcolor("lightgreen")
screen.setup(width=1.0, height=1.0)  # Fullscreen

# --- Register Shapes ---
screen.addshape("monkey.gif")
screen.addshape("banana.gif")
#screen.addshape("qr.png")  # QR code image

# --- Caption Turtle ---
caption = turtle.Turtle()
caption.hideturtle()
caption.penup()
caption.goto(0, 300)
caption.color("darkblue")
caption.write(
    "Want to learn Python coding fundamentals the fun and easy way?\nAttend our demo class!",
    align="center",
    font=("Arial", 24, "bold")  # Larger font
)

# --- Sub-caption ---
details = turtle.Turtle()
details.hideturtle()
details.penup()
details.goto(0, 260)
details.color("black")
details.write(
    "For details, contact: y2lacademy.com",
    align="center",
    font=("Arial", 20, "normal")
)

# --- QR Code ---
#qr = turtle.Turtle()
#qr.shape("qr.gif")
#qr.penup()
#qr.goto(300, -200)

# --- QR Label ---
qr_label = turtle.Turtle()
qr_label.hideturtle()
qr_label.penup()
qr_label.goto(300, -270)
qr_label.color("black")
qr_label.write("SignUp here : https://tinyurl.com/49kma5t9 ", align="center", font=("Arial", 16, "bold"))

# --- Banana ---
banana = turtle.Turtle()
banana.shape("banana.gif")
banana.penup()
banana.goto(200, -50)

# --- Monkey ---
monkey = turtle.Turtle()
monkey.shape("monkey.gif")
monkey.penup()
monkey.goto(-350, -50)

# --- Animation ---
def move_monkey_to_banana():
    time.sleep(10)  # 5-second delay
    while monkey.xcor() < banana.xcor() - 10:
        new_x = monkey.xcor() + 5
        bounce = 10 * math.sin(new_x / 15)
        monkey.goto(new_x, -50 + bounce)
        time.sleep(0.03)

    banana.hideturtle()
    monkey.write("Yum!", align="left", font=("Arial", 18, "bold"))

# --- Start ---
move_monkey_to_banana()
screen.mainloop()
pygame.mixer.music.stop()


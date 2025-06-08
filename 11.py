import turtle

t = turtle.Turtle()
t.pensize(3)
t.color("blue")

# Draw a square
for i in range(4):
    t.forward(100)
    t.right(90)

turtle.done()


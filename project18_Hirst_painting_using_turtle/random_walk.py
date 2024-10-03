import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

timmy.shape("turtle")
timmy.pensize(10)
timmy.speed(9)


directions = [0,90,180,270]

for _ in range(200):
    timmy.fd(30)
    timmy.setheading(random.choice(directions))
    timmy.color(random_colour())

screen = t.Screen()
screen.exitonclick()
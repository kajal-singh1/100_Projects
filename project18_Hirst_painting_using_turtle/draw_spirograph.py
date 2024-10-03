import turtle as t
import random as rn

timmy = t.Turtle()
t.colormode(255)
timmy.speed('fastest')

def rand_color():
    r = rn.randint(0,255)
    g = rn.randint(0,255)
    b = rn.randint(0,255)
    return (r, g, b)

def spirograh(angle):
    for i in range(int(360/angle)):
        timmy.pensize(2)
        timmy.color(rand_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+angle)

spirograh(5)








screen = t.Screen()
screen.exitonclick()
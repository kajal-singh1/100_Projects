from turtle import Turtle, Screen
import random

timmy = Turtle()

timmy.shape("turtle")

for tri in range(3):
    timmy.up(100)
    timmy.r(120)
    
for sq in range(4):
    timmy.fd(100)
    timmy.rt(90)

for sq in range(5):
    timmy.fd(100)
    timmy.rt(72)

for sq in range(6):
    timmy.fd(100)
    timmy.rt(60)

for sq in range(7):
    timmy.fd(100)
    timmy.rt(51.4285)

for sq in range(8):
    timmy.fd(100)
    timmy.rt(45)

for sq in range(9):
    timmy.fd(100)
    timmy.rt(40)

for sq in range(10):
    timmy.fd(100)
    timmy.rt(36)


#More Good Way
colours = ["red" , "green", "blue", "chocolate", "dark green","dark green","orange red","medium violet red","gold","navy"]

def draw_shape(no_of_sides):
    angle = 360/no_of_sides
    for _ in range(no_of_sides):
        timmy.fd(100)
        timmy.rt(angle)
for shape_n in range(3, 11):
    timmy.color(random.choice(colours))
    draw_shape(shape_n)

screen = Screen()
screen.exitonclick()
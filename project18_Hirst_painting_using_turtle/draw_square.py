from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

timmy.shape("turtle")

for _ in range(4):
    timmy.fd(100)
    timmy.rt(90)



screen = Screen()
screen.exitonclick()
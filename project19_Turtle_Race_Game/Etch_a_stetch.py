from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
timmy.speed("fastest")


def move_forward():
    timmy.fd(100)


def move_backward():
    timmy.bk(100)


def move_counter_clockwise():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)

def move_clockwise():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


def clearr():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()



screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clearr)










screen.exitonclick()
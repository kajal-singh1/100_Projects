# import colorgram

# rgb_color = []
# colors = colorgram.extract('hirst.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)

# print(rgb_color)
import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
color_list = [ (215, 166, 17),  (205, 153, 99), (225, 205, 103), (161, 55, 101), (113, 187, 213), (154, 31, 58), (8, 109, 166), (42, 13, 24), (160, 29, 25), (12, 23, 52), (34, 122, 62), (59, 23, 18), (9, 32, 26), (186, 156, 173), (63, 166, 88), (171, 57, 42), (156, 208, 215), (94, 183, 167), (205, 99, 95), (240, 200, 3), (213, 174, 198), (28, 37, 105), (187, 99, 110), (163, 209, 197), (220, 177, 173), (14, 105, 56)]

timmy.setheading(255)
timmy.fd(300)
timmy.setheading(0)
num_of_dots = 100

for count in range(1, num_of_dots+1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)






screen = t.Screen()
screen.exitonclick()
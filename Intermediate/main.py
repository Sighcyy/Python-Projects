import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract("image.jpg", 225)
rgb_colors = []
for color  in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


screen = Screen()
tim = Turtle()
tim.penup()
screen.colormode(255)
tim.speed("fastest")
tim.hideturtle()


i = -300

for _ in range(14):
    tim.setposition(-300, i)
    for _ in range(13):
        tim.dot(30, random.choice(rgb_colors))
        tim.forward(50)
    i = i + 50


screen.exitonclick()
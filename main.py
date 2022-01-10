import colorgram
from turtle import Screen, Turtle

turtle = Turtle()
screen = Screen()
screen.colormode(255)

num_color = 10
colors = colorgram.extract('danielhirstpainting.jpg', num_color)


for _ in range(num_color):
    rgb = colors[_].rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b



screen.exitonclick()



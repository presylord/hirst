import colorgram
import random
from turtle import Screen, Turtle

x = 10
y = 10

turtle = Turtle()
turtle.ht()
turtle.width(10)
turtle.speed("fastest")

screen = Screen()
screen.colormode(255)

num_color = 30
colors = colorgram.extract('danielhirstpainting.jpg', num_color)
colors_list = []


def generate_color():
    for _ in range(num_color):
        rgb = colors[_].rgb
        color = (rgb.r, rgb.g, rgb.b)
        colors_list.append(color)


def dot_x():
    for axis_x in range(int(x)):
        turtle.dot(20, random.choice(colors_list))
        turtle.penup()
        turtle.forward(50)


generate_color()
turtle.penup()

for _ in range(int(y)):
    turtle.setpos(-200, -200 + (_ * 50))
    dot_x()




screen.exitonclick()



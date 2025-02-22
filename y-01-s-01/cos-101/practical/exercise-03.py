# Shawqi Fares
# 4515520
# Thursday, 20 February 2025
# Exercise no. 03

import turtle

window = turtle.Screen()
window.bgcolor("white")

pen = turtle.Turtle()

def draw_heart():
    pen.color("black")
    pen.penup()
    pen.goto(0, -150)
    pen.pendown()

    pen.left(140)
    pen.forward(180)
    pen.circle(-90, 200)
    pen.left(120)
    pen.circle(-90, 200)
    pen.forward(180)

def draw_arrow():
    pen.width(20)
    pen.penup()
    pen.goto(-200, 50)
    pen.pendown()

    pen.goto(150, -50)

draw_heart()
draw_arrow()

pen.hideturtle()
turtle.done()


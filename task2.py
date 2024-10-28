import turtle
import sys
from math import sqrt

def pythagoras_tree(order=1):
    size = 300
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -size)
    t.pendown()
    t.left(90)
    t.forward(size)
    draw_branches(t, size/sqrt(2), order)
    window.mainloop()

def draw_branches(t, size, order):
    pos_x, pos_y = t.pos()
    angle = t.heading()
    t.right(45)
    t.forward(size)
    if order > 0:
        draw_branches(t, size/sqrt(2), order - 1)

    t.penup()
    t.goto(pos_x, pos_y)
    t.pendown()
    t.setheading(angle)
    t.left(45)
    t.forward(size)
    if order > 0:
        draw_branches(t, size/sqrt(2), order - 1)

if __name__ == '__main__':
    pythagoras_tree(int(sys.argv[1]))

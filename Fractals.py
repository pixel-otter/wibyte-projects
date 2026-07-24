import turtle
import random

t = turtle.Turtle()
ts = turtle.Screen()
ts.tracer(0)
t.speed(0)
t.hideturtle()
turtle.colormode(255)

def square(x, y, len):
    x = x
    y = y - len/2
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x + len, y)
    t.goto(x + len, y + len)   
    t.goto(x, y + len)
    t.goto(x, y)
    if len > 2:
        square(x + 3*len/4, y + len/2, len/2)
        square(x - len/4, y + len/2, len/2)
        square(x + len/4, y - len/4, len/2)
        #The last line creates serpinskis triangle inside this fractal




square(-250, 0, 300)

turtle.mainloop()
import turtle
import math

t = turtle.Turtle()
ts = turtle.Screen()
ts.tracer(0)
t.speed(2)
#t.hideturtle()

phi = (1 + math.sqrt(5))/2
scaling = 1/phi

def Branch(size, level):
    angle = 60
    t.color("brown")
    if level > 3:
        t.color("brown")
        t.pensize(level)
        t.pendown()
        t.forward(size)
        t.right(angle)
        Branch(size*scaling, level-1)
        t.right(angle*-2)
        Branch(size*scaling, level-1)   
        t.right(angle)
        t.forward(-size)
    elif level > 1:
        t.color("green")
        t.pensize(level)
        t.pendown()
        t.forward(size)
        t.right(angle)
        Branch(size*scaling, level-1)
        t.right(angle*-2)
        Branch(size*scaling, level-1)   
        t.right(angle)
        t.forward(-size)
        t.color("brown")
    elif level > 0:
        t.color("red")
        t.dot(2)
        t.color("brown")

t.penup()
t.goto(-40, -100)
t.setheading(90)   
Branch(200, 15)

turtle.mainloop()
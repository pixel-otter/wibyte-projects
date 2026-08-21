import turtle
import time
import math
import random

turtle.colormode(255)

color = "red"
t = turtle.Turtle()
ts = turtle.Screen()
def square(x, y, color):
    t.penup()
    t.goto(x, y)
    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(20)
        t.right(90)
    t.end_fill()

#square(0, 0, "white")

def cls(x, d, bits):
    d = d % bits

    s = x << d
    b = x >> bits - d
    final = (s | b) & ((1 << bits) - 1)
    return final

done = False
while not done:
    try:
        style = int(input("Please give Styling:\n>>"))
        done = True
    except ValueError: 
        done = False

done = False
while not done:
    try:
        clrstyle = int(input("Please give Color Styling:\n>>"))
        done = True
    except ValueError: 
        done = False



if style == 0:
    patternVector = ["00000001", "00000011", "00000110", "00001100", "00011000", "00110000", "01100000", "11001100"]
elif style == 1:
    patternVector = ["11111111", "11111111", "11000011", "11000011", "11000011", "11000011", "11111111", "11111111"]
elif style == 2:
    patternVector = ["11111111", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000"]



r = 255
g = 230
b = 0
colorNum = (r << 16) + (g << 8) + (b)

cnt = 0
while True:
    cnt += 1
    if clrstyle == 0:
        colorNum = cls(colorNum, 1, 24)
    elif clrstyle == 1:
        colorNum = cls(colorNum, 1, 24)
    
    time.sleep(0.1)
    ts.tracer(0)
    t.penup()
    for m in range(8):
        pattern = int(patternVector[m], 2)
        if clrstyle == 0:
            colorNum = cls(colorNum, 2, 24)
        elif clrstyle == 1:
            colorNum = cls(colorNum, 4, 24)
        
        for k in range(8):
            i = k
            if clrstyle == 0:
                colorNum = cls(colorNum, 2, 24)
            elif clrstyle == 1:
                colorNum = cls(colorNum * 3, 3, 24)
            colorStr = "#" + f"{colorNum:06x}"
            b = (pattern & (1 << i)) >> i
            t.goto(100 - 40*(k + 1), 100 - 40*(m + 1) + 40)
            t.write(f"b{i + m*8}")
            if b == 1:
                square(100 - 40*(k + 1), 100 - 40*(m), colorStr)
            else:
                square(100 - 40*(k + 1), 100 - 40*(m), "white")
            t.penup()

    for i in range(len(patternVector)):
        val = int(patternVector[i], 2)
        iv = 0
        if style == 0:
            iv = val << 1
            if len(bin(iv)) > 10:
                    iv = 0b0000011
        elif style == 1:
            iv = val ^ 0b11111111
        elif style == 2:
            iv = val | (32 ^ (cnt % 8))
        patternVector[i] = f"{iv:08b}"
            
    ts.update()
    
    
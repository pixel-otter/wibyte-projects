import turtle

t = turtle.Turtle()
ts = turtle.Screen()
ts.tracer(0)

ts.colormode(255)

def fofz(z, c):
    # Nativly works on complex numbers
    return z**2 + c

z_val = 1 + 2j
c_val = 2 + 3j

result = fofz(z_val, c_val)
print(str(result))

mandelbrotset = []
colors = []

realstart = -2.0
realend = 0.5
imagstart = -1.2
imagend = 1.2

resolution = 500

x_step = (realend - realstart) / resolution
y_step = (imagend - imagstart) / resolution

for i in range(resolution):
    #Prevent Drift Error
    imag = imagstart + (i * y_step)
    for j in range(resolution):
        #Prevent Drift Error
        real = realstart + (x_step * j)

        #Combines real and imaginary numbers
        c = complex(real, imag)

        # Z is the value increasing
        z = 0 + 0j

        #Quite Importantly, the score decideds the color, time till explosion
        score = -1

        for b in range(1, 101):
            z = fofz(z, c)

            #this is the explosion, if it exceeds 2 it grows so fast it is not possible
            if abs(z) > 2:
                score = b
                break
        #Append
        mandelbrotset.append(c)
        colors.append((c, score))

#The set is quite simple

coords = []

for a in mandelbrotset:
    x = a.real * 500
    y = a.imag * 500 
    coords.append((x, y))
    
print(len(coords))
ts.setworldcoordinates(-1100, -700, 400, 700)

ts.tracer(0)

for m in range(len(coords)):
    i = coords[m]
    w = colors[m]
    t.penup()
    x = i[0]
    y = i[1]
    if (type(x) == float or type(x) == int) and type(y) == float or type(y) == int:
        t.goto(x, y)
        score = w[1]
        if score == -1:
            t.color(0, 0, 0)
        else:
            r = (score * 9) % 256
            g = (score * 5) % 256
            b = (score * 15) % 256

            t.color(r, g, b)
        t.dot(4) 
    else:
        continue 

    t.pendown()

ts.update()
turtle.mainloop()
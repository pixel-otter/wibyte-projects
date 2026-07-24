from PIL import Image
import math
#I did not code the pillow switch, I just got bored waiting so
def fofz(z, c):
    # Nativly works on complex numbers
    return z**2 + c

z_val = 1 + 2j
c_val = 0 + 1j
result = fofz(z_val, c_val)
print(str(result))

juliaset = []
colors = []

realstart = -1.5
realend = 1.5
imagstart = -1.5
imagend = 1.5

resolution = 2000

x_step = (realend - realstart) / resolution
y_step = (imagend - imagstart) / resolution

img = Image.new('RGB', (resolution, resolution))
#c = complex(-0.74434, 0.10772)
c = complex(-1, 0)

for i in range(resolution):
    #Prevent Drift Error
    imag = imagstart + (i * y_step)
    for j in range(resolution):
        #Prevent Drift Error
        real = realstart + (x_step * j)

        #Combines real and imaginary numbers

        # Z is the value increasing
        z = complex(real, imag)
        pos = complex(real, imag)

        #Quite Importantly, the score decideds the color, time till explosion
        score = -1

        for b in range(1, 101):
            z = fofz(z, c)

            #this is the explosion, if it exceeds 2 it grows so fast it is not possible
            if abs(z) > 2:
                score = b
                break
        #Append
        juliaset.append(pos)
        colors.append((pos, score))

#The set is quite simple
#THIS IS NOT MY CODE. I JUST GOT BORED WAITING FOR THE TURTLE SO I FOUND THIS
#If you want my code copy the madelbort set code and replace marndelbrotset with juliaset
print(f"Lists packed with {len(juliaset)} points.")

# 2. Setup the flat Pillow Canvas in RAM
img = Image.new('RGB', (resolution, resolution))

scheme = "Base"
# 3. Fast Image Array Render Loop
# Instead of moving a Turtle pen, we read the arrays sequentially
for index in range(len(juliaset)):
    # Calculate the flat grid position (column and row) from the sequential index
    col = index % resolution
    row = index // resolution
    
    score = colors[index][1] # Pull the saved score from your list
    

    # Run your exact color math formulas
    if score == -1:
        if not scheme == "Base"and not scheme == "one":
            r, g, b_chan = 255, 255, 255
        else:
            r, g, b_chan = 0, 0, 0
    else:
        angle = score / 12
        if not scheme == "Base" and not scheme == "two":
            r = 255 - int((math.sin(angle + 0.0) * 127.5) + 127.5)
            g = 255 - int((math.sin(angle + 2.0) * 127.5) + 127.5)
            b_chan = 255 - int((math.sin(angle + 4.0) * 127.5) + 127.5)
        else:
            r = int((math.sin(angle + 0.0) * 127.5) + 127.5)
            g = int((math.sin(angle + 2.0) * 127.5) + 127.5)
            b_chan = int((math.sin(angle + 4.0) * 127.5) + 127.5)

    # Stamp the pixel into memory instantly
    img.putpixel((col, row), (r, g, b_chan))

# 4. Flash the final picture instantly
img.show()
import math

width = 600
height = 600
maxcolor=256
code = "P3\n"
code+= "%d %d %d\n"%(width, height, maxcolor)


for w in range(width):
    for h in range(height):
        r = w%maxcolor
        g = h%maxcolor
        b = (w+h)%maxcolor
        code += "%d %d %d "%(r, g, b)
    code+="\n"



f=open("3.ppm", "w")
f.write(code)
f.close()

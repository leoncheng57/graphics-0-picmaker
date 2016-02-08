import math

width = 600
height = 600
maxcolor=256
code = "P3\n"
code+= "%d %d %d\n"%(width, height, maxcolor)


for w in range(width):
    for h in range(height):
        r = math.ceil(w*w+h*h)%maxcolor
        g = math.ceil(w*w+h*h)%maxcolor
        b = math.ceil(w*w+h*h)%maxcolor
        code += "%d %d %d "%(r, g, b)
    code+="\n"



f=open("4.ppm", "w")
f.write(code)
f.close()

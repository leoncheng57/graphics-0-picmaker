import math

width = 600
height = 600
maxcolor=256
code = "P3\n"
code+= "%d %d %d\n"%(width, height, maxcolor)


for w in range(width):
    for h in range(height):
        r = math.ceil(math.sqrt((w-width/2)**2+(h-height/2)**2)-70)%maxcolor
        g = math.ceil(w+h)%maxcolor
        b = math.ceil(h-w)%maxcolor
        code += "%d %d %d "%(r, g, b)
    code+="\n"

f=open("7.ppm", "w")
f.write(code)
f.close()

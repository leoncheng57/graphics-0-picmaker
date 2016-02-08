#TODO: Make recursive, fractal circles
#if <r then do this first
#else, call recursive function, set enter to w/4, h/4
#also set r to r/4

import math

width = 600
height = 600
maxcolor=256
code = "P3\n"
code+= "%d %d %d\n"%(width, height, maxcolor)

def inRange(h, k, radius):
    b1 = math.sqrt((x-h)**2+(y-k)**2)<radius 
    b2 = math.sqrt((x-h)**2+(y-k)**2)>radius/2 
    return b1 and b2

h = width/2
k = height/2
radius = width/2


def circle(x, y, h, k):
    r = math.ceil(math.sqrt((x-h)**2+(y-k)**2)+590)%maxcolor
    g = math.ceil(math.sqrt((x-h)**2+(y-k)**2)+500)%maxcolor
    b = math.ceil(math.sqrt((x-h)**2+(y-k)**2)+50)%maxcolor
    ret = "%d %d %d "%(r, g, b)
    return ret

for y in range(height):
    for x in range(width):
        if (inRange(h, k, radius)):
            code+=circle(x, y, h, k)
        else:
            r = math.ceil(math.sqrt((x-width/2)**2+(y-height/2)**2)-90)%maxcolor
            g = math.ceil(math.sqrt((x-width/2)**2+(y-height/2)**2)+x+y-50)%maxcolor
            b = math.ceil(math.sqrt((x-width/2)**2+(y-height/2)**2)+x*y+50)%maxcolor
            code+="%d %d %d "%(r, g, b)
    code+="\n"
        
f=open("6.ppm", "w")
f.write(code)
f.close()

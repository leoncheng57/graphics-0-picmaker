#TODO: Make recursive, fractal circles
#if <r then do this first
#else, call recursive function, set enter to w/4, h/4
#also set r to r/4

import math

width = 400
height = 400
maxcolor= 256
code = "P3\n"
code+= "%d %d %d\n"%(width, height, maxcolor)

def inRange(h, k, radius):
    return math.sqrt((x-h)**2+(y-k)**2)<radius

def circle(x, y, h, k, radius):
    ret = ""
    if (inRange(h, k, radius)): 
        r = math.ceil(math.sqrt((x-h)**2+(y-k)**2))%maxcolor
        g = math.ceil(math.sqrt((x-h)**2+(y-k)**2))%maxcolor
        b = math.ceil(math.sqrt((x-h)**2+(y-k)**2)+50)%maxcolor
        ret += "%d %d %d "%(r, g, b)
    else:
        ret+=circle(x, y, h/2, k/2, radius/2)
        ret+=circle(x, y, h/2*3, k/2, radius/2)
        ret+=circle(x, y, h/2, k/2*3, radius/2)
        ret+=circle(x, y, h/2*3, k/2*3, radius/2)
        #r = 0;
        #g = 0;
        #b = 0;
        ret+="%d %d %d "%(r, g, b)
    ret+="\n"
    return ret

h = width/2
k = height/2
radius = width/2

while (radius>1):
    for y in range(height):
        for x in range(width):
            code += circle(x,y,h,k,radius)
        
f=open("8.ppm", "w")
f.write(code)
f.close()

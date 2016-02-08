import math
import random 

width = 512
height = 512
maxcolor = 256
code = "P3\n %d %d \n %d\n"%(width, height, maxcolor)

for i in range(width):
    for j in range(height):
        r = random.randint(0, 256)
        g = random.randint(0, 256)
        b = random.randint(0, 256)
        code += "%d %d %d "%(r, g, b)

f=open("1.ppm","w")
f.write(code)
f.close()

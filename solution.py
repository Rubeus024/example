import math
a = 1
b = 1
c = -2

delta = b**2-4*a*c

if delta>0 :
    x1 = (-b-math.sqrt(delta))/(2*a)
    x2 = (-b+math.sqrt(delta))/(2*a)
    print(x1,x2,"Jest git")

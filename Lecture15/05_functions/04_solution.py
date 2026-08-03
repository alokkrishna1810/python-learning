import math

def circle_stats(radius):
    area =  math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return area, circumference
    # print("hi") # code not reachable after return in function

a, c = circle_stats(3)

print("Area:", a, "Circumference:", c)

import math

x1, y1, x2, y2, x3, y3 = map(float, input().split())


a = math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))
b = math.sqrt((x2 - x3)*(x2 - x3) + (y2 - y3)*(y2 - y3))
c = math.sqrt((x3 - x1)*(x3 - x1) + (y3 - y1)*(y3 - y1))

s = (a+b+c)/2

A = math.sqrt(s*(s-a)*(s-b)*(s-c))

print (A)
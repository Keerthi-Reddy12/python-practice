import math
class shape:
    pass
class circle(shape):
    def int(s,r): s.r=r
    def area(s):
        return 3.14*s.r*s.r
    def peri(s):
        return 2+3.14+s.r
class square(shape):
    def int(s,a): s.a=a
    def peri(s):
        return 4*s.a 
    def area(s):
        return s.a*s.a 
c=circle()
print(c.area(),c.peri())
s=square(4)
print(s.area(),s.peri())
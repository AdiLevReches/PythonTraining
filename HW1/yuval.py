from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("<"+str(self.x)+","+str(self.y)+">")

    def distance(self,other):
        return(sqrt((self.x-other.x)**2+(self.y-other.y)**2))

p1=Point(3, 4)
p2=Point(4,3)
p1.print_point()
print(p1.distance(p2))


class Circle:

    def __init__(self,p,r):
        self.p=p
        self.r=r

    def in_circle(self,point):
        # return self.p.distance(point) < self.r
        dist = self.p.distance(point)
        if dist < self.r:
            return True
        else:
            return False

circle1 = Circle(Point(3,2),4)

print(circle1.in_circle(Point(4,5)))
print(circle1.in_circle(Point(10,5)))


class Rectangle:
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2

    def Calc(self):
        if p1.y > 0 and p2.y < 0 :
            height = p1.y + abs(p2.y)
        else:
            height = p1.y - p2.y
        if p1.x < 0 and p2.x > 0 :
            width = p2.x + abs(p1.x)
        else:
            width = p2.x - p1.x
        return(height * width)

rec1 = Rectangle(Point(2,2),Point(1,1))
rec2 = Rectangle(Point(2,2),Point(0,1))
rec3 = Rectangle(Point(2,2),Point(1,1))
print(rec1.Calc())
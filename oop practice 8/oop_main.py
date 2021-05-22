import math


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):

        x1,y1 = self.coor1
        x2,y2 = self.coor2

        print(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


    def slope(self):

        x1, y1 = self.coor1
        x2, y2 = self.coor2

        print((y2 - y1) / (x2 - x1))
        return (y2 - y1) / (x2 - x1)


# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

li.distance()

li.slope()
# d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#
# slope = (y2 - y1) / (x2 - x1)

class Cylinder:

    def __init__(self, height=1, radius=1):

        self.height = height
        self.radius = radius

    def volume(self):
        v = 3.14 * (self.radius**2) * self.height
        print(v)
        return v


    def surface_area(self):
        a = (2 * 3.14 * self.radius * self.height) + (2 * 3.14 * self.radius**2)
        print(a)
        return a

# EXAMPLE OUTPUT
c = Cylinder(2,3)

c.volume()

c.surface_area()
from collections import namedtuple
from math import sqrt

# Point = namedtuple('Point' , ['x' , 'y' ])



# p : Point = Point(1 , 2 )

# q : Point = Point(4,5)



# r = sqrt((p.x - q.x)**2 + (p.y - q.y)**2)

# print(r)



Point = namedtuple('Cordinate' , ['x' , 'y' , 'z'])



a : Point = Point(0, 0 , 0)

b : Point = Point(1 , 2, 3)

c : Point = Point( 4 , 5  , 6)


area = 0.5*(   a.x*(b.y - c.y) + b.x*(c.y - a.y) + c.x*(a.y-b.y))


print("Area of Triange is {area}".format(area=area))


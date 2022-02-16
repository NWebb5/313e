#  File: Geometry.py

#  Description:

#  Student Name: Nicholas Webb

#  Student UT EID: nw6887

#  Partner Name: EJ Porras

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

import math
import re

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
    self.x = x
    self.y = y
    self.z = z

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
    return "(" + self.x + ", " + self.y + ", " + self.z + ")"

  def is_equal (self, a, b):
    tol = 1.0e-6
    return (abs(a-b) < tol )

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
    math.sqrt((self.x - other.x)**2 - (self.y - other.y)**2 + (self.z - other.z)**2)

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    return self.is_equal(self.x, other.x) and self.is_equal(self.y, other.y) and self.is_equal(self.z, other.z)

class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
    self.x = x
    self.y = y
    self.z = z
    self.radius = radius
    self.center = Point(x, y, z)

  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
    return "(" + self.x + ", " + self.y + ", " + self.z + ")"

  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
    return 4*math.pi()*self.radius

  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
    return (4/3)*math.pi()*(self.radius)**3

  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
    if p.x < self.x and p.y < self.y and p.z < self.z:
      return True
    else:
      return False

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
    return self.center.distance(other.center) + other.radius < self.radius

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    cube_verticies = []
    half_points = [(-.5, .5, .5),
    (-.5, -.5, .5), (-.5, -.5, -.5), (.5, -.5, .5), (.5, .5, -.5), (.5, -.5, -.5), (.5, -.5, -.5), (.5, .5, .5)]
    for half_points in half_points:
      cube_verticies = cube_verticies.append(Point(a_cube.x + (half_points[0] * a_cube.side), a_cube.y + (half_points[1] * a_cube.side), a_cube.z + (half_points[2] * a_cube.side)))

    for i in range(0,8):
      if self.center.distance(half_points[i]) <= self.radius:
        return True
    return False
      
  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, a_cyl):
    pass
  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
    outside_sphere =  other.radius + self.radius < self.center.distance(other)
    
    return not self.is_inside_sphere(other) and not outside_sphere
    
  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube):
    cube_verticies = []
    cube_check_outside = True
    half_points = [(-.5, .5, .5),
    (-.5, -.5, .5), (-.5, -.5, -.5), (.5, -.5, .5), (.5, .5, -.5), (.5, -.5, -.5), (.5, -.5, -.5), (.5, .5, .5)]
    for half_points in half_points:
      cube_verticies = cube_verticies.append(Point(a_cube.x + (half_points[0] * a_cube.side), a_cube.y + (half_points[1] * a_cube.side), a_cube.z + (half_points[2] * a_cube.side)))
    
    for i in range(0,8):
      if self.center.distance(cube_verticies[i]) <= self.radius:
        cube_check_outside = False

    return not self.is_inside_cube(a_cube) and not cube_check_outside


  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
    return Cube(self.x, self.y, self.z, (2*self.radius)/math.sqrt(3))

class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
    self.x = x
    self.y = y
    self.z = z
    self.side = side
    self.center = Point(x, y, z)


  # string representation of a Cube of the form:
  # Center: (x, y, z), Side: value
  def __str__ (self):
    return "(" + self.x + ", " + self.y + ", " + self.z + ")"


  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
    return 6*self.side**2

  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
    return self.side**3

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
    cube_verticies = []
    half_points = [(-.5, .5, .5),
    (-.5, -.5, .5), (-.5, -.5, -.5), (.5, -.5, .5), (.5, .5, -.5), (.5, -.5, -.5), (.5, -.5, -.5), (.5, .5, .5)]
    for half_points in half_points:
      cube_verticies = cube_verticies.append(Point(self.x + (half_points[0] * self.side), self.y + (half_points[1] * self.side), self.z + (half_points[2] * self.side)))

    for i in 

  # determine if a Sphere is strictly inside this Cube
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    pass

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
    pass

  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, a_cyl):
    pass

  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
    pass

  # determine the volume of intersection if this Cube
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
    pass

  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
    pass

class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
    pass
  # returns a string representation of a Cylinder of the form:
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
    pass
  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
    pass
  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
    pass
  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
    pass
  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    pass
  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    pass
  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
    pass
  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cylinder (self, other):
    pass

def main():
  # read data from standard input

  # read the coordinates of the first Point p

  # create a Point object

  # read the coordinates of the second Point q

  # create a Point object

  # read the coordinates of the center and radius of sphereA

  # create a Sphere object

  # read the coordinates of the center and radius of sphereB

  # create a Sphere object

  # read the coordinates of the center and side of cubeA

  # create a Cube object

  # read the coordinates of the center and side of cubeB

  # create a Cube object

  # read the coordinates of the center, radius and height of cylA

  # create a Cylinder object

  # read the coordinates of the center, radius and height of cylB

  # create a Cylinder object


  # print if the distance of p from the origin is greater
  # than the distance of q from the origin


  # print if Point p is inside sphereA
  if sphereA.is_inside_point(point_p):
    print('Point p is inside sphereA')
  else:
    print('Point p is not inside sphereA')


  # print if sphereB is inside sphereA
  if sphereA.is_inside_sphere(sphereB):
    print('sphereB is inside sphereA')
  else:
    print('sphereB is not inside sphereA')

  # print if cubeA is inside sphereA
  if cubeA.is_inside_sphere(sphereA):
    print('cubeA is inside sphereA')
  else:
    print('cubaA is not inside sphereA')

  # print if cylA is inside sphereA
  if sphereA.is_inside_cyl(cyl_A):
    print('cylA is inside sphereA')
  else:
    print('cylA is not inside sphereA')

  # print if sphereA intersects with sphereB
  if sphereA.does_intersect_sphere(sphereB):
    print('sphereA does intersect sphereB')
  else:
    print('sphereA does not intersect with Sphere B')

  # print if cubeB intersects with sphereB
  if sphereB.does_intersect_cube(cubeB):
    print('cubeB does intersect sphereB')
  else:
    print('cubeB does not intersect sphereB')

  # print if the volume of the largest Cube that is circumscribed
  # by sphereA is greater than the volume of cylA
  if sphereA.circumscribe_cube().volume() > cyl_A.volume():
    print('Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA')
  else:
    print('Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA')
  print()


  # print if Point p is inside cubeA
  if cubeA.is_inside_point(point_p):
    print('Point p is inside cubeA')
  else:
    print('Point p is not inside cubeA')

  # print if sphereA is inside cubeA
  if cubeA.is_inside_sphere(sphereA):
    print('sphereA is inside cubeA')
  else:
    print('sphereA is not inside cubeA')

  # print if cubeB is inside cubeA
  if cubeA.is_inside_cube(cubeB):
    print('cubeB is inside cubeA')
  else:
    print('cubeB is not inside cubeA')

  # print if cylA is inside cubeA
  if cubeA.is_inside_cylinder(cyl_A):
    print('cylA is inside cubeA')
  else:
    print('cylA is not inside cubeA')

  # print if cubeA intersects with cubeB
  if cubeA.does_intersect_cube(cubeB):
    print('cubeA does intersect cubeB')
  else:
    print('cubeA does not intersect cubeB')

  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
  if cubeA.intersection_volume(cubeB) > sphereA.volume():
    print('Intersection volume of cubeA and cubeB is greater than the volume of sphereA')
  else:
    print('Intersection volume of cubeA and cubeB is not greater than the volume of sphereA')

  # print if the surface area of the largest Sphere object inscribed
  # by cubeA is greater than the surface area of cylA
  if cubeA.inscribe_sphere().area() > cyl_A.area():
    print('Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA')
  else:
    print('Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA')
  print()


  # print if Point p is inside cylA
  if cyl_A.is_inside_point(point_p):
    print('Point p is inside cylA')
  else:
    print('Point p is not inside cylA')

  # print if sphereA is inside cylA
  if cyl_A.is_inside_sphere(sphereA):
    print('sphereA is inside cylA')
  else:
    print('sphereA is not inside cylA')

  # print if cubeA is inside cylA
  if cyl_A.is_inside_cube(cubeA):
    print('cubeA is inside cylA')
  else:
    print('cubeA is not inside cylA')

  # print if cylB is inside cylA
  if cyl_A.is_inside_cylinder(cyl_B):
    print('cylB is inside cylA')
  else:
    print('cylB is not inside cylA')

  # print if cylB intersects with cylA
  if cyl_A.does_intersect_cylinder(cyl_B):
    print('cylB does intersect cylA')
  else:
    print('cylB does not intersect cylA')

if __name__ == "__main__":
  main()

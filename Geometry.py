#  File: Geometry.py

#  Description: This program

#  Student Name: Nicholas Webb

#  Student UT EID: nw6887

#  Partner Name: EJ Porras

#  Partner UT EID: ejp2488

#  Course Name: CS 313E

#  Unique Number: 51135

#  Date Created: 2/11/2022

#  Date Last Modified: 2/15/2022
from typing import Any

import math


class Point(object):
    # constructor with default values
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__(self):
        return "(" + str(float(self.x)) + ", " + str(float(self.y)) + ", " + str(float(self.z)) + ")"

    # get distance to another Point object
    # other is a Point object
    # returns the distance as a floating point number
    def distance(self, other):
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2 + (other.z - self.z) ** 2)

    # test for equality between two points
    # other is a Point object
    # returns a Boolean
    def __eq__(self, other):
        tol = 1.0e-6
        return (abs(self.x - other.x) < tol) and (abs(self.y == other.y) < tol) \
        and (abs(self.z == other.z) < tol)


class Sphere(object):

    # constructor with default values
    def __init__(self, x = 0, y = 0, z = 0, radius = 1):
        self.center = Point(x, y, z)
        self.radius = radius

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__(self):
        return "Center: " + str(self.center) + ", Radius: " + str(float(self.radius))
    # compute surface area of Sphere
    # returns a floating point number
    def area(self):
        return 4 * math.pi * self.radius ** 2

    # compute volume of a Sphere
    # returns a floating point number
    def volume(self):
        return (4 * math.pi * self.radius ** 3)/3

    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point(self, p):
        return p.distance(p, self.center) < self.radius

    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, other):
        return self.radius > (other.radius + self.center.distance(other.center))

    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are strictly
    # inside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        return self.radius > a_cube.center.distance(self.center) + math.sqrt(3 * ((a_cube.side / 2) ** 2))

    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cyl(self, a_cyl):
        return self.radius > a_cyl.center.distance(self.center) + math.sqrt((a_cyl.height / 2) ** 2 + a_cyl.radius ** 2)

    # determine if another Sphere intersects this Sphere
    # other is a Sphere object
    # two spheres intersect if they are not strictly inside
    # or not strictly outside each other
    # returns a Boolean
    def does_intersect_sphere(self, other):
        return not self.is_inside_sphere(other) and (self.radius + other.radius < self.center.distance(other.center))

    # determine if a Cube intersects this Sphere
    # the Cube and Sphere intersect if they are not
    # strictly inside or not strictly outside the other
    # a_cube is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, a_cube):
        dist = self.center.distance(a_cube.center)
        hypot_half = (((a_cube.side**2) + (a_cube.side**2))**0.5)/2
        sum_radii = self.radius + hypot_half

        if (sum_radii <= dist) and (sum_radii >= dist):
            return True
        else:
            return False

    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube(self):
        return Cube(self.center.x, self.center.y, self.center.z, 2 * math.sqrt(self.radius ** 2/ 3))


class Cube(object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__(self, x = 0, y = 0, z = 0, side = 1):
        self.center = Point(x, y, z)
        self.side = side

    # string representation of a Cube of the form:
    # Center: (x, y, z), Side: value
    def __str__(self):
      return "Center: " + str(self.center) +  ", Side: " + str(float(self.side))

    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area(self):
        return 6 * self.side ** 2

    # compute volume of a Cube
    # returns a floating point number
    def volume(self):
      return self.side ** 3

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point(self, p):
        return math.sqrt(3 * (self.side / 2) ** 2) > p.distance(self.center)

    # determine if a Sphere is strictly inside this Cube
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        return self.side / 2 > self.center.distance(a_sphere.center) + a_sphere.radius

    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube(self, other):
        return self.side > other.side + other.center.distance(self.center)

    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, a_cyl):
        return a_cyl.height < self.side

    # determine if another Cube intersects this Cube
    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, other):
        return self.center.distance(other.center) < self.side + other.side

    # determine the volume of intersection if this Cube
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number
    def intersection_volume(self, other):
        return self.volume() - other.volume()

    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere(self):
        return Sphere(self.center.x, self.center.y, self.center.z, self.side / 2)


class Cylinder(object):
    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__(self, x = 0, y = 0, z = 0, radius = 1, height = 1):
        self.center = Point(x, y, z)
        self.radius = radius
        self.height = height

    # returns a string representation of a Cylinder of the form:
    # Center: (x, y, z), Radius: value, Height: value
    def __str__(self):
        return "Center: " + str(self.center) + ", Radius: " + str(float(self.radius)) + ", Height: " + str(float(self.height))

    # compute surface area of Cylinder
    # returns a floating point number
    def area(self):
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * self.radius ** 2)

    # compute volume of a Cylinder
    # returns a floating point number
    def volume(self):
        return math.pi * self.radius ** 2 * self.height

    # determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # returns a Boolean
    def is_inside_point(self, p):
      return p.distance(self.center) < self.radius and p.distance(self.center) < self.height

    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        return self.radius > a_sphere.radius + self.center.distance(other.center)

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        return self.radius >= self.center.distance(a_cube.center) + a_cube.side

    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, other):
        return self.radius > other.radius + self.center.distance(other.center)

    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean
    def does_intersect_cylinder(self, other):
        return self.center.distance(other.center) < self.radius + other.radius \
               and self.center.distance(other.center) < self.height + other.height


def main():

    try:
        while True:
            # read data from standard input
            p_coord_info = input().split()
            q_coord_info = input().split()
            sphereA_info = input().split()
            sphereB_info = input().split()
            cubeA_info = input().split()
            cubeB_info = input().split()
            cylA_info = input().split()
            cylB_info = input().split()

            # read the coordinates of the first Point p
            for i in range(len(p_coord_info)):
                p_coord_info[i] = float(p_coord_info[i])

            # create a Point object
            p_coord = Point(p_coord_info[0], p_coord_info[1], p_coord_info[2])

            # read the coordinates of the second Point q
            for i in range(len(q_coord_info)):
                q_coord_info[i] = float(q_coord_info[i])

            # create a Point object
            q_coord = Point(q_coord_info[0], q_coord_info[1], q_coord_info[2])

            # read the coordinates of the center and radius of sphereA
            for i in range(len(sphereA_info)):
                sphereA_info[i] = float(sphereA_info[i])

            # create a Sphere object
            sphereA = Sphere(sphereA_info[0], sphereA_info[1], sphereA_info[2], sphereA_info[3])

            # read the coordinates of the center and radius of sphereB
            for i in range(len(sphereB_info)):
                sphereB_info[i] = float(sphereB_info[i])

            # create a Sphere object
            sphereB = Sphere(sphereB_info[0], sphereB_info[1], sphereB_info[2], sphereB_info[3])

            # read the coordinates of the center and side of cubeA
            for i in range(len(cubeA_info)):
                cubeA_info[i] = float(cubeA_info[i])

            # create a Cube object
            cubeA = Cube(cubeA_info[0], cubeA_info[1], cubeA_info[2], cubeA_info[3])

            # read the coordinates of the center and side of cubeB
            for i in range(len(cubaB_info)):
                cubeB_info[i] = float(cubeB_info[i])

            # create a Cube object
            cubeB = Cube(cubeB_info[0], cubeB_info[1], cubeB_info[2], cubeB_info[3])

            # read the coordinates of the center, radius and height of cylA
            for i in range(len(cylA_info)):
                cylA_info[i] = float(cylA_info[i])

            # create a Cylinder object
            cylA = Cylinder(cylA_info[0], cylA_info[1], cylA_info[2], cylA_info[3], cylA_info[4])

            # read the coordinates of the center, radius and height of cylB
            for i in range(len(cylB_info)):
                cylB_info[i] = float(cylB_info[i])

            # create a Cylinder object
            cylB = Cylinder(cylB_info[0], cylB_info[1], cylB_info[2], cylB_info[3], cylB_info[4])

            # print if the distance of p from the origin is greater
            # than the distance of q from the origin
            origin = Point(0, 0, 0)
            if p_coord.distance(origin) > q_coord.distance(origin):
                print("True")
            else:
                print("False")

            # print if Point p is inside sphereA
            if sphereA.is_inside_point(p_coord):
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
            if sphereA.is_inside_cyl(cylA):
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
            if sphereA.circumscribe_cube().volume() > cylA.volume():
                print('Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA')
            else:
                print('Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA')
            print()

            # print if Point p is inside cubeA
            if cubeA.is_inside_point(p_coord):
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
            if cubeA.is_inside_cylinder(cylA):
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
            if cubeA.inscribe_sphere().area() > cylA.area():
                print('Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA')
            else:
                print('Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA')
            print()

            # print if Point p is inside cylA
            if cylA.is_inside_point(p_coord):
                print('Point p is inside cylA')
            else:
                print('Point p is not inside cylA')

            # print if sphereA is inside cylA
            if cylA.is_inside_sphere(sphereA):
                print('sphereA is inside cylA')
            else:
                print('sphereA is not inside cylA')

            # print if cubeA is inside cylA
            if cylA.is_inside_cube(cubeA):
                print('cubeA is inside cylA')
            else:
                print('cubeA is not inside cylA')

            # print if cylB is inside cylA
            if cylA.is_inside_cylinder(cylB):
                print('cylB is inside cylA')
            else:
                print('cylB is not inside cylA')

            # print if cylB intersects with cylA
            if cylA.does_intersect_cylinder(cylB):
                print('cylB does intersect cylA')
            else:
                print('cylB does not intersect cylA')
    except EOFError:
        pass


if __name__ == "__main__":
    main()

"""
@Author : Rohit Shedage
@Goal : To implement area of triangle
"""

import sys


class Point2D:
    """
    class implementation of 2D point coordinate x and y
    """

    def __init__(self, x: float, y: float):
        """
        constructor accepting x and y coordinate
        :param x: taking x coordinate
        :param y: taking y coordinate
        """
        if (type(x) != int and type(x) != float) or (type(y) != int and type(y) != float):
            print("Bad Coordinate value")
            sys.exit(-1)

        self.x = x
        self.y = y

    def get_distance(self, other) -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


def type_check_triangle_parameter(v) -> bool:
    if type(v) != tuple:
        return False
    if len(v) != 2:
        return False
    if (type(v[0]) != int and type(v[0]) != float) or (type(v[1]) != int and type(v[1]) != float):
        return False

    return True


class Triangle:
    """
    Implementation of 2D triangle with cartesian coordinate
    """

    def __init__(self, init_vertex_a: tuple, init_vertex_b: tuple, init_vertex_c: tuple):
        """
        Constructor accepting vertex of triangle
        :param init_vertex_a: a coordinate vertex
        :param init_vertex_b: b coordinate vertex
        :param init_vertex_c: c coordinate vertex
        """
        if (type_check_triangle_parameter(init_vertex_a) == False and
                type_check_triangle_parameter(init_vertex_b) == False and
                type_check_triangle_parameter(init_vertex_c) == False):
            print("Bad Coordinate For Triangle")
            sys.exit(-1)

        self.vertex_a = Point2D(init_vertex_a[0], init_vertex_a[1])
        self.vertex_b = Point2D(init_vertex_b[0], init_vertex_b[1])
        self.vertex_c = Point2D(init_vertex_c[0], init_vertex_c[1])

        self.len_ab = self.vertex_a.get_distance(self.vertex_b)
        self.len_bc = self.vertex_b.get_distance(self.vertex_c)
        self.len_ca = self.vertex_c.get_distance(self.vertex_a)

        if (self.len_ab + self.len_bc <= self.len_ca or
                self.len_bc + self.len_ca <= self.len_ab or
                self.len_ca + self.len_ab <= self.len_bc):
            print("Sum of length of two sides of triangle must be greater than the other sides")
            sys.exit(-1)

    def perimeter(self) -> float:
        return self.len_ab + self.len_bc + self.len_ca

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.len_ab) - (s - self.len_bc) - (s - self.len_ca)) ** 0.5

    def get_len_ab(self) -> float:
        return self.len_ab

    def get_len_bc(self) -> float:
        return self.len_bc

    def get_len_ca(self) -> float:
        return self.len_ca


T1 = Triangle((-4.5, -1.5), (1.5, 5.0), (4.5, 0.5))
p = T1.perimeter()
print("Perimeter of a triangle :", p)
A = T1.area()
print("Area of triangle is :", A)
print("L(AB) =", T1.get_len_ab())
print("L(BC) =", T1.get_len_bc())
print("L(CA) =", T1.get_len_ca())

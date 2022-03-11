"""
@Author : Rohit
@Goal : TO compute distance between two point
"""


def compute_distance(x1: float, y1: float, x2: float, y2: float)-> float:
    """
    Compute distance points P1(x1,y1), P2(x2, y2)
    :param x1: x Coordinate of point 1
    :param y1: y Coordinate of point 1
    :param x2: x Coordinate of point 2
    :param y2: y Coordinate of point 2
    :return: Distance Between (x1, y1) and (x2, y2)
    """
    if type(x1) != float and type(x1) != int:
        print("Bad Type :x1")
        return None

    if type(y1) != float and type(y1) != int:
        print("Bad Type :y1")
        return None

    if type(x2) != float and type(x2) != int:
        print("Bad Type :x2")
        return None

    if type(y2) != float and type(y2) != int:
        print("Bad Type :y2")
        return None

    d = ((y2 - y1)**2 + (x2 - x1)**2)**0.5

    return d


x1 = 1.1
x2 = 2.3
y1 = -3.2
y2 = 4.3

D = compute_distance(x1, y1, x2, y2)

print("Distance Between Two Points :", D)

"""
@Author : Rohit
@goal : To Compute Gravitational Law
"""


def compute_gravitational_law(m1: float, m2: float, r: float) -> float:
    """
    Compute the gravitational force in Newtons between two object
    :param m1: mass of object 1
    :param m2: mass of object 2
    :param r: distance between two object
    :return: magnitude of gravitation force
    """
    if type(m1) != float and type(m1) != int:
        print("Bad Type of :m1")
        return None

    if type(m2) != float and type(m2) != int:
        print("Bad Type of :m2")
        return None

    if type(r) != float and type(r) != int:
        print("Bad Type of :Distance")
        return None

    g = 6.67 * (10 ** -11)

    f = (g * m1 * m2)/(r**2)

    return f


m1 = 5543323556
m2 = 74332336567
d = 0.5

Ret = compute_gravitational_law(m1, m2, d)
if Ret != None:
    print("Distance Between Two Masses :", Ret)

help(compute_gravitational_law)

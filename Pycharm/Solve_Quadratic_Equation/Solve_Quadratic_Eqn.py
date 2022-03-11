"""
@Author : RS
@Goal : To Solve Quadratic Equation
"""

def solve_quadratic_eqn(cf_a, cf_b, cf_c):
    """
    Solve Quadratic Equation take coefficients of
    a quadratic equation and return their roots
    :param cf_a: Coefficient of term x**2 in QE
    :param cf_b: Coefficient of term x in QE
    :param cf_c: Constant term in QE
    :return: None if type error or no real roots
             list of two roots otherwise
    """

    if type(cf_a) != float and type(cf_a) != int:
        print("Bad Type For cf_a")
        return None

    if type(cf_b) != float and type(cf_b) != int:
        print("Bad Type For cf_b")
        return None

    if type(cf_c) != float and type(cf_c) != int:
        print("Bad Type For cf_c")
        return None

    delta = ((cf_b ** 2) - (4 * cf_a * cf_c))

    if delta < 0:
        print("This Equation Does Not Have Roots in real Number")
        return None

    root1 = (-cf_b + delta ** 0.5)/(2*cf_a)
    root2 = (-cf_b - delta ** 0.5)/(2*cf_a)

    roots = [root1, root2]

    return roots


a1 = "Hello"
b1 = [10, 20, 30]
c1 = True

roots = solve_quadratic_eqn(a1, b1, c1)

if roots == None:
    print("Wrong Typed Parameter")

a2 = 10
b2 = 2
c2 = 15
roots = solve_quadratic_eqn(a2, b2, c2)

if roots == None:
    print("Wrong Typed Parameter")

a3 = 4
b3 = 20
c3 = 2
roots = solve_quadratic_eqn(a3, b3, c3)

if roots != None:
    print("Root1 :", roots[0])
    print("Root2 :", roots[1])





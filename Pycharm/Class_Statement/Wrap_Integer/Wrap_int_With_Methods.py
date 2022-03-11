"""
@Author : Rohit Shedage
@Goal : To Implement Wrap Integer Method in wrap class
"""

import sys


class WrapInt:
    """
    Class Wrap integer And its methods
    """
    def __init__(self, init_value: int):
        """
        Parameterized Constructor of wrap int class
        :param init_value: 1st Parameter of class wrap int taking value
        """
        if type(init_value) != int:
            print("Error")
            sys.exit(-1)
        self.value = init_value

    def summation(self, other):
        sum_ = self.value + other.value
        result = WrapInt(sum_)
        return result

    def subtraction(self, other):
        sum_ = self.value - other.value
        result = WrapInt(sum_)
        return result

    def multiplication(self, other):
        sum_ = self.value * other.value
        result = WrapInt(sum_)
        return result

    def division(self, other):
        sum_ = self.value // other.value
        result = WrapInt(sum_)
        return result

    def modulus(self, other):
        sum_ = self.value % other.value
        result = WrapInt(sum_)
        return result

    def show(self, msg):
        print(msg, self.value)


n = WrapInt(10)
m = WrapInt(20)

Addition = n.summation(m)
print(type(Addition))
print(Addition.__dict__)
Addition.show("Given Number Addition is :")

sub = n.subtraction(m)
print(type(sub))
print(sub.__dict__)
sub.show("Given Number subtraction is is :")

quotient = n.division(m)
print(type(quotient))
print(quotient.__dict__)
quotient.show("Given Number quotient is :")

multiplication = n.multiplication(m)
print(type(multiplication))
print(multiplication.__dict__)
multiplication.show("Given Number multiplication is :")

remainder = n.modulus(m)
print(type(remainder))
print(remainder.__dict__)
remainder.show("Given Number remainder is :")

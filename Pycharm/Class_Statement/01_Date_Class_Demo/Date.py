"""
@Author : Rohit Shedage
@Goal : To implement date class
"""


class Date:
    """
    Class To Demonstrate Date
    """

    def __init__(self, init_day: int, init_month: int, init_year: int):
        """
        Date class parameterized constructor
        :param init_day: Taking day integer value
        :param init_month: Taking month integer value
        :param init_year: Taking year integer value
        """

        self.day = init_day
        self.month = init_month
        self.year = init_year


B_day = Date(23, 10, 2000)
Today = Date(22, 11, 2021)

print(B_day.__dict__)
print(Today.__dict__)

print(type(B_day))
print(type(Today))
"""
@Author : Rohit Shedage
@Goal : To Implement Credit Card Class
@Date : 23-11-2021
"""


class Date:
    """
    Date Class implementation
    """

    def __init__(self, dd: int, mm: int, yyyy: int) -> None:
        """
        Parameterized Constructor of Date Class which accept three parameter
        :param dd: It accept day parameter 1 of type integer
        :param mm: It accept month parameter 2 of type integer
        :param yyyy: It accept year parameter 3 of type integer
        :return : None
        """
        self.day = dd
        self.month = mm
        self.year = yyyy


class CreditCard:
    def __init__(self, init_cc_name: str,
                 init_cc_number: int,
                 init_cc_valid_date: tuple,
                 init_expiry_date: tuple,
                 init_cvv: int
                 ) -> None:
        """
        Parameterized Constructor of CreditCard Class and various parameter of CreditCard
        :param init_cc_name: Credit Card holder name
        :param init_cc_number: credit Card Number
        :param init_cc_valid_date: Credit Card issued or valid Date
        :param init_expiry_date: Credit Card Expiry Date
        :param init_cvv: Credit Card CVV Number
        :return: None
        """
        if (type(init_cc_name) != str or
                type(init_cc_number) != int or
                type(init_cc_valid_date) != tuple or
                type(init_expiry_date) != tuple or
                type(init_cvv) != int):

            print("Bad Error For Type")

        self.cc_name = init_cc_name
        self.cc_number = init_cc_number
        self.cc_valid_date = Date(init_cc_valid_date[0], init_cc_valid_date[1], init_cc_valid_date[2])
        self.cc_expiry_date = Date(init_expiry_date[0], init_expiry_date[1], init_expiry_date[2])
        self.cc_cvv = init_cvv


ccobj = CreditCard("Rohit Shedage", 65328974663, (23, 20, 2016), (23, 10, 2040), 101)

print(type(ccobj))
print(ccobj.__dict__)


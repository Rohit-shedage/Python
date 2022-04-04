"""
    Syntax 6:- 
        L = [g(f(x),f(y)) for x in range(1,5) for y in range(6,11)]
        L = [x**2+y**3 for x in range(5,8) for y in range(6,11)]
        INNER WORKING
        S1 :- Split Iter1-> temp1
              1 2 3 4 
              Split Iter2->temp2
              5 6 7
        S2 :- Apply f(x) on all element
              tmp1 => 1 4 9 16 
              Apply f(y) on all element
              tmp1 => 125 216 343
        S3 :- Take Cartesian product of tmp1 X tmp2
              (1,125),(1,216),(1,343),
              (4,125),(4,216),(4,343),
              (9,125),(9,216),(9,343),
              (16,125),(16,216),(16,343),
              
        S4 :- Apply g(f(x), f(y)) means apply
              + operator on cartesian product and 
              convert to list.
              ['126','217','344',
               '129','220','347',
               '134','225','352',
               '141','232','359']
              
"""

import sys

def main():

    L = [x**2+y**3 for x in range(1,5) for y in range(5,8)]
    print("L:", L)
    """
        S1 :- Split Iter1-> temp1
              1 2 3 4 
              Split Iter2->temp2
              5 6 7
        S2 :- Apply f(x) on all element
              tmp1 => 1 4 9 16 
              Apply f(y) on all element
              tmp1 => 125 216 343
        S3 :- Take Cartesian product of tmp1 X tmp2
              (1,125),(1,216),(1,343),
              (4,125),(4,216),(4,343),
              (9,125),(9,216),(9,343),
              (16,125),(16,216),(16,343),
              
        S4 :- Apply g(f(x), f(y)) means apply
              + operator on cartesian product and 
              convert to list.
              ['126','217','344',
               '129','220','347',
               '134','225','352',
               '141','232','359']
    """

    sys.exit(0)

if __name__ == '__main__':
    main()
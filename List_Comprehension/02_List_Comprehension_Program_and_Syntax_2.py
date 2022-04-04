"""
    Syntax 2:-
        Abtract Syntax:
        L = [Function of x f(x) for variable in Iterable]

        eg :-   
            L = [x**2 for x in range(1,6)]
            INNER WORKING

            def f(x):
                return x**2
            
            df = range(1,6)

            L = [f(x) for x in df]

            L = [x**2 for x in range(1,6)]
            OUTPUT :-
                ['1','4','9','16','25']
                ['1','4','9','16','25]
"""

import sys

def f(x):
    return x**2

def main():

    df = range(1,6)

    L1 = [f(x) for x in df]
    print("L1:", L1)

    L2 = [x**2 for x in range(1,6)]
    print("L2:", L2)
    """
        S1 :- Split the range 1 2 3 4 5
        S2 :- Pass to Funtion x**2
              1 4 9 16 25
    """

    sys.exit(0)

if __name__ == '__main__':
    main()

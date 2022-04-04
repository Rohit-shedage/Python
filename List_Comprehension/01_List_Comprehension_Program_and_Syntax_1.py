"""
Syntax 1 :-
    L = [Variable for Variable in Iterable]
    eg:-
        L = [x for x in range(1,10)]

        C = [c for c in "Hello"]

        OUTPUT :-
                ['1','2','3','4','5','6','7','8','9']
                ['H','e','l','l','o']
"""

import sys

def main():

    L = [x for x in range(1,10)]
    print("L:",L)

    C = [c for c in "Hello"]
    print("C:", C)

    sys.exit(0)

if __name__ == '__main__':
    main()
"""
    Syntax 3:-
        L = [Variable for Variable in Iterable Condition]

        eg:-
            L = [x for x in range(1,6) if x%2 == 0]

            INNER WORKING :-
                S1:- Split Iterable in constituent element
                    1 2 3 4 5 
                S2 :- Apply Condition on them and
                      Shortlist those which satisfied
                      the condition x%2 == 0
                      2 4
                S3 :- Apply Variable which have shortlisted
                      from S2 and Applied list on them
            
            OUTPUT :- 
                ['2','4']
"""

import sys

def main():

    L = [x for x in range(1,10) if x%2 == 0]
    """
        S1 :- 1 2 3 4 5 6 7 8 9
        S1 :- 2 4 6 8
        S3 :- ['2','4','6','8']
    """
    print("L:", L)

    sys.exit(0)

if __name__ == '__main__':
    main()
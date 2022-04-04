"""
    Syntax 4:-
        L = [Function of x f(x) for variable in Iterable Condition]
    eg :- 
        L = [f(x) for x in range(1,10) if x%2 == 0]

        INNER WORKING
            S1 :- SPlit Iterable in Constituent element
                  1 2 3 4 5 6 7 8 9
            S2 : Apply COndition c on all of them and 
                 Shortlist those which have satisfied
                 the condition
                 2  4  6  8
            S3 : Apply F(x) on all element which 
                 has been shortlisted in S2 and 
                 form list out of them
                 f(x) :- 4 16 36 64
                 ['4','16','36','64']
"""
import sys

def main():
    
    L = [x**2 for x in range(1,10) if x%2 == 0]
    """
     S1 :- 1 2 3 4 5 6 7 8 9
     S2 :- 2 4 6 8
     S3 :- 4 16 36 64
           ['4','16','36','64']
    """
    print("L:", L)

    sys.exit(0)

if __name__ == '__main__':
    main()
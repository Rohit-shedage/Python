""" 
 Two Variable Version Now Applying Condition on it.
 Syntax 8:-
    L = [g(f(x),f(y)) for x in range(6,15) for y in range(1,8) if x%2 == 0 if y%2 == 1]
    L = [x**2+y**3 for x in range(6,15) for y in range(1,8) if x%2 == 0 if y%2 == 1]
    S1 :- Split Iter1 -> tmp1
          6 7 8 9 10 11 12 13 14
          Apply C1 Condition on tmp1
          x%2 == 0 => 6 8 10 12 14
          Apply f(x) on c1.tmp1->f1.tmp1
          36 64 100 144 196
    S2 :- Split Iter2 -> tmp2
          1 2 3 4 5 6 7
          Apply C2 Condition on tmp1
          y%2 == 1 => 1 3 5 7
          Apply f(y) on c2.tmp2->f2.tmp2
          1 27 125 343
    S3 :- Take Cartesian Product tmp1 X tmp2 And Convert to list
          (36,1),(36,27),(36,125),(36,343),
          (64,1),(64,27),(64,125),(64,343),
          (100,1),(100,27),(100,125),(100,343),
          (144,1),(144,27),(144,125),(144,343),
          (196,1),(196,27),(196,125),(196,343)
    S4 :- Apply + operator on cartesian products
          (36+1),(36+27),(36+125),(36+343),
          (64+1),(64+27),(64+125),(64+343),
          (100+1),(100+27),(100+125),(100+343),
          (144+1),(144+27),(144+125),(144+343),
          (196+1),(196+27),(196+125),(196+343)

          ['37','63','161','379',
           '65','91','189','407',
           '101','127','225','443',
           '145','171','269','487',
           '197','223','321','539',]

"""

import sys

def main():

    L = [x**2+y**3 for x in range(6,15) for y in range(1,8) if x%2 == 0 if y%2 == 1]
    print("L:", L)
    """
    S1 :- Split Iter1 -> tmp1
          6 7 8 9 10 11 12 13 14
          Apply C1 Condition on tmp1
          x%2 == 0 => 6 8 10 12 14
          Apply f(x) on c1.tmp1->f1.tmp1
          36 64 100 144 196
    S2 :- Split Iter2 -> tmp2
          1 2 3 4 5 6 7
          Apply C2 Condition on tmp1
          y%2 == 1 => 1 3 5 7
          Apply f(y) on c2.tmp2->f2.tmp2
          1 27 125 343
    S3 :- Take Cartesian Product tmp1 X tmp2 And Convert to list
          (36,1),(36,27),(36,125),(36,343),
          (64,1),(64,27),(64,125),(64,343),
          (100,1),(100,27),(100,125),(100,343),
          (144,1),(144,27),(144,125),(144,343),
          (196,1),(196,27),(196,125),(196,343)

    S4 :- Apply + operator on cartesian products     
          ['37','63','161','379',
           '65','91','189','407',
           '101','127','225','443',
           '145','171','269','487',
           '197','223','321','539',]
    """

    sys.exit(0)

if __name__ == '__main__':
    main()
"""
 Last Version of list comprehension
 Syntax 9:-
 L = [g(f(x1),f(x2),....,f(n)) 
                    for variable_1 in Iterable_1 if C1(x1)
                    for variable_2 in Iterable_2 if C2(x2)
                    .
                    .
                    .
                    for variable_n in Iterable_n if Cn(xn)

                    if MasterCondition(g(f(x1),f(x2),....,f(n)))
      ]

  L = [x**2-y**3+z**4 for x in range(1,10) if x % 2 == 0 
                      for y in range(5,15) if y % 3 == 2 
                      for z in range(3,8) if z % 2 == 1
                      if (x**2-y**3+z**4) > 0]

   
    S1 :- Split Iter1 -> tmp1
          1 2 3 4 5 6 7 8 9
          Apply C1 Condition on tmp1
          x%2 == 0 => 2 4 6 8
          Apply f(x) on c1.tmp1->f1.tmp1
          4 16 36 64
    S2 :- Split Iter2 -> tmp2
          5 6 7 8 9 10 11 12 13 14 
          Apply C2 Condition on tmp2
          y%3 == 2 => 5 8 11 14
          Apply f(y) on c2.tmp2->f2.tmp2
          125 512 1331 2744
    S3 :- Split Iter3 -> tmp3
          3 4 5 6 7 
          Apply C3 Condition on tmp3
          z%2 == 1 => 3 5 7
          Apply f(z) on c3.tmp3->f3.tmp3
          81 625 2401
    S4 :- Take Cartesian Product tmp1 X tmp2 And Convert to list
          (4,125,81),(4,125,625),(4,125,2401),
          (4,512,81),(4,512,625),(4,512,2401),
          (4,1331,81),(4,1331,625),(4,1331,2401),
          (4,2744,81),(4,2744,625),(4,2744,2401),

          (16,125,81),(16,125,625),(16,125,2401),
          (16,512,81),(16,512,625),(16,512,2401),
          (16,1331,81),(16,1331,625),(16,1331,2401),
          (16,2744,81),(16,2744,625),(16,2744,2401),

          (36,125,81),(36,125,625),(36,125,2401),
          (36,512,81),(36,512,625),(36,512,2401),
          (36,1331,81),(36,1331,625),(36,1331,2401),
          (36,2744,81),(36,2744,625),(36,2744,2401),

          (64,125,81),(64,125,625),(64,125,2401),
          (64,512,81),(64,512,625),(64,512,2401),
          (64,1331,81),(64,1331,625),(64,1331,2401),
          (64,2744,81),(64,2744,625),(64,2744,2401),
          
    S5 :- Apply Function g on every tuple in cartesian product of S4
          (4 - 125 + 81),(4 - 125 + 625),(4 - 125 + 2401),
          (4 - 512 + 81),(4 - 512 + 625),(4 - 512 + 2401),
          (4 - 1331 + 81),(4 - 1331 + 625),(4 - 1331 + 2401),
          (4 - 2744 + 81),(4 - 2744 + 625),(4 - 2744 + 2401),

          (16 - 125 + 81),(16 - 125 + 625),(16 - 125 + 2401),
          (16 - 512 + 81),(16 - 512 + 625),(16 - 512 + 2401),
          (16 - 1331 + 81),(16 - 1331 + 625),(16 - 1331 + 2401),
          (16 - 2744 + 81),(16 - 2744 + 625),(16 - 2744 + 2401),

          (36 - 125 + 81),(36 - 125 + 625),(36 - 125 + 2401),
          (36 - 512 + 81),(36 - 512 + 625),(36 - 512 + 2401),
          (36 - 1331 + 81),(36 - 1331 + 625),(36 - 1331 + 2401),
          (36 - 2744 + 81),(36 - 2744 + 625),(36 - 2744 + 2401),

          (64 - 125 + 81),(64 - 125 + 625),(64 - 125 + 2401),
          (64 - 512 + 81),(64 - 512 + 625),(64 - 512 + 2401),
          (64 - 1331 + 81),(64 - 1331 + 625),(64 - 1331 + 2401),
          (64 - 2744 + 81),(64 - 2744 + 625),(64 - 2744 + 2401),

          -40    504  2280 
          -425   117  1893
          -1246 -702  1074
          -2659 -2114 -339

          -28    516  2296
          -415   129  1905
          -1234 -690  1086
          -2647 -2103 -327

          -8     536   2312
          -396   149   1925
          -1214 -670   1106
          -2627 -2083  -307

          20     564   2340
          -367   177   1956
          -1186 -642   1134
          -2599 -2055  -279
    S6 :- Apply MasterCondition if (x**2-y**3+z**4) > 0
          ['504','2280','117','1893','1074',
           '516','2296','129','1905','1086',
           '536','2312','149','1925','1106',
           '20','564','2340','177','1956','1134']
"""

import sys

def main():

    L = [x**2-y**3+z**4 for x in range(1,10) if x % 2 == 0 
                      for y in range(5,15) if y % 3 == 2 
                      for z in range(3,8) if z % 2 == 1
                      if (x**2-y**3+z**4) > 0
      ]
    print("L:", L)
    
    """


   
    S1 :- Split Iter1 -> tmp1
          1 2 3 4 5 6 7 8 9
          Apply C1 Condition on tmp1
          x%2 == 0 => 2 4 6 8
          Apply f(x) on c1.tmp1->f1.tmp1
          4 16 36 64
    S2 :- Split Iter2 -> tmp2
          5 6 7 8 9 10 11 12 13 14 
          Apply C2 Condition on tmp2
          y%3 == 2 => 5 8 11 14
          Apply f(y) on c2.tmp2->f2.tmp2
          125 512 1331 2744
    S3 :- Split Iter3 -> tmp3
          3 4 5 6 7 
          Apply C3 Condition on tmp3
          z%2 == 1 => 3 5 7
          Apply f(z) on c3.tmp3->f3.tmp3
          81 625 2401
    S4 :- Take Cartesian Product tmp1 X tmp2 And Convert to list
          (4,125,81),(4,125,625),(4,125,2401),
          (4,512,81),(4,512,625),(4,512,2401),
          (4,1331,81),(4,1331,625),(4,1331,2401),
          (4,2744,81),(4,2744,625),(4,2744,2401),

          (16,125,81),(16,125,625),(16,125,2401),
          (16,512,81),(16,512,625),(16,512,2401),
          (16,1331,81),(16,1331,625),(16,1331,2401),
          (16,2744,81),(16,2744,625),(16,2744,2401),

          (36,125,81),(36,125,625),(36,125,2401),
          (36,512,81),(36,512,625),(36,512,2401),
          (36,1331,81),(36,1331,625),(36,1331,2401),
          (36,2744,81),(36,2744,625),(36,2744,2401),

          (64,125,81),(64,125,625),(64,125,2401),
          (64,512,81),(64,512,625),(64,512,2401),
          (64,1331,81),(64,1331,625),(64,1331,2401),
          (64,2744,81),(64,2744,625),(64,2744,2401),
          
    S5 :- Apply Function g on every tuple in cartesian product of S4
          (4 - 125 + 81),(4 - 125 + 625),(4 - 125 + 2401),
          (4 - 512 + 81),(4 - 512 + 625),(4 - 512 + 2401),
          (4 - 1331 + 81),(4 - 1331 + 625),(4 - 1331 + 2401),
          (4 - 2744 + 81),(4 - 2744 + 625),(4 - 2744 + 2401),

          (16 - 125 + 81),(16 - 125 + 625),(16 - 125 + 2401),
          (16 - 512 + 81),(16 - 512 + 625),(16 - 512 + 2401),
          (16 - 1331 + 81),(16 - 1331 + 625),(16 - 1331 + 2401),
          (16 - 2744 + 81),(16 - 2744 + 625),(16 - 2744 + 2401),

          (36 - 125 + 81),(36 - 125 + 625),(36 - 125 + 2401),
          (36 - 512 + 81),(36 - 512 + 625),(36 - 512 + 2401),
          (36 - 1331 + 81),(36 - 1331 + 625),(36 - 1331 + 2401),
          (36 - 2744 + 81),(36 - 2744 + 625),(36 - 2744 + 2401),

          (64 - 125 + 81),(64 - 125 + 625),(64 - 125 + 2401),
          (64 - 512 + 81),(64 - 512 + 625),(64 - 512 + 2401),
          (64 - 1331 + 81),(64 - 1331 + 625),(64 - 1331 + 2401),
          (64 - 2744 + 81),(64 - 2744 + 625),(64 - 2744 + 2401),

          -40    504  2280 
          -425   117  1893
          -1246 -702  1074
          -2659 -2114 -339

          -28    516  2296
          -415   129  1905
          -1234 -690  1086
          -2647 -2103 -327

          -8     536   2312
          -396   149   1925
          -1214 -670   1106
          -2627 -2083  -307

          20     564   2340
          -367   177   1956
          -1186 -642   1134
          -2599 -2055  -279
    S6 :- Apply MasterCondition if (x**2-y**3+z**4) > 0
          ['504','2280','117','1893','1074',
           '516','2296','129','1905','1086',
           '536','2312','149','1925','1106',
           '20','564','2340','177','1956','1134']
    """

    sys.exit(0)

if __name__ == '__main__':
    main()
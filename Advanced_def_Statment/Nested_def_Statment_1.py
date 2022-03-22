#-------
# Program
from tkinter.constants import N


a = 10
b = 20

def f():
    m = 10
    n = 20
    p = m + n
    def g():
        L = [10, 20, 30, 40]
        for x in L:
            print(x)
    print(p)
    g()
    print(m, n)
print(a)
f()
# g() ERROR :- g() is not defined
print(b)
D = {"a":10, "b":20, "c":30}

def f():
    L = [100, 200, 300, 400]
    def g():
        s = "Hello"
        for c in s:
            print(c)
        def h():
            T = (1000, 2000, 300)
            for x in T:
                print(x)
        for c in s:
            print(c*2)
        h()
    for x in L:
        print(x**2)
    g()
    for x in L:
        print(x+1)

for key in D.keys():
    print(key, D[key])

f()
print("END")
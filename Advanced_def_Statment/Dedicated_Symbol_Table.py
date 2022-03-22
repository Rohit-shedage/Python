n = 10
print(n)
n = 100
print(n)

print("IL0:", locals())

def f():
    n = 3.14
    print(n)
    print("IL1:", locals())

f()
"""
@Author : RS
@Goal : To Demonstrate Basic List Operation
"""

L = [10, 20, 30, 40, 50]

# Built-ins with which list object can be used

print("L:", L)

n= len(L)

print("Length Of the List is:", n)
print("Type(L):", type(L))
print("id(L) :", id(L))

# Operators on List
# Concatenation

L1 = [10, 20, 30, 40, 50]
L2 = [40, 50, 60, 70, 80, 90, 100]
# L3 = L1 + L2
L3 = list.__add__(L1, L2)
print("id(L1) :", id(L1))
print("L1 :", L1)
print("L2 :", L2)
print("L3 :", L3)

# Multiplication By Integer

L = [True, 10, 3.14, "Hello"]
M = L * 2

print("L :", L)
print("M :", M)

n = L * 3
print("n :", n)

# Index Operator

L = [10, 20, 30, 40]
i = 0

while i < len(L):
    print("L[", i, "] :", L[i])
    i = i + 1

# Index Assignment

print("L :", L)
print("id(L[0]) :", id(L[0]))
L[0] = 100
print("L :", L)
print("id(L[0]) :", id(L[0]))

print("L :", L)
print("id(L[1]) :", id(L[1]))
L[1] = 200
print("L :", L)
print("id(L[1]) :", id(L[1]))

print("L :", L)
print("id(L[2]) :", id(L[2]))
L[2] = 300
print("L :", L)
print("id(L[2]) :", id(L[2]))

print("L :", L)
print("id(L[3]) :", id(L[3]))
L[3] = 400
print("L :", L)
print("id(L[3]) :", id(L[3]))

# Membership Test

L = [100, 200, 300, 400, 500]
b1 = (100 in L)  # Object in Container
print("b1 :", b1)

b2 = (1000 in L)
print("b2 :", b2)

"""
str_n = input("Enter a Number To Check in List :")
n = int(str_n)

if n in L:
    print(n, "is Present in Given List L:", L)

else :
    print(n, "is not Present in Given List L:", L3)
"""

# object.function(arguments)
# How to add one object to a list(atomic or container)

L = []
print("L:", L)
L.append(1000)
print("L:", L)
L.append(2000)
print("L:", L)
# list.__append__(L, 3000)
list.append(L, 3000)
print("L:", L)
L.append(4000)
print("L:", L)

M = [-1, -2, -3]
L.append(M)
print("L:", L)

# Adding Element in other container individually

L.extend(M)
print("L:", L)

# Index based removal
L = [10, 20, 30, 40]
print("Before del L[0]:")
i = 0
while i < len(L):
    print(i, L[i])
    i = i + 1
del L[2]
print("After del L[0]:")

i = 0
while i < len(L):
    print(i, L[i])
    i = i + 1

"""
Generalization :
      del L[i] will remove element at index i
      from the container all element from i + 1
      to len(L) - 1 will have indices i to len(2) - 2
      after del L[i] is complete
      
      while doing del L[i]
      we must ensure
      0 <= i < len(L)
      other we will getIndex Error
"""

# Data based removal

L = [100, 200, 300, 400]
print("Before L.remove(300): L:", L)

L.remove(300)
print("After L.remove(300): L:", L)

"""
Gneralization: 
    L.remove(data)
    The first occurrence of data will be
    removed from L index 
    Index readjustment = same as what happens in del L[i]
    
    Data must exit in container L otherwise we will get valueError
"""
# sort()
L1 = [50, 40, 30, 20, 10]
L2 = [5.5, 4.6, 2.3, 1.1, 3.4]
L3 = [50, 4.4, 6, 3.5, 1.2, 1, 20, 60, 30]
L4 = ["Hello", "Python", 'advanced', 'Batch']

print("Before sort : L1:", L1)
L1.sort()
print("After sort : L1:", L1)

print("Before sort : L2:", L2)
L2.sort()
print("After sort : L2:", L2)

print("Before sort : L3:", L3)
L3.sort()
print("After sort : L3:", L3)

print("Before sort : L4:", L4)
L4.sort()
print("After sort : L4:", L4)

# reverse
L = [10, 20, 30, 40, 50]
print("L:", L)
L.reverse()
print("L After first reverse :L:", L)
L.reverse()
print("L After second reverse :L:", L)

# Index Method
L = [10, 20, 30, 40, 50]
print("L.index(10) :", L.index(10))
print("L.index(20) :", L.index(20))
print("L.index(30) :", L.index(30))
print("L.index(40) :", L.index(40))
print("L.index(50) :", L.index(50))

L = [10, 20, 30, 10, 50, 10, 30, 90]
print("L.index(10):", L.index(10))
print("L.index(10,1):", L.index(10, 1))  # Starting Index Of Searching Element in list
print("L.index(10):", L.index(10, 4))

# Count

print("L.count(10) :", L.count(10))
print("L.count(20) :", L.count(20))





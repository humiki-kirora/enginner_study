from math import *

def add(a,b):
    assert len(a) == len(b)
    return [x + y for x,y in zip(a,b)]

def subtract(a,b):
    assert len(a) == len(b)
    return [x - y for x,y in zip(a,b)]

def product(a,b):
    assert len(a) == len(b)
    return [x * y for x,y in zip(a,b)]

def div(a,b):
    assert len(a) == len(b)
    return [x / y for x,y in zip(a,b)]

def dot(a,b):
    assert len(a) == len(b)
    num = 0
    for x,y in zip(a,b):
        num += x * y
    return num

def cross(a,b):
    assert len(a) == len(b)
    assert len(a) == 3
    return [a[1] * b[2] - a[2] * b[1],a[2] * b[0] - a[0] * b[2],a[0] * b[1] - a[1] * b[0]]

def L1norm(a):
    num = 0
    for x in a:
        num += abs(x)
    return num

def L2norm(a):
    return sqrt(dot(a,a))

def Linfnorm(a):
    return max(a)

a =[1,2,3]
b = [4,5,6]

print(add(a,b))
print(subtract(a,b))
print(product(a,b))
print(div(a,b))

print(dot(a,b))
print(cross(a,b))

print(L1norm(a))
print(L2norm(a))
print(Linfnorm(a))


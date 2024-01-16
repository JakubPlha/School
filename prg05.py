import random
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

if a>b and a>c and a>d and a>e:
    print("a je největší")

if b>a and b>c and b>d and b>e:
    print("b je největší")

if c>a and b<c and c>d and c>e:
    print("c je největší")

if d>a and d>c and b<d and d>e:
    print("d je největší")

if e>a and e>c and e>d and b<e:
    print("e je největší")
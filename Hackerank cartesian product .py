from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

AB = (product(A,B))

for i in AB:
    print(i,end='')
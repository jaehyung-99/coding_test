import sys

n1 = int(input())
l1 = set(map(int, sys.stdin.readline().split()))
n2 = int(input())
l2 = list(map(int, sys.stdin.readline().split()))

for i in l2:
    if i in l1:
        print(1)
    else:
        print(0)
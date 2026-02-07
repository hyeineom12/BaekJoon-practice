import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

b = 0
prior = 0
A = None

for i in range(n) :
    if a[i] == A :
        prior *= 2
        b += prior
    else :
        prior = 2
        b += prior

    if b >= 100 :
        b = 0
        prior = 0
        A = None
        continue

    A = a[i]

print(b)

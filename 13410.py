import sys

N, K = map(int, sys.stdin.readline().split())

numlist = []
for i in range(1, K + 1) : 
    num = str(N * i)[::-1]

    numlist.append(int(num))

print(max(numlist))


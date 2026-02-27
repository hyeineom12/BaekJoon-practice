import sys

N = int(sys.stdin.readline())
pre = list(sys.stdin.readline().strip().split())
h = list(sys.stdin.readline().strip().split())


for i in range(N) :
    if pre[i] not in h :
        print(pre[i])
        break

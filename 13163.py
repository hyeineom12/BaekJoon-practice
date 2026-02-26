import sys

N = int(sys.stdin.readline())
name = []

for _ in range(N) :
    n = list(sys.stdin.readline().strip().split())
    na = ''

    for i in range(1, len(n)) :
        na += n[i]
    
    name.append(na)


for i in range(N) :
    print("god"+name[i])
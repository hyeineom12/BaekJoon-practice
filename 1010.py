import sys

T = int(sys.stdin.readline().strip())
result = []

for _ in range(T) :
    N, M = map(int, sys.stdin.readline().strip().split())
    up = 1
    down = 1
    # M P N
    for i in range(1, M + 1) :
        up *= i
    
    if M - N != 0 : 
        for j in range(1, M - N + 1) :
            down *= j
        for k in range(1, N + 1) :
            down *= k
    else :
        result.append(1)
        continue
    
    result.append(up // down)

for r in result :
    print(r)
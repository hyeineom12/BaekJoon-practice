import sys

T = int(sys.stdin.readline())
result = []

for _ in range(T) :
    m, n = map(int, sys.stdin.readline().split())
    M = []
    count = 0

    for i in range(m) :
        M.append(list(map(int, sys.stdin.readline().split())))
    
    for j in range(n) :
        zero = 0
        for k in range(m-1, -1, -1) :
            if M[k][j] == 0 :
                zero += 1
            else :
                count += zero
    
    result.append(count)

        

for i in range(T) :
    print(result[i])
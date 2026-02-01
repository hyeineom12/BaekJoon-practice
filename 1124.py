import sys

A, B = map(int, sys.stdin.readline().split())

result = 0

for i in range(A, B + 1) :
    cnt = 0
    dec = True
    x = i
    d = 2

    while d * d <= x :
        while x % d == 0 :
            x = x // d
            cnt += 1
        d += 1
    
    if x > 1 :
        cnt += 1
    
    if cnt < 2 :
        continue
    
    for j in range(2, cnt) :
        if cnt % j == 0 :
            dec = False
            break
    
    if dec :
        result += 1
    
    
print(result)




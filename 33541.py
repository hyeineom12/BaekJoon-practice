import sys

x = sys.stdin.readline()
n = int(x) + 1

while True :
    x1, x2 = int(str(n)[:2]), int(str(n)[2:])

    if n > 9999 :
        print(-1)
        break
    else :
        if (x1 + x2)**2 == n :
            print(n) 
            break
        else :
            n += 1


import sys

L, R = sys.stdin.readline().split()


if len(L) != len(R) :
    print(0)
else :
    count = 0

    for i in range(len(R)) :
        if L[i] == R[i] == '8':
            count += 1
        else :
            break
    print(count)

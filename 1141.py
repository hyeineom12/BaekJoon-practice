N = int(input())
A = []

for _ in range(N) :
    A.append(input())

A.sort()

cnt = 0
pre = []

for i in range(N-1) :
    if A[i] == A[i+1][0:len(A[i])] :
        continue
    else :
        cnt += 1

cnt += 1

print(cnt)
        
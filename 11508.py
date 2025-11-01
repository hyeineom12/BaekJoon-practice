N = int(input())
C = []
result = []
for i in range(N) :
    x = input()
    C.append(int(x))

C.sort()

while len(C) >= 3 :
    result.append(C[1]) 
    result.append(C[len(C)-1])
    del C[len(C)-1]
    del C[1]
    del C[0]

for i in range(len(C)) :
    result.append(C[i])

X = 0
for i in range(len(result)) :
    X += int(result[i])

print(X)
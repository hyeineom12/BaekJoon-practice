x = input()
N = int(x.split()[0])
A = int(x.split()[1])
B = int(x.split()[2])

T = 1
F = 1
Y = 0

for i in range(N) :
    T += A
    F += B

    if T < F :
        Y = T
        T = F
        F = Y
    elif T == F :
        F = F - 1


print(T, F)

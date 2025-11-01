X = input()
s = input()
command = []

#N과 M 나누기
N = int(X.split()[0])
M = int(X.split()[1])

#s를 리스트에 대입하기
List = []
for i in range(N) :
    List.append(int(s.split()[i]))

# ?엥 M번째 줄이여야 맞는거 아닌가??
for i in range(M) :
    m = input()
    command.append(m)

for i in range(M) :
    a = int(command[i].split()[0])
    b = int(command[i].split()[1])
    c = int(command[i].split()[2])

    if a == 1 :
        List[b-1] = c
    elif a == 2 :
        for j in range(b-1, c) :
            if List[j] == 1 :
                List[j] = 0
            else :
                List[j] = 1
    elif a == 3 :
        for k in range(b-1, c) :
            List[k] = 0
    else :
        for y in range(b-1, c) :
            List[y] = 1

for i in range(N) :
    print(List[i], end = " ")
print()
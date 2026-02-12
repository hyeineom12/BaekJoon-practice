import sys

x = sys.stdin.readline().strip()

isFA = []
p = True

X = int(x[0]) * len(x)
isFA.append(X)

while True :
    if X in isFA :
        print("FA")
        p = False
        break
    isFA.append(X)

    if len(str(X)) == 1 :
        break

    X = int(x[0]) * len(str(X))

if p :
    print("NFA")

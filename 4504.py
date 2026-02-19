import sys

n = int(sys.stdin.readline().strip())
numlist = []

while True :
    num = int(sys.stdin.readline().strip())

    if num == 0 :
        break

    numlist.append(num)

for i in numlist :
    if i % n == 0 :
        print(f'{i} is a multiple of {n}.')
    else :
        print(f'{i} is NOT a multiple of {n}.')

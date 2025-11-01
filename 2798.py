from itertools import combinations

main = input("")

N = int(main.split(" ")[0])
M = int(main.split(" ")[1])

num = input("")

close = 999999999
numlist = []
result = 0
many = int((N * (N-1) * (N-2)) / 3 * 2 * 1)

for i in range(0,N) :
    numlist.append(num.split(" ")[i])

newlist = list(combinations(numlist, 3))

for i in range(0,len(newlist)) :
        newlist[i] = int(newlist[i][0]) + int(newlist[i][1]) + int(newlist[i][2])

for i in range(0,len(newlist)) :
      if abs(newlist[i]-M) < close :
            close = abs(newlist[i] - M)
            result = newlist[i]

print(result)
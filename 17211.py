import sys

N, feel = map(int, sys.stdin.readline().strip().split())
qlist = list(map(float, sys.stdin.readline().strip().split()))

if feel == 0 :
    good = 1
    bad = 0
else :
    good = 0
    bad = 1

for i in range(N) :
    nextgood = good * qlist[0] + bad * qlist[2]
    nextbad = good * qlist[1] + bad * qlist[3]

    good = nextgood
    bad = nextbad

print(round(nextgood * 1000))
print(round(nextbad * 1000))
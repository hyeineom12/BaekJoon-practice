import sys

S = sys.stdin.readline().strip()
time1 = ['1)', '(1', '()']


if S == '(1)' :
    print(0)
elif any(x in S for x in time1) :
    print(1)
else :
    print(2)
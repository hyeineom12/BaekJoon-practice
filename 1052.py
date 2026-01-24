import sys

N, K = map(int, sys.stdin.readline().split())

cnt = 0

while True :
    two = format(N, 'b')
    bottle = two.count('1')

    if bottle <= K :
       break
    
    idx = two.rfind('1')
    add = 2 ** (len(two) - idx - 1)
    N += add
    cnt += add

print(cnt)
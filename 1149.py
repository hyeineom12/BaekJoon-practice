import sys

N = int(sys.stdin.readline())
cost = []

for _ in range(N) :
    cost.append(list(map(int, sys.stdin.readline().split())))

R, G, B = cost[0]

for i in range(1, N) :
    r, g, b = R, G, B
    R = cost[i][0] + min(g, b)
    G = cost[i][1] + min(r, b)
    B = cost[i][2] + min(r, g)

print(min(R, G, B))

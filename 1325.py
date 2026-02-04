import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M) :
    A, B = map(int, sys.stdin.readline().split())
    graph[B].append(A)

count_list = [0] * (N+1)
visited = [0] * (N+1)
visit_id = 0

for i in range(1, N+1) :
    count = 1

    visit_id += 1
    dq = deque()
    dq.append(i)
    visited[i] = visit_id

    while dq :
        now = dq.popleft()

        for next in graph[now] :
            if visited[next] != visit_id :
                visited[next] = visit_id
                dq.append(next)
                count += 1

    count_list[i] = count

max_count = max(count_list)
for i in range(1, N+1) :
    if count_list[i] == max_count :
        print(i, end = ' ')
import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
board = []
Wresult = 0
Bresult = 0

for _ in range(N) :
    board.append(list(sys.stdin.readline().rstrip()))

dq = deque()
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[False] * M for _ in range(N)]

for br in range(N) :
    for bc in range(M) :

        if not visited[br][bc] : # 방문을 하지 않았을 때 
            dq.append((br, bc))
            visited[br][bc] = True
            count = 1

            while dq : # dq 안에 값이 있을 때 
                r, c = dq.popleft()

                for i in range(4) :
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if (0 <= nr < N and 0 <= nc < M and board[nr][nc] == board[r][c] and not visited[nr][nc]) :
                        visited[nr][nc] = True
                        dq.append((nr, nc))
                        count += 1
        
            if board[br][bc] == 'W' :
                Wresult += count * count
            else :
                Bresult += count * count


print(Wresult, Bresult)

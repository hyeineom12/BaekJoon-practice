import sys

N, H, W = map(int, sys.stdin.readline().split())
st = []
result = ['?'] * N

for _ in range(H) :
    st.append(sys.stdin.readline().strip())

for i in range(N) :
    start = i * W
    for row in range(H) :
        for col in range(W) :
            if st[row][start + col] != '?' :
                result[i] = st[row][start + col]

       
for i in range(N) :
    print(result[i], end='')

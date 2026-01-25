N, M = map(int, input().split())

A = []
for _ in range(N) :
    A.append(list(map(int, input())))
    # 3

B = []
for _ in range(N) :
    B.append(list(map(int, input())))
    # 4

# count = 0

# if A > 3 and B > 3 :
#     for i in range(N - 3) :
#         for j in range(M - 3) :
#             if A[i][j] != B[i][j] : 
#                 A[i:i + 3][j:j+3] = 1 - A[i:i + 3][j:j+3]
#                 count += 1

# if not count :
#     print(-1)
# else :
#     print(count)

print(A[0][0])
print(B[0][0])
print(A[2][1])
print(B[2][1])
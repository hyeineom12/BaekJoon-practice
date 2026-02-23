import sys

T = int(sys.stdin.readline())
P = []

for _ in range(T) :
    B = int(sys.stdin.readline())
    S = sys.stdin.readline().strip()
    result = ''

    S = S.replace('I', '1').replace('O', '0')

    for i in range(B) :
        I = int(S[:8], 2)
        result += chr(I)
        
        S = S[8:]
    
    P.append(result)

    
for i in range(T) :
    print(f'Case #{i + 1}: {P[i]}')
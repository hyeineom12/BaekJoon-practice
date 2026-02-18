import sys

N = int(sys.stdin.readline().strip())
positive = ["Never gonna give you up", 
"Never gonna let you down", 
"Never gonna run around and desert you", 
"Never gonna make you cry", 
"Never gonna say goodbye", 
"Never gonna tell a lie and hurt you", 
"Never gonna stop"]

now = True

for _ in range(N) :
    S = sys.stdin.readline().strip()

    if S not in positive :
        now = False

if now :
    print("No")
else :
    print("Yes")
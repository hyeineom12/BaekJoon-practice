import sys

while True :
    tri = list(map(int, sys.stdin.readline().split()))
    tri.sort()

    if all(i == 0 for i in tri) :
        break
    
    if tri[-1] >= tri[0] + tri[1] :
        print("Invalid")
    else :
        tri_set = set(tri)

        if len(tri_set) == 1 :
            print("Equilateral")
        elif len(tri_set) == 2 :
            print("Isosceles")
        else :
            print("Scalene")

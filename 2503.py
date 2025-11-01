time = input()

not_result = set()
result = []
process1 = []
process2 = []


for i in range(0,int(time)) :
    q = input().split()

    q1 = q[0]
    q2 = q[1]
    q3 = q[2]

    if q[2] == "0" :
        not_result.add(q1[0])
        if q1[1] not in not_result:
            not_result.add(q1[1])
        if q1[2] not in not_result:
            not_result.add(q1[2])
    else :
        pass

    if int(q[1]) == 1 :
        process1.append(q[0])
    else :
        pass

    if int(q[1]) == 2 :
        process2.append(q[1])



# 저는 총 가능한 숫자의 갯수가 9^3이니 거기에서 불가능 한 숫자를 빼고(0 볼이 나온 숫자)
# 나머지 스트라이크로 추려내려고 하였으나 도저히 문제를 풀 수가 없습니다..


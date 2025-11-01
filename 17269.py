value = {'A': 3, 'F': 3, 'H': 3, 'K': 3, 'M': 3,
'B': 2, 'D': 2, 'N': 2, 'P': 2, 'Q': 2, 'R': 2, 'T': 2, 'X': 2, 'Y': 2,
'C': 1, 'G': 1, 'I': 1, 'J': 1, 'L': 1, 'O': 1, 'S': 1, 'U': 1, 'V': 1, 'W': 1, 'Z': 1,
'E': 4} #알파벳에 대응되는 수 정리


# 입력받을 값
length = input("leght: ").split(' ') #이름이 두 개
name = input("name: ").split(' ')



# 길이 두개로 나누기
length1 = int(length[0])
length2 = int(length[1])

if length1 >= length2 :
    pass
else :
    length2 = int(length[0])
    length1 = int(length[1]) #length1을 더 긴 이름으로 설정


# 이름 두 개로 나누기

name1 = name[0]
name2 = name[1]

if len(name1) >= len(name2) :
    pass
else :
    name2 = name[0]
    name1 = name[1] #name1을 length1과 맞추기 위해


# 이름 대문자 변경
name1 = name1.upper()
name2 = name2.upper()


# 알파벳을 번갈아가면서 입력
result = []

for i in range(length1):
    if i < length1:
        result.append(value[name1[i]]) #길이에 안 맞는 이름을 뒤에 입력하기 위함
    if i < length2:
        result.append(value[name2[i]])



# 숫자 계산
while len(result) > 2 : #퍼센트 숫자 두 개가 남아야 함
    result1 = []
    for i in range(len(result)-1) : #아래 if절을 위해
        if i + 1 < len(result): #숫자를 길이에 맞추기 위함
            if result[i] + result[i+1] < 10:
                result1.append(result[i] + result[i+1])
            else :
                result1.append((result[i]+ result[i+1]) - 10) #10 이상이면 1의 자리 숫자이기에
    result = result1


#결과 도출
print(str(result[0])+str(result[1])+"%")



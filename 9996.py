# 입력 값
time = input("파일의 개수를 입력하십시오: ")
pattern = input("패턴을 입력하십시오: ")

time = int(time) #횟수를 정수로 바꿈
pattern1 = pattern[0] #패턴 첫번째 문자
pattern2 = pattern[-1] #패턴 마지막 문자

result = []

time_1 = time #time_1은 점점 숫자가 줄어들기 때문

#공식
while time_1 > 0 :
    name = input("파일의 이름을 입력하십시오: ")
    
    if name[0] == pattern1 :
        if name[-1] == pattern2 :
            result.append("DA")
        else :
            result.append("NE")
    else :
        result.append("NE")
    time_1 -= 1


for i in range(0,time):
    print(result[i])
# input
import sys
sys.stdin = open("20291_input.txt", "r")

T = int(input())

dic_extension = {}

# process
for i in range(T):
    _, data = input().split('.') # 확장자만 데이터 변수에 저장 

    if data not in dic_extension: # 데이터가 기존에 존재 하지 않는다면
        dic_extension[data] = 1 # 생성
    else: # 존재한다면
        dic_extension[data] += 1 # 증가

dic_extension = sorted(dic_extension.items()) # 정렬

# output
for ext, count in dic_extension:
    print(ext, count)
        


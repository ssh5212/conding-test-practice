import sys

from cv2 import sort
sys.stdin = open("22993_input.txt", "r")

# input
T = int(input())

# process
damage_list = list(map(int, input().split()))
my_damage = damage_list[0] # 첫번째 유저
damage_list.remove(damage_list[0]) # 첫 번째 요소(첫번째 유저) 제거
damage_list = sorted(damage_list) # 리스트 정렬

for i in range(T):
    if i != T-1:
        if my_damage > damage_list[i]: # 내 데미지가 큰 경우
            my_damage += damage_list[i] 
        else: # 내 데미지가 작은 경우
            print("No")
            break
    else:
        print("Yes")


    




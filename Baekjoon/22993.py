import sys

from cv2 import sort
sys.stdin = open("22993_input.txt", "r")

# input
T = int(input())

# process
damage_list = list(map(int, input().split()))
my_damage = damage_list[0]
damage_list.remove(damage_list[0]) 
damage_list = sorted(damage_list)

for i in range(T):
    if i != T-1:
        if my_damage > damage_list[i]:
            my_damage += damage_list[i]
        else:
            print("No")
            break
    else:
        print("Yes")


    




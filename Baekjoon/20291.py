# input
import sys
sys.stdin = open("20291_input.txt", "r")

T = int(input())

dic_extension = {}

# process
for i in range(T):
    _, data = input().split('.')

    if data not in dic_extension:
        dic_extension[data] = 1
    else:
        dic_extension[data] += 1

dic_extension = sorted(dic_extension.items())

# output
for ext, count in dic_extension:
    print(ext, count)
        


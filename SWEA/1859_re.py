# 런타임 에러 발생 (홈페이지의 10개의 테스트케이스 중 9개가 맞음)
import time

from django.test import TestCase
s = time.time()

import sys
sys.stdin = open("1859_input2.txt", "r")

def findMax(t, cost, idx=0):
    return max(cost[t][idx:])

# input
cost = []
N = 0
T = int(input()) # 테스트 케이스 수

idx = 0
output = [0 for i in range(T)]

for test_case in range(1, T + 1):
    N = int(input()) # 예측 가능한 날짜
    cost.append(tuple(map(int, input().split()))) # 가격 리스트

    # process
    maxNum = findMax(test_case-1, cost) # 최대 값을 찾음
    for idx, c in enumerate(cost[test_case-1]):
        if c != maxNum: # 최대 값이 아닌 경우
            output[test_case-1] = output[test_case-1] + maxNum - c
        elif c == maxNum and idx+1 < len(cost[test_case-1]):
            maxNum = findMax(test_case-1, cost, idx+1)

    # output
    print(f"#{test_case} {output[test_case-1]}")

e = time.time()
print("time = ", e-s)
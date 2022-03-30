# 값은 정상적으로 출력되나 페이지에서 런타임 에러
import time
s = time.time()

def findMax(t, cost, idx=0):
    return max(cost[t][idx:])

# source
import sys
sys.stdin = open("1859_input2.txt", "r")

# input
cost = []
N = 0
T = int(input()) # 테스트 케이스 수
for t in range(T):
    N = int(input()) # 예측 가능한 날짜
    cost.append(tuple(map(int, input().split()))) # 가격 리스트
    
# process
idx = 0
output = [0 for i in range(T)]
for t in range(T):
    maxNum = findMax(t, cost)
    for idx, c in enumerate(cost[t]):
        if c != maxNum: # 최대 값이 아닌 경우
            output[t] = output[t] + maxNum - c
        elif c == maxNum and idx+1 < len(cost[t]):
            maxNum = findMax(t, cost, idx+1)

# output
for idx, result in enumerate(output):
    print(f"#{idx+1} {result}")


e = time.time()
print("time = ", e-s)
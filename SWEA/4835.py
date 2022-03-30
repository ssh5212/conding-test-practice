import sys
sys.stdin = open("4835_input.txt", "r")

# input
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    maxAdd = 0
    minAdd = 50*10000
    for i in range(N-M+1):
        print("i : ", i)
        add = 0
        for j in range(M):
            # print("j : ", i)
            add = add + data[i+j]
        if maxAdd < add: 
            maxAdd = add
        if minAdd > add: 
            minAdd = add
    print(maxAdd, minAdd)
    print(f"#{test_case} {maxAdd-minAdd}")
import sys
sys.stdin = open("4828_input.txt", "r")

# input
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    listData = list(map(int, input().split()))

    # process
    maxData = 0
    minData = 1000001
    
    for data in listData:
        if data > maxData:
            maxData = data
        if data < minData:
            minData = data
    
    # output
    print(f"#{test_case} {maxData-minData}")


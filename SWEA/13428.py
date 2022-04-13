import sys
sys.stdin = open("13428_input.txt", "r")

# input
T = int(input())
for test_case in range(1, T + 1):
    N = input() # 숫자 양수
    max = int(N)
    min = int(N)

    for i in range(len(N)):
        test = int(N[i]+N[0:i]+N[i+1:])
        if max < test:
            max = test
        elif int(N[i]) != 0 and min > test:
            min = test

    print(f'#{test_case} {min} {max}')



    
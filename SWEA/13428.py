import sys
sys.stdin = open("13428_input.txt", "r")

# input
T = int(input())
for test_case in range(1, T + 1):
    N = list(map(int, input())) # 숫자 양수
    max_num = max(N)
    min_num = 1000000000

    for i in N:
        if i != 0 and min_num > i:
            min_num = i

    for i, n in enumerate(N):
        if n == max_num:
            continue
        elif n < max_num:
            N[N.index(max_num)], N[N.index(n)] = N[N.index(n)], N[N.index(max_num)]
            break
    
    print(f'#{test_case} {"".join(N)} {max}')



    
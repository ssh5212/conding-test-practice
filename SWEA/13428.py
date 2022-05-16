import sys
sys.stdin = open("13428_input.txt", "r")

# input
T = int(input())
for test_case in range(1, T + 1):
    N = input() # 숫자 양수

    num_list = list(map(str, N))
    while '0' in num_list:
        num_list.remove('0')
    num_list.sort(reverse=True)

    max_swap = 0
    min_swap = 0
    max_idx = 0
    min_idx = 0

    for i in range(len(num_list)):
        if N[i] != num_list[i]:
            max_idx = N.index(num_list[i])
            max_swap = i
            break
    
    for i in range(len(num_list)):
        if N[i] != num_list[len(num_list)-i-1]:
            min_idx = N.index(num_list[len(num_list)-i-1])
            min_swap = i
            break

    max_num = N[:max_swap] + N[max_idx] + N[max_swap+1:max_idx] + N[max_swap] + N[max_idx+1:]

    min_num = N[:min_swap] + N[min_idx] + N[min_swap+1:min_idx] + N[min_swap] + N[min_idx+1:]
    
    if max_swap == max_idx:
        max_num = N
    if min_swap == min_idx:
        min_num = N

    print(f'#{test_case} {min_num} {max_num}')



    
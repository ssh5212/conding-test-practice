import sys
sys.stdin = open("4834_input.txt", "r")

# input
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    a = input()
    # process
    counter = [0 for _ in range(10)]
    max_count = 0
    max_num = 0

    for number in a:
        counter[int(number)-1] = counter[int(number)-1] + 1
        if max_count < counter[int(number)-1]:
            max_count = counter[int(number)-1]
            max_num = number
        elif max_count == counter[int(number)-1] and max_num < number:
            max_num = number

    # output
    print(f"#{test_case} {max_num} {max_count}")
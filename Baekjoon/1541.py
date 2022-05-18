import sys

sys.stdin = open("1541_input.txt", "r")

# input
expression = input()
appear_minus = 0
total = 0
start_number = 0
number_list = []

# process
for i, text in enumerate(expression):
    if text == '-' or text == '+': # 시작 지점부터 부호 앞까지 하나의 정수가 나온 상태
        number_list.append(int(expression[start_number:i]))
        start_number = i
    if i == len(expression) - 1: # 마지막 부호가 나온 시점부터 식의 끝까지 하나의 정수
        number_list.append(int(expression[start_number:]))

for i in number_list:
    if i < 0: # 0보다 작은 경우 무조건 음수로 표현
        total += i
        appear_minus = 1 # 음수가 한 번이라도 나온 경우 변수 값을 변경
    elif i > 0 and appear_minus == 1: # 양수이고 음수가 한 번이라도 나온적이 있는 경우
        total -= i 
    elif i > 0 and appear_minus == 0: # 양수이고 음수가 한 번이라도 나온적이 없는 경우
        total += i

# output
print(total)




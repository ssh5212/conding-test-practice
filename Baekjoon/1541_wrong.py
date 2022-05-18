# 잘못된 코드입니다.
import sys

sys.stdin = open("1541_input.txt", "r")

# input
expression = input()

is_start = 0
start = 0
count = 0

for i, text in enumerate(expression):
    if text == '-':
        if is_start == 1:
            start = i
            is_start == 0
        else:
            if start == 0:
                # case 00009 : eval leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
                count += int(eval(expression[start:i]))
            else:
                count -= int(eval(expression[start:i]))
            is_start == 1
            start = i + 1
    if i == len(expression) - 1:
        if start == 0:
            count += int(eval(expression[start:i]))
        else:
            count -= int(eval(expression[start:i]))

print(count)


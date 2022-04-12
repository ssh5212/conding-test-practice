import sys
sys.stdin = open("1240_input.txt", "r")
password = ['1011000', '1001100', '1100100', '1011110', '1100010', '1000110', '1111010', '1101110', '1110110', '1101000'] # 암호코드 역순으로 작성
# input
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    output = -1
    for n in range(N):
        line = input()
        if int(line) != 0 and output == -1:
            line = str(int(line[::-1])) # 문장을 역순으로 바꿔서 뒤에 있는 0을 제거함

            data=[]
            for i in range(8):
                data.insert(0, password.index(line[7*i : 7*i+7])) # 역순으로 저장된 암호코드

            solve = (data[0] + data[2] + data[4] + data[6])*3 + data[1] + data[3] + data[5] + data[7] 

            if solve % 10 == 0:
                output = sum(data)
            else:
                output = 0

    print(f"#{test_case} {output}")
import sys
sys.stdin = open("1983_input.txt", "r")

# input
T = int(input())
for test_case in range(1, T + 1):
	N, K = int(input().split())
	for i in range(N):
		score = list(map(int, input().split()))
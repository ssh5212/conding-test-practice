import sys
sys.stdin = open("1983_input.txt", "r")

# input
T = int(input())
for test_case in range(1, T + 1):
	N, K = map(int, input().split())
	total_score = [0 for i in range(N)] # 점수를 저장할 변수

	RANK = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

	# process
	k_score = 0 # 찾을 학생의 점수를 저장할 변수
	for i in range(N):
		score = list(map(int, input().split()))
		total_score[i] = score[0]*0.35 + score[1]*0.40 + score[2]*0.20 

	k_score = total_score[K-1]
	total_score.sort(reverse=True) # 내림차순 정렬

	k_rank = total_score.index(k_score)//(N//10) # 인덱스(순위)를 찾음
	
	# output
	print(f'#{test_case} {RANK[k_rank]}')

	

		


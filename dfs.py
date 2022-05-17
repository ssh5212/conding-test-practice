import sys

sys.stdin = open("dfs.txt", "r")

def clear_func(go):
    for i in range(T+1):
        graph[i][go] = 0

def dfs(i):
    global str
    for go in range(T+1):
        print(go)

        if graph[i][go] == 1:  
            str = f'{str}{i} ' 
            print(i, go)
            clear_func(i)
            dfs(go)
            graph[me][go] = 0

T = int(input())
graph = [[0] * (T + 1) for _ in range(T + 1)] 
# print(graph)

str = ''

for i in range(T):
    me, go = map(int, input().split())
    graph[me][go] = 1
print(graph)

for i in range(1, T+1):
    dfs(i)

print(str)



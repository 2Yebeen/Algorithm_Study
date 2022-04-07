"""
[백준/21937] - 작업
https://www.acmicpc.net/problem/21937

민상이가 작업 X를 하기 위해 먼저 해야하는 일의 개수를 출력한다.
--------------------
	input 1
6 4
1 6
2 4
4 6
4 5
5
	output 1
2
	input 2
6 4
1 6
2 4
4 6
4 5
3
	output 2
0
	inbput 3
4 4
1 2
1 3
2 4
3 4
4
	output 3
3
"""
from collections import deque
input = __import__('sys').stdin.readline
MIIS = lambda: map(int, input().split())

N,M = MIIS()
cnt = 0
work = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(M):
	a, b = MIIS()
	work[b].append(a)

start = int(input())
que = deque()
que.append(start)
visited[start] = True

while que:
	x = que.popleft()
	for i in work[x]:
		if not visited[i]:
			visited[i] = True
			cnt += 1
			que.append(i)

print(cnt)
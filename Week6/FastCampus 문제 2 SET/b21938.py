"""
[백준/21938] - 영상처리
https://www.acmicpc.net/problem/21938

화면에 있는 물체의 개수를 출력하라. 만약 물체가 없으면 0을 출력하면 된다.
--------------------
	input 1
3 3
255 255 255 100 100 100 255 255 255
100 100 100 255 255 255 100 100 100
255 255 255 100 100 100 255 255 255
101
	output 1
5
	input 2
2 2
124 150 123 100 100 100
103 103 103 183 5 3
255
	output 2
0
"""
"""
#상, 하, 좌, 우 체크
dr, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
while
=> 처음 255발견하면 cnt + 1 and 발견한 255와 인접해있는 255를 -1으로 변경,
monitor = [[R, G, B],...]
255 255 255 100 100 100 255 255 255
100 100 100 255 255 255 100 100 100
255 255 255 100 100 100 255 255 255

255 100 255
100 255 100
255 100 255

101

255 0 255
0  255  0
255 0 255

124 150 123 100 100 100
103 103 103 183 5 3

135 100
103 65

255

0 0
0 0
"""
from collections import deque
input = __import__('sys').stdin.readline
MIIS = lambda: map(int, input().split())

# 입력
N, M = MIIS()
pixels = []
screen = [[] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
for _ in range(N):
	pixels.append(list(MIIS()))
T = int(input())

# 화면 값 계산
for i in range(N):
	for j in range(0,M*3,3):
		if sum(pixels[i][j:j+3]) < T * 3:
			screen[i].append(0)
		else :
			screen[i].append(255)

# 물체 계산
que = deque()
# 상(-1, 0), 하(1, 0), 좌(0, -1), 우(0, 1)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(r, c):
	que.append((r,c))
	visited[r][c] = True
	
	while que:
		x, y = que.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < N and 0 <= ny < M:
				if not visited[nx][ny] and screen[nx][ny] == 255:
					visited[nx][ny] = True
					que.append((nx,ny))
cnt = 0
for x in range(N):
	for y in range(M):
		if screen[x][y] == 255  and not visited[x][y]:
			bfs(x,y)
			cnt += 1

print(cnt)
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input().strip())))
que = deque()
visited = [[0] * M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

row, col = 0, 0
que.append((row, col))
visited[row][col] = 1

while que:
    row, col = que.popleft()
    if (row, col) == (N - 1, M - 1):
        print(visited[row][col])
    for i in range(4):
        if 0 <= row + dr[i] < N and 0 <= col + dc[i] < M and \
                maze[row + dr[i]][col + dc[i]] == 1 and \
                not visited[row + dr[i]][col + dc[i]]:
            que.append((row + dr[i], col + dc[i]))
            visited[row + dr[i]][col + dc[i]] = visited[row][col] + 1 
import sys
from collections import deque
input = sys.stdin.readline

MAX = 100001
N, K = map(int, input().split())
visited = [0] * MAX
loc = deque()
loc.append(N)

while loc:
    x = loc.popleft()
    if x == K:
        print(visited[x])
        break
    for i in (x - 1, x + 1, 2 * x):
        if 0 <= i < MAX and not visited[i]:
            loc.append(i)
            visited[i] = visited[x] + 1
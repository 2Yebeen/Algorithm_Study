from sys import stdin
from collections import deque
input = stdin.readline

A, B, C = map(int, input().split())
bottle = deque()
bottle.append((0, 0, C))
visited = [[0] * (B + 1) for _ in range((A + 1))]
water = []

while bottle:
    a, b, c = bottle.popleft()
    if visited[a][b]:
        continue
    visited[a][b] = 1
    if a == 0:
        water.append(c)
    bottle.append((0, a+b, c)) if (a + b) < B else bottle.append((a+b-B, B, c))
    bottle.append((0, b, a+c)) if (a + c) < C else bottle.append((a+c-C, b, C))

    bottle.append((b+a, 0, c)) if (b + a) < A else bottle.append((A, b+a-A, c))
    bottle.append((a, 0, b + c)) if (b + c) < C else bottle.append((a, b+c-C, C))

    bottle.append((c+a, b, 0)) if (c + a) < A else bottle.append((A, b, c+a-A))
    bottle.append((a, c+b, 0)) if (c + b) < B else bottle.append((a, B, c+b-B))

water.sort()
print('\n'.join(map(str, water)))
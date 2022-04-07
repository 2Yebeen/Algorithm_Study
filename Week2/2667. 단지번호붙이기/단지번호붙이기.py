import sys
input = sys.stdin.readline

N = int(input())
apt = []
for _ in range(N):
    apt.append(list(map(int, input().strip())))
ans = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
cnt = 0


def dfs(r, c):
    global cnt
    if 0 <= r < N and 0 <= c < N and apt[r][c]:
        cnt += 1
        apt[r][c] = 0
        for i in range(4):
            dfs(r + dr[i], c + dc[i])


for x in range(N):
    for y in range(N):
        if apt[x][y]:
            dfs(x, y)
            ans.append(cnt)
            cnt = 0
ans.sort()
print(len(ans))
print('\n'.join(map(str, ans)))
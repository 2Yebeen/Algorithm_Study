"""
[백준/21922] - 학부 연구생 민상
https://www.acmicpc.net/problem/21922

민상이가 원하는 자리의 개수를 출력한다.
--------------------
    input 1
8 8
0 0 0 0 0 0 0 0
0 0 0 3 0 0 0 4
0 1 0 0 3 0 0 3
0 0 0 0 0 0 1 0
0 1 0 9 0 0 4 0
0 0 0 0 2 0 0 0
0 0 0 0 0 0 0 0
0 0 0 2 0 0 0 0
    output 1
25
    input 2
5 5
3 0 0 0 4
0 9 2 0 0
0 1 9 1 0
0 0 2 9 0
4 0 0 0 3
    output 2
17
    input 3
3 3
3 0 4
0 9 0
4 0 3
    output 3
5
    input 4
3 5
9 0 0 0 4
4 0 0 0 0
0 0 0 0 3
    output 4
15
    input 5
4 4
1 0 1 0
0 2 0 2
3 0 3 0
0 4 0 4
    output 5
0
"""
"""
1. 연구실 내부 구조 정보를 저장
2. 에어컨의 위치를 구한다.
  2-1. 에어컨의 위치 정보가 없으면, 앉을 자리가 없는 것으로 간주 0을 출력한다.
3. 에어컨 위치 정보에 따라 바람의 경로를 구한다.
  3-1. 연구실 범위를 벗어나면 멈춘다.
  3-2. 다른 에어컨을 만나면 멈춘다.
  3-3. 물건 1, 2가 있으면, 멈춘다.
4. 바람이 지나가는 자리를 구한다.
  4-1. 바람이 지나가는 자리의 개수를 구한다.
"""
from collections import deque
input = __import__('sys').stdin.readline
MIIS = lambda: map(int, input().split())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
wind_rotate = {
    1 : [0, 1, 9, 9], 
    2 : [9, 9, 2, 3],
    3 : [3, 2, 1, 0],
    4 : [2, 3, 0, 1]
}
N, M = MIIS()   # 연구실의 세로N(1 <= N <= 2,000), 가로M(1 <= M <= 2,000)
lab = []
air_conditioners = deque()
visited = [[False] * M for _ in range(N)]
for i in range(N):
    # 연구실 내부 구조 정보(1, 2, 3, 4), 에어컨(9(0개 ~ 50개)), 빈 공간(0)
    lab.append(list(MIIS()))
    # 에어컨의 좌표 정보 저장
    for j in range(M):
        if lab[i][j] == 9:
            air_conditioners.append([i, j])
            visited[i][j] = True


def solution():
    ans = 0
    while air_conditioners:
        r, c = air_conditioners.popleft()
        # 바람 경로 구하기
        for i in range(4):
            row = r + dr[i]
            col = c + dc[i]
            # 연구실을 벗어나지 않고, 현재 위치가 에어컨이 아닌 경우
            while 0 <= row < N and 0 <= col < M and lab[row][col] != 9 :
                visited[row][col] = True
                # 현재 위치에 물건이 있는 경우
                if lab[row][col] in (1, 2, 3, 4):
                    # 바람이 이동할 수 있는 경우
                    if wind_rotate[lab[row][col]][i] != 9:
                        i = wind_rotate[lab[row][col]][i]
                    else : break
                row += dr[i]
                col += dc[i]

    for x in range(len(visited)):
        ans += visited[x].count(True)
        # print(visited[x])
    return ans


# print(lab)
# print(visited)
print(solution())
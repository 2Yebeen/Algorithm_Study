"""
[백준/21921] - 블로그
https://www.acmicpc.net/problem/21921

    input 1
5 2
1 4 2 5 1
    output 1
7
1
    input 2
7 5
1 1 1 1 1 5 1
    output 2
9
2
    input 3
5 3
0 0 0 0 0
    output 3
SAD

40
"""
import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

tmp = sum(visitors[:X])
max_v = tmp
cnt = 1
for l in range(X, N):
    tmp -= visitors[l - X]
    tmp += visitors[l]
    if max_v < tmp:
        max_v = tmp
        cnt = 1
    elif max_v == tmp:
        cnt += 1
print("SAD") if max_v == 0 else print(max_v, cnt)
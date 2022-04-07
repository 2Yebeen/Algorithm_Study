"""
[백준/21940] - 가운데에서 만나기

	input 1
4 9
1 2 9
2 3 9
3 1 9
1 4 1
4 1 1
2 4 1
4 2 1
3 4 1
4 3 1
3
1 2 3
	output 1
4
	input 2
3 3
1 2 1
2 3 1
3 1 1
2
1 2
	output 2
1 2 3
"""

input = __import__('sys').stdin.readline
MIIS = lambda: map(int, input().split())

N, M = MIIS()
dis = [] * N + 1
for _ in range(M):
	A, B, T = MIIS()

K = int(input())
C = MIIS()

"""
[백준 / 21939] - 문제 추천 시스템 Version 1
https://www.acmicpc.net/problem/21939

recommend  1 : 문제 리스트에서 가장 어려운 문제의 번호를 출력(만약 가장 어려운 문제가 여러 개라면 문제 번호가 큰 것을 출력)
recommend -1 : 문제 리스트에서 가장 쉬운 문제의 번호를 출력(가장 쉬운 문제가 여러개라면 문제 번호가 작은 것을 출력)

add P(문제번호) L(난이도) : 추천 문제 리스트에 난이도가 L 인 문제 번호 P를 추가

solved P(문제번호) : 문제번호 P를 제거
--------------------
	input 1
5
1000 1
1001 2
19998 78
2667 37
2042 55
8
add 1402 59
recommend 1
solved 1000
solved 19998
recommend 1
recommend -1
solved 1001
recommend -1
	output 1
19998
1402
1001
2667
"""
import heapq
input = __import__('sys').stdin.readline


def recommend(x):
	if x == 1:
		print((max_h[0][1] * -1))
	else:
		print(min_h[0][1])

        
def add(p, l):
	heapq.heappush(min_h, (l, p))
	heapq.heappush(max_h, (-l, -p))

    
def solved(p):
	if p == (max_h[0][1] * -1):
		heapq.heappop(max_h)
	elif p == min_h[0][1]:
		heapq.heappop(min_h)

    
N = int(input())
min_h = []
max_h = []

for i in range(N):
	P, L = map(int, input().split())
	heapq.heappush(min_h, (L, P))  # 우선순위, 값(최소)
	heapq.heappush(max_h, (-L, -P)) # 우선순위, 값(최대)

M = int(input())
for j in range(M):
	tmp = list(map(str, input().split()))
	if tmp[0] == 'recommend':
		recommend(int(tmp[1]))
	if tmp[0] == 'add':
		add(int(tmp[1]), int(tmp[2]))
	if tmp[0] == 'solved':
		solved(int(tmp[1]))
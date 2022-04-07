"""
	input 1
abcxyzxabc
2
abc 10
xyz 5
	output 1
26
	input 2
abcxyzxabc
2
abc 2
xyz 1
	output 2
10
"""
import heapq
input = __import__('sys').stdin.readline


def del_chr(str, cnt):
	for i in range(len(str)-1):
		if str[i] != "_":
			cnt += 1
			str = str.replace(str[i], "_", 1)
	return cnt


s = input()
M = int(input())
heap_A = []
heap_B = []
score = 0
for _ in range(M):
	A, X = map(str, input().split())
	la = len(A)
	ix = int(X)
	heapq.heappush(heap_A, (-(ix/la), A))
	heapq.heappush(heap_B, (-(ix/la), int(X)))
while heap_A:
	_, a = heapq.heappop(heap_A)
	_, x = heapq.heappop(heap_B)
	if x > len(a):
		while a in s:
			s = s.replace(a, "_", 1)
			score += x

score += del_chr(s, 0)
print(score)

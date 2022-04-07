"""
recommend G x
  if x ==  1 : 알고리즘 분류가 G인 문제 중 가장 어려운 문제 번호 출력(문제 번호 큰 것 우선)
elif x == -1 : 알고리즘 분류가 G인 문제 중 가장 쉬운 문제 번호 출력(문제 번호 작은 것 우선)

recommend2 x
  if x ==  1 : 알고리즘 분류 상관없이 가장 어려운 문제 번호 출력(문제 번호 큰 것 우선)
elif x == -1 : 알고리즘 분류 상관없이 가장 쉬운 문제 번호 출력(문제 번호 작은 것 우선)

recommend3 x L
  if x ==  1 : 알고리즘 분류 상관없이 난이도가 L보다 크거나 같은 문제 중 가장 쉬운 문제 번호 출력(문제 번호 작은 것 우선)
			   조건에 만족하는 문제 번호가 없는 경우, -1 출력
elif x == -1 : 알고리즘 분류 상관없이 난이도가 L보다 작은 문제 중 가장 어려운 문제 번호 출력(문제 번호가 큰 것 우선)
			   조건에 만족하는 문제 번호가 없을 경우, -1 출력

add P L G 
난이도가 L이고 알고리즘 분류가 G인 문제 번호 P를 추가한다.

solved P
문제 번호 P를 제거한다.

1. 같은 문제번호가 주어질 수 있다.
2-1. 알고리즘 분류를 확인하여 문제 번호를 출력하거나
2-2. 난이도로 나눠 문제 번호를 출력하거나
2-3. 특정 난이도 조건에 맞춰 문제 번호를 출력해야 한다.
3. recommend3의 경우, 난이도 L이 없는 경우가 있을 수 있으므로 범위에 맞게 확인해야 한다.

"""

input = __import__('sys').stdin.readline


def recommend(g, x):
	# 알고리즘 분류 확인 후
	if x == 1:
		# 난이도가 가장 높은 문제 번호 출력
		pass
	else:
		# 난이도가 가장 낮은 문제 번호 출력
		pass
	pass


def recommend2(x):
	# 난이도로 정렬된(오름차순) 리스트 중
	if x == 1:
		# 가장 뒤에 있는 문제 번호 출력
		pass
	else:
		# 가장 앞에 있는 문제 번호 출력
		pass
	pass


def recommend3(x, l):
	r = l
	# 레범 범위 체크
	if r >= l and x == 1:
		# 가장 쉬운 문제 번호 출력 
		pass
	elif r < l:
		# 가장 어려운 문제 번호 출력
		pass
	print(-1)


def add(p, l, g):
	# 난이도가 l이고 알고리즘 분류가 g인 문제번호 p추가
	pass


def solved(p):
	# 문제번호 p제거
	pass


MIIS = lambda: map(int, input().split())
MSIS = lambda: map(str, input().split())
N = int(input())

for _ in range(N):
	P, L, G = MIIS()

M = int(input())
for _ in range(M):
	line = input().split()
	if line[0] == 'recommend':
		pass
	elif line[0] == 'recommend1':
		pass
	elif line[0] == 'recommend3':
		pass
	elif line[0] == 'add':
		pass
	elif line[0] == 'solved':
		pass
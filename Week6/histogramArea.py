def left(x, end, arr):
	cnt = 0
	for i in range(end-1, -1, -1):
		if x > arr[i]:
			break
		cnt += 1
	return cnt * x


def right(x, start, arr):
	cnt = 0
	for i in range(start, len(arr)):
		if x > arr[i]:
			break
		cnt += 1
	return cnt * x


def sol(arr):
	area = 0
	l = len(arr)
	for i in range(l):
		x = arr[i]
		tmp = left(x, i, arr) + right(x, i, arr)
		if area <= tmp:
			area = tmp
	return area



A = [6, 3, 1, 4, 12, 4]
B = [5, 6, 7, 4, 1]
print(sol(A))
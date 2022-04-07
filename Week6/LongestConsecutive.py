
def LongestConsecutive(arr):
	max_cnt = 0
	l = len(arr)
	arr.sort()

	for i in range(l-1):
		tmp = []
		j = i
		x = 0
		while j < len(arr) and arr[i] + x == arr[j]:
			tmp.append(arr[j])
			x += 1
			j += 1
		if len(tmp) >= max_cnt:
			max_cnt = len(tmp)
	return max_cnt


A = [6, 7, 3, 1, 100, 102, 6, 12]
B = [5, 6, 1, 2, 8, 9, 7]

print(LongestConsecutive(A))
print(LongestConsecutive(B))
# print(LongestConsecutive(input()))
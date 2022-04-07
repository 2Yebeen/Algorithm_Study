def CityTraffic(arr):
	lst = [[] for _ in range(len(arr)+1)]
	for x in arr:
		i, val = x.split(":")
		i = int(i)
		val = val.replace('[', '')
		val = val.replace(']', '')
		val = list(map(int, val[:].split(',')))
	for i in lst:
		pass
	print(lst)

A = ["1:[5]", "2:[5]", "3:[5]", "4:[5]", "5:[1, 2, 3, 4]"]
B = ["1:[5]", "2:[5, 18]", ]
print(CityTraffic(A))
# print(CityTraffic(input()))
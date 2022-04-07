import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

num_sum = 0
end = 0
length = 100000001

for start in range(N):
    while num_sum < S and end < N:
        num_sum += numbers[end]
        end += 1
    if num_sum >= S:
        length = min(length, end - start)
    num_sum -= numbers[start]

print(length) if 100000001 > length else print(0)
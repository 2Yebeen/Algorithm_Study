import sys
input = sys.stdin.readline


def num_sum(target, arr):
    s, e = 0, len(arr) - 1
    while s < e:
        sum_n = arr[s] + arr[e]
        if sum_n == target:
            return 1
        if sum_n < target:
            s += 1
        else:
            e -= 1
    return 0


N = int(input())
numbers = sorted(list(map(int, input().split())))
val = 0

for i in range(N):
    val += num_sum(numbers[i], numbers[:i] + numbers[i+1:])

print(val)
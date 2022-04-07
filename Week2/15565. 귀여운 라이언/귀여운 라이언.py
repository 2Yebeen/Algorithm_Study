import sys
input = sys.stdin.readline

N, K = map(int, input().split())
doll = list(map(int, input().split()))

lion_sum = 0
end = 0
length = N+1

for start in range(N):
    while lion_sum < K and end < N:
        if doll[end] == 1: lion_sum += 1
        end += 1
    if lion_sum >= K:
        length = min(length, end - start)
    if doll[start] == 1: lion_sum -= 1

print(length) if length < N else print(-1)
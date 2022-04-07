import sys
input = sys.stdin.readline

N, C = list(map(int, input().split()))
house = sorted([int(input()) for _ in range(N)])

start, end = 1, house[-1] - house[0]
ans = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    wifi = house[0]

    for i in range(1, N):
        if wifi + mid <= house[i]:
            cnt += 1
            wifi = house[i]

    if cnt >= C:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

sys.stdout.write(str(ans))

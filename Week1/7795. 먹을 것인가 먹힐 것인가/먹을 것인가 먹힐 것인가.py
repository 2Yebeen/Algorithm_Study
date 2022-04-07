import sys


def feed(a, arr):
    s, e = 0, len(arr) - 1
    cnt = 0
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] < a:
            s = mid + 1
            cnt = s
        else:
            e = mid - 1
    return cnt


T = int(sys.stdin.readline())
for _ in range(T):
    ans = 0
    N, M = list(map(int, sys.stdin.readline().split()))
    A = sorted(list(map(int, sys.stdin.readline().split())))
    B = sorted(list(map(int, sys.stdin.readline().split())))
    for target in A:
        ans += feed(target, B)
    print(ans)
    
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

flag = [0] * 100001
ans = 0
end = 0

for start in range(N):
    while end < N:
        if flag[arr[end]]:
            break
        flag[arr[end]] = 1
        end += 1
    ans += end - start
    flag[arr[start]] = 0
    
print(ans)
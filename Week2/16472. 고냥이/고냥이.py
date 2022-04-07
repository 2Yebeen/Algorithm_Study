import sys
input = sys.stdin.readline

N = int(input())
arr = input().rstrip()

flag = [0] * 26
ans, cnt, end = 0, 0, 0
size = len(arr)
a = ord('a')

for start in range(size):
    while end < size:
        if cnt == N and not flag[ord(arr[end]) - a]:
            break
        if not flag[ord(arr[end]) - a]:
            cnt += 1
        flag[ord(arr[end]) - a] += 1
        end += 1
    ans = max(ans, end - start)
    flag[ord(arr[start]) - a] -= 1
    if not flag[ord(arr[start]) - a]:
        cnt -= 1

print(ans)
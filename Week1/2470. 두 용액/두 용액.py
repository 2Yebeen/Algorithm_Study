import sys

N = int(sys.stdin.readline())
solution = list(map(int, sys.stdin.readline().split()))
solution.sort()
min_s = 2000000000
ans = []

s = 0
e = N - 1
while s < e:
    sum_s = solution[s] + solution[e]
    if min_s > abs(sum_s):
        min_s = abs(sum_s)
        ans = [solution[s], solution[e]]

    if sum_s < 0:
        s += 1
    else:
        e -= 1

sys.stdout.write(str(ans[0]) + " " + str(ans[1]) + "\n")
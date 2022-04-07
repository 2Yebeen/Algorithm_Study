import sys

N = int(sys.stdin.readline())
li = []
tot = 0
for _ in range(N):
    point, color = map(int, sys.stdin.readline().split())
    li.append([point, color])
li.sort(key=lambda x: (x[1], x[0]))
for idx in range(len(li)):
    if idx == 0:
        if li[1][1] == li[0][1]:
            tot += abs(li[1][0] - li[0][0])
    elif idx != (len(li) - 1):
        if li[idx - 1][1] == li[idx][1] and li[idx + 1][1] == li[idx][1]:
            tot += min(abs(li[idx][0] - li[idx + 1][0]), abs(li[idx][0] - li[idx - 1][0]))
        elif li[idx - 1][1] != li[idx][1] and li[idx + 1][1] == li[idx][1]:
            tot += abs(li[idx + 1][0] - li[idx][0])
        elif li[idx - 1][1] == li[idx][1] and li[idx + 1][1] != li[idx][1]:
            tot += abs(li[idx - 1][0] - li[idx][0])
    else:
        if li[idx - 1][1] == li[idx][1]:
            tot += abs(li[idx - 1][0] - li[idx][0])

sys.stdout.write(str(tot) + "\n")
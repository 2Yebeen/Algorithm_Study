import time, sys
n = int(input().strip())
score = [sys.stdin.readline().strip().split() for _ in range(n)]
score.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for name in score:
    sys.stdout.write(str(name[0]) + '\n')
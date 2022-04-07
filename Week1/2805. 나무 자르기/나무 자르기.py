import sys
input = sys.stdin.readline
from collections import Counter

N, M = map(int, input().split())
trees = Counter(map(int, input().split()))

start, end = 0, max(trees)
while start <= end:
    cut = ((start + end) // 2)
    height = 0

    height = sum((i - cut) * j for i, j in trees.items() if i > cut)
    if height >= M:
        start = cut + 1
    else:
        end = cut - 1
sys.stdout.write(str(end))

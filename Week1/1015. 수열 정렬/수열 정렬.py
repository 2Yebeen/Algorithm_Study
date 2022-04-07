n = int(input())
a = list(map(int, input().strip().split()))
p = sorted(a)
for i in range(n):
    idx = p.index(a[i])
    print(idx, end=" ")
    p[idx] = -1
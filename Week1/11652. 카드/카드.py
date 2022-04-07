import sys
n = int(sys.stdin.readline())
card = {}
for _ in range(n):
    num = int(sys.stdin.readline())
    if num in card:
        card[num] += 1
    else:
        card[num] = 1
ans = sorted(card.items(), key=lambda x: (-x[1], x[0]))
sys.stdout.write(str(ans[0][0]))
"""
[백준/21919] - 소수 최소 공배수
첫째 줄에 소수들의 최소공배수를 출력한다.
만약 소수가 없는 경우는 -1을 출력한다.

    input 1
5
2 3 5 6 8
    output 1
30
    input 2
4
4 16 64 256
    output 2
-1

1. 소수 찾기
2. 최소 공배수 찾기
"""
import sys
input = sys.stdin.readline

def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0 : return False
        i += 1
    return True


N = int(input())
A = list(set(map(int, input().split())))
prime = []
ans = 1
for prime in A:
    if is_prime(prime):
        ans *= prime
print(-1) if ans == 1 else print(ans)

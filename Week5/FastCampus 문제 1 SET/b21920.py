"""
[백준/21920] - 서로소 평균

첫째 줄에 수열 A에서 X와 서로소인 수들의 평균을 출력한다.
절대/상대 오차는 10-6까지 허용한다.

    input
5
4 2 8 5 7
4
    output
6
----------
"""
import sys
from math import gcd
input = sys.stdin.readline

# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a


int(input())
A = list(map(int, input().split()))
X = int(input())
numbers = [num for num in A if gcd(X, num) == 1]
print(f"{sum(numbers)/len(numbers):.6f}")

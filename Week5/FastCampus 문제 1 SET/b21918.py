"""
[FastCampus 문제 1 SET]
https://www.acmicpc.net/workbook/view/7942

전구(21918)
https://www.acmicpc.net/problem/21918

    input 1
8 3
0 0 0 0 0 0 0 0
1 2 1
1 4 1
2 2 4
    output 1
0 0 1 0 0 0 0 0
    input 2
8 6
0 0 0 0 0 0 0 0
1 2 1
1 4 1
2 2 4
2 1 7
3 5 8
4 4 6
    output 2
1 1 0 1 1 1 0 0
20M
"""
import sys
input = sys.stdin.readline

def states_bulb(com, a, b):
    if com == 1 :
        bulbs[a] = b
    elif com == 2:
        for i in range(a, b):
            bulbs[i] = 0 if bulbs[i] == 1 else 1
    elif com == 3:
        bulbs[a:b] = [0] * (b - a)
    elif com == 4:
        bulbs[a:b] = [1] * (b - a)


N, M = map(int, input().split())
bulbs = list(map(int, input().split()))
for _ in range(M):
    # com, l, r / com, i, x
    # 1번 명령 : i번째 전구를 x로 변경
    # 2번 명령 : l 부터 r 까지 전구 상태 변경
    # 3번 명령 : l 부터 r 까지 전구를 끈다.
    # 4번 명령 : l 부터 r 까지 전구를 켠다.
    command, l, r = map(int, input().split())
    states_bulb(command, l-1, r)

print(*bulbs)
"""
[백준/21924] - 도시 건설
https://www.acmicpc.net/problem/21924

예산을 얼마나 절약 할 수 있는지 출력한다. 
만약 모든 건물이 연결되어 있지 않는다면 -1을 출력한다.
--------------------
    input 1
7 9
1 2 15
2 3 7
1 3 3
1 4 8
3 5 6
4 5 4
4 6 12
5 7 1
6 7 6
    output 1
35
    input 2
8 10
1 2 4
2 3 9
2 4 9
3 4 4
3 5 1
4 6 14
6 7 5
5 7 3
7 8 7
6 8 3
    output 2
30
    inpput 3
5 4
1 2 1
2 3 1
3 1 1
4 5 5
    output 3
-1
"""
# 최소 신장 트리 문제 : 전체 요소들을 연결할 때 사용(Kruskal, Prim)
"""
[ kruskal 알고리즘 이용 ]

1. 간선 정렬
2. 간선을 잇는 두 정점을 찾는다.
3. 다르다면 하나의 root를 바꿔 연결시켜준다.
** 간선을 정렬해야 하기때문에 간선이 많으면 Prim알고리즘을 이용하는 것이 좋다.
** 비슷한 알고리즘으로 다익스트라 알고리즘이 있다.
   다익스트라 알고리즘의 경우, 한 정점에서 다른 정점으로 가는 가장 짧은 방법을 구할 때 사용한다.
"""
input = __import__('sys').stdin.readline
MIIS = lambda: map(int, input().split())

# 건물의 개수 N(3 <= N <= 10^5), 도로의 개수 M(2 <= M <= min(N(N-1)/2, 5×10^5))
N, M = MIIS()
parent = [i for i in range(N + 1)] # 건물 번호(1 <= a, b <=N, a != b), 각 정점의 보모 원소 자기 자신으로 설정
edges = [] # 간선 정보 저장
for _ in range(M):
    # a번노드에서 b번 노드로 가는 비용c
    edges.append(list(MIIS()))


# 간선들이 이은 두 정점을 찾는다.
def find(node):
    # path compressino 기법
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

# 두 집합 연결
def union(node_a, node_b):
    root1 = find(node_a)
    root2 = find(node_b)
    # root값이 큰 값을 작은 root값으로 만들어 연결해준다.
    if root1 > root2:
        root1, root2 = root2, root1
    parent[root2] = root1



def kruskal(graph):
    ans = 0
    # 가중치(건설비용) 기준으로 정렬한다.
    graph.sort(key=lambda x: x[2])

    for a, b, c in graph:
        ans += c
        # 사이클 X 
        if find(a) != find(b):
            union(a, b)
            ans -= c
    for i in range(2, N + 1):
        if find(i) != 1:
            return -1
    return ans


print(kruskal(edges))
    
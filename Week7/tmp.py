"""
디딤돌의 숫자는 한 번 밟을 때 마다 1씩 줄어든다
숫자가 0이되면 더 이상 밟을 수 없다 -> 다음 디딤돌로 한번에 여러 칸 건널 수 있다.
밟을 수 있는 디딤돌은 가장 가까운 디딤돌로 건너야 한다.
디딤돌의 최대 칸수 K
"""
"""

"""
def solution(stones, k):
	answer = 0
	while True:
		cnt = 0
		for i in range(len(stones)):
			print(stones, answer)
			if stones[i] == 0:
				cnt += 1
				if cnt == k:
					return(answer)
			else:
				cnt = 0
				stones[i] -= 1
		answer += 1
	return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
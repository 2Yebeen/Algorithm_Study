from itertools import combinations
input = __import__('sys').stdin.readline
MIIS = lambda: map(int, input().split())

N = int(input())
numbers = list(MIIS())
P, Q = MIIS()
ans = 0


def dfs(cu_val,cnt,lst_num):
	global ans
	if cnt == 0:
		ans = max(ans,cu_val*sum(lst_num))
		return cu_val * sum(lst_num)
	else:
		idx_list = range(len(lst_num))
		for pick_cnt in range(1,len(lst_num)-cnt+1):
			for comb in combinations(idx_list,pick_cnt):
				copy_lst_num = lst_num[:]
				comb = list(reversed(comb))
				temp_sum = 0
				for idx in comb:
					temp_sum += copy_lst_num.pop(idx)                
				dfs(cu_val*temp_sum,cnt-1,copy_lst_num)

# 곱하기를 최대로 먼저 
dfs(1, Q, numbers)
print(ans)
from itertools import permutations
def dfs(idx,cnt,position,num_list):
	global result
	if (cnt+N-1-idx)<Q:
		return
	if idx == N-1:
		position.append(idx)
		mul_val = 1
		sum_val = 0
		cu_idx = 0
		for mul_idx in position:
			while (cu_idx<=mul_idx):
				sum_val += num_list[cu_idx]
				cu_idx += 1
			mul_val *= sum_val
			sum_val = 0
		result = max(result,mul_val)
		position.pop()
		return
	dfs(idx+1,cnt,position,num_list)
	position.append(idx)
	if cnt+1<=Q:
		dfs(idx+1,cnt+1,position,num_list)
	position.pop()
N = int(input())
arr = list(map(int,input().split()))
result = 0
arr.sort()
 
P,Q = map(int,input().split())
for perm in permutations(arr):
    dfs(0,0,[],perm)
print(result)
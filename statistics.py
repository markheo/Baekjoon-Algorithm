# statistics (Baekjoon 2108)
import sys
N = int(input())
#N = int(sys.stdin.readline())

num_lst = []
num_dict = {}
for _ in range(N):
    num = int(input())
    #num = int(sys.stdin.readline())
    num_lst.append(num)
    try:
        num_dict[num] += 1
    except KeyError:
        num_dict[num] = 1

cnt = 0
for k,v in num_dict.items():
    cnt += k * v
# mean
print(round(cnt / sum(num_dict.values())))

# median
num_lst.sort()
print(num_lst[N//2])

# mode
klst = list(num_dict.keys())
vlst = list(num_dict.values())
ans = []
for k in klst:
    if num_dict[k] == max(vlst):
        ans.append(k)
if len(ans) == 1:
    print(max(num_dict, key=num_dict.get))
else:
    ans = sorted(ans)
    print(ans[1])

# range
print(max(klst) - min(klst))
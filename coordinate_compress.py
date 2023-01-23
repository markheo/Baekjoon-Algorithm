# coordinate compression (Baekjoon 18870) - time over
import sys
N = int(input())
#N = int(sys.stdin.readline())
lst1 = list(map(int, input().split()))
#lst1 = list(map(int, sys.stdin.readline().split()))
lst2 = list(set(lst1.copy()))
ans = [0 for _ in range(len(lst1))]
for i in range(len(lst1)):
    for j in range(len(lst2)):
        if lst1[i] > lst2[j]:
            ans[i] += 1
print(*ans, sep=' ')



# coordinate compression (Baekjoon 18870) - time over because Time Complexity of .index O(N)
import sys
N = int(input())
#N = int(sys.stdin.readline())
lst1 = list(map(int, input().split()))
#lst1 = list(map(int, sys.stdin.readline().split()))
lst2 = sorted(list(set(lst1)))
ans = []
for i in range(len(lst1)):
    num = lst2.index(lst1[i])
    ans.append(num)
print(*ans, sep=' ')



# coordinate compression (Baekjoon 18870) - 150180KB / 1880ms
import sys
N = int(input())
#N = int(sys.stdin.readline())
lst1 = list(map(int, input().split()))
#lst1 = list(map(int, sys.stdin.readline().split()))
lst2 = sorted(list(set(lst1)))
ans_dct = {lst2[i]:i for i in range(len(lst2))} # sorted array index를 dict화
for num in lst1:
    print(ans_dct[num], end=' ')
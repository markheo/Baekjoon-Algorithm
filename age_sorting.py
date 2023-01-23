# age order sorting (Baekjoon 10814) - 60844KB / 272ms
import sys
N = int(input())
#N = int(sys.stdin.readline())
ans = []
for _ in range(N):
    info = input().split()
    #info = sys.stdin.readline().split()
    ans.append(info)
ans.sort(key=lambda x: int(x[0]))
for i in range(N):
    a, b = ans[i][0], ans[i][1]
    print(a, b)
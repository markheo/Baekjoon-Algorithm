# word-sorting (Baekjoon 1181) - 35272KB / 72ms
import sys
N = int(input())
#N = int(sys.stdin.readline())
ans = []
for _ in range(N):
    word = input()
    #word = sys.stdin.readline().strip()
    ans.append(word)
ans = list(set(ans))
ans.sort()
ans.sort(key=lambda x: len(x))
print(*ans, sep='\n')
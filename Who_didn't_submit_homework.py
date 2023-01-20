# Who didn't submit homework..? (Baekjoon 5597)
import sys

scores = set()

for _ in range(28):
    score = int(input())
    # score = int(sys.stdin.readline())
    scores.add(score)

full_lst = set([x for x in range(1, 31)])
ans = sorted(list(full_lst - scores))
print(ans[0])
print(ans[1])
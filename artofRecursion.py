# art of recursion (Baekjoon 25501)
def recursion(s, l, r, cnt):
    if l >= r:
        return 1, cnt
    elif s[l] != s[r]:
        return 0, cnt
    else:
        return recursion(s, l+1, r-1, cnt+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

import sys
N = int(input())
#N = int(sys.stdin.readline())
ans = []

for _ in range(N):
    txt = input()
    #txt = sys.stdin.readline().strip()
    ans.append(isPalindrome(txt))
print(ans)
for i in range(N):
    print(*ans[i], sep=' ')
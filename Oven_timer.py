# Oven Timer (Baekjoon 2525)
h, m = map(int, input().split())
l = int(input())

if l >= 60:
    h += l // 60
    m += l % 60
else:
    m += l

if m >= 60:
    m -= 60
    h += 1

if h >= 24:
    h -= 24

print(h, m)
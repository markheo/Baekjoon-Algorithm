# coordinate-sorting (Baekjoon 11650) - selection sort -- Timeout!!
import sys
N = int(input())
#N = int(sys.stdin.readline())
x_lst, y_lst = [], []
ans_lst = []

for _ in range(N):
    x, y = map(int, input().split())
    #x, y = map(int, sys.stdin.readline().split())
    x_lst.append(x)
    y_lst.append(y)
    ans_lst.append((x, y))

for i in range(N):
    smallest = i
    for j in range(i+1, N):
        if x_lst[smallest] > x_lst[j]:
            x_lst[j], x_lst[smallest] = x_lst[smallest], x_lst[j]
            y_lst[j], y_lst[smallest] = y_lst[smallest], y_lst[j]
            ans_lst[j], ans_lst[smallest] = ans_lst[smallest], ans_lst[j]
        elif x_lst[smallest] == x_lst[j]:
            if y_lst[smallest] > y_lst[j]:
                x_lst[j], x_lst[smallest] = x_lst[smallest], x_lst[j]
                y_lst[j], y_lst[smallest] = y_lst[smallest], y_lst[j]
                ans_lst[j], ans_lst[smallest] = ans_lst[smallest], ans_lst[j]

for i in range(N):
    a, b = ans_lst[i][0], ans_lst[i][1]
    print(a, b)




# coordinate-sorting (Baekjoon 11650) - selection sort -- Timeout!!
import sys
N = int(input())
#N = int(sys.stdin.readline())
ans_lst = []

for _ in range(N):
    x, y = map(int, input().split())
    #x, y = map(int, sys.stdin.readline().split())
    ans_lst.append([x, y, (x, y)])

for i in range(N):
    smallest = i
    for j in range(i+1, N):
        if ans_lst[smallest][0] > ans_lst[j][0]:
            ans_lst[j], ans_lst[smallest] = ans_lst[smallest], ans_lst[j]
        elif ans_lst[smallest][0] == ans_lst[j][0]:
            if ans_lst[smallest][1] > ans_lst[j][1]:
                ans_lst[j], ans_lst[smallest] = ans_lst[smallest], ans_lst[j]

for i in range(N):
    a, b = ans_lst[i][2][0], ans_lst[i][2][1]
    print(a, b)




# coordinate-sorting (Baekjoon 11650) - internal method + lambda -- 53512KB, 372ms
import sys
N = int(input())
#N = int(sys.stdin.readline())
ans_lst = []

for _ in range(N):
    x, y = map(int, input().split())
    #x, y = map(int, sys.stdin.readline().split())
    ans_lst.append([x, y])

ans_lst.sort(key = lambda x: (x[0], x[1]))

for i in range(N):
    a, b = ans_lst[i][0], ans_lst[i][1]
    print(a, b)
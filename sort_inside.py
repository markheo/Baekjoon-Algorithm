# sort-inside (Baekjoon 1427)
import sys
N = int(input())
#N = int(sys.stdin.readline())

N = str(N)
num_lst = list(map(int, list(N)))
num_lst.sort(reverse=True)
num_lst = list(map(str, num_lst))
reverse_N = "".join(num_lst)
print(reverse_N)
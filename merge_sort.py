# merge sort (Baekjoon 24060)
import sys
ans = []

def mergeSort(L: list) -> None:
    mergeSortHelp(L, 0, len(L) - 1)


def mergeSortHelp(L: list, first: int, last: int) -> None:
    if first == last:
        return

    else:
        mid = first + (last - first) // 2
        mergeSortHelp(L, first, mid)
        mergeSortHelp(L, mid + 1, last)
        merge(L, first, mid, last)


def merge(L: list, first: int, mid: int, last: int) -> None:
    i = j = 0
    k = first
    sub1 = L[first:mid + 1]
    sub2 = L[mid + 1:last + 1]
    while i < len(sub1) and j < len(sub2):
        if sub1[i] <= sub2[j]:
            L[k] = sub1[i]
            ans.append(L[k])
            i += 1
        else:
            L[k] = sub2[j]
            ans.append(L[k])
            j += 1
        k += 1

    if i < len(sub1):
        L[k:last + 1] = sub1[i:]
        ans.extend(L[k:last + 1])
    elif j < len(sub2):
        L[k:last + 1] = sub2[j:]
        ans.extend(L[k:last + 1])


N, K = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))
mergeSort(L)
try:
    print(ans[K - 1])
except:
    print(-1)
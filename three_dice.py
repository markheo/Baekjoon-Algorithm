# Three dice (Baekjoon 2480)
input_lst = list(map(int, input().split()))
num_dict = {}
for i in input_lst:
    if i in num_dict:
        num_dict[i] += 1
    else:
        num_dict[i] = 1

if max(num_dict.values()) == 3:
    print(10000 + 1000 * max(num_dict, key=num_dict.get))
elif max(num_dict.values()) == 2:
    print(1000 + 100 * max(num_dict, key=num_dict.get))
else:
    print(100 * max(num_dict))
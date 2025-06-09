from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

indexes = list(combinations(range(n), k))
count_a = sum(1 for i in indexes if 'a' in [letters[x] for x in i])

print("{:.4f}".format(count_a / len(indexes)))

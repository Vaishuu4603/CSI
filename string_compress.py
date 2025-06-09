from itertools import groupby

s = input("Enter a string: ")

compressed = [(len(list(g)), int(k)) for k, g in groupby(s)]
print(*compressed)

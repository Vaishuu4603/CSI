import re

T = int(input())
for i in range(T):
    pattern = input()
    try:
        re.compile(pattern)
        print(True)
    except re.error:
        print(False)

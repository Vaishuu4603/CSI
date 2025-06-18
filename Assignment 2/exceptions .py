
T = int(input())

for i in range(T):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError:
        print("Error Code: invalid literal for int() with base 10")

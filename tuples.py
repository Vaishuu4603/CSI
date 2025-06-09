n = int(input("Enter size of tuple: "))
integer_list = tuple(map(int, input("Enter elements: ").split()))
print(hash(integer_list))

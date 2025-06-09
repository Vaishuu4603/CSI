n = int(input("Enter number of students: "))
student_marks = {}

for _ in range(n):
    name, *scores = input().split()
    student_marks[name] = list(map(float, scores))

query_name = input("Enter student name: ")
avg = sum(student_marks[query_name]) / len(student_marks[query_name])
print("{:.2f}".format(avg))

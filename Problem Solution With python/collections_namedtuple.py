from collections import namedtuple

n = int(input())

total_marks = 0
for _ in range(n):
    students = namedtuple('student', input().split())
    MARKS, CLASS, NAME, ID = input().split()
    student = students(MARKS, CLASS, NAME, ID)
    total_marks += int(student.MARKS)
print('{:.2f}'.format(total_marks / n))
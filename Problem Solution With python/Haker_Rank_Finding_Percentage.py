
from logging import PercentStyle
from traceback import format_tb


n=int(input())

student_makrs={}

for _ in range(n):
    name, *line=input().split()
    scores = list(map(float,line))
    student_makrs[name]=scores
qurey_name=input()

marks=list(student_makrs[qurey_name])
Percentage=sum(marks)/len(scores)

print("%.2f"%Percentage)

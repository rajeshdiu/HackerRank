from itertools import permutations
import itertools

sk=input().split()

s=sk[0]
k=int(sk[1])

output=sorted(list(itertools.permutations(s,k)))

for i in output:
    for j in i:
        print(j,end="")
    print()
    
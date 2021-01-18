# Enter your code here. Read input from STDIN. Print output to STDOUT
x=input().split()
string=x[0]
k=int(x[1])
from itertools import permutations
l=list(permutations(string,k))
ll=[]
for i in l:
    ll.append("".join(i))
for i in sorted(ll):
    print(i)

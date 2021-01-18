# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s=input().split()
s[0]=sorted(s[0])
k=list(combinations_with_replacement(s[0],int(s[1])))
for i in range(len(k)):
    print(''.join(k[i]))

# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
set_a=set(input().split())
b=int(input())
set_b=set(input().split())
out=len(set_a.difference(set_b))
print(out)

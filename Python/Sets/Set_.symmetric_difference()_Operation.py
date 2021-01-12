# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
set_a=set(input().split())
m=int(input())
set_b=set(input().split())
out=len(set_a.symmetric_difference(set_b))
print(out)

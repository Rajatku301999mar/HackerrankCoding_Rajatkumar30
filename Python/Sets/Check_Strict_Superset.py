# Enter your code here. Read input from STDIN. Print output to STDOUT
'''set_a=set(input().split())
set_0=set(input().split())
set_1=set(input().split())
set_2=set(input().split())
if set_0 in set_a:
    if set_1 in set_a:
        if set_2 in set_a:
            print("True")
print("False")'''

a=set(map(int, input().split()))
n=int(input())
f=0
for i in range(n):
    b=set(map(int, input().split()))
    if len(b.difference(a))!=0:
        f=1
    else:
        if len(b)==len(a):
            f=1
if f==0:
    print ("True")
else:
    print ("False")

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

n=int(input())
m=int(input())
o=math.sqrt((m*m)+(n*n))
an = math.acos(m/o )
de=math.degrees(an)
print(round(de),chr(176),sep='' )

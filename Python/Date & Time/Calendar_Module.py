# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
a=input()
split=a.split(' ')
day=int(split[1])
month=int(split[0])
year=int(split[2])
b=calendar.weekday(year, month, day)
switcher={
    6:'SUNDAY',
    0:'MONDAY',
    1:'TUESDAY',
    2:'WEDNESDAY',
    3:'THURSDAY',
    4:'FRIDAY',
    5:'SATURDAY'
    }
print(switcher.get(b,"Invalid day of week"))

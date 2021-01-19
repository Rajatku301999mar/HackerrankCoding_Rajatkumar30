from collections import OrderedDict

N = int(input())
items = OrderedDict()
for i in range(N):
    *item_name,price = input().split()
    try:
        items[' '.join(item_name)] += int(price)
    except KeyError:
        items[' '.join(item_name)] = int(price)

for it in items:
    print(it,items[it])

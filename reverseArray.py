list1 = [1,2,3,4,5,5]
list2 = []

for x in range(0,len(list1)-1):
    list2.insert(0, list1[x])

print(list1)
print(list2)
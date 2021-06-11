list1=[12,14,-95,3]
list2=[]
list3=[]
for i in range (0,len(list1)):
    if list1[i]<=0:
        list3.append(list1[i])
    else:
        list2.append(list1[i])
print(list2)
